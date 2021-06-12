import csv
import re
from datetime import datetime
from typing import Dict

import requests
import requests_random_user_agent  # автоматически подставляет случайный user-agents, нужен только импорт
from bs4 import BeautifulSoup
from loguru import logger

logger.add(
    'debug.log',
    format='{time} {level} {message}',
    level="DEBUG",
    encoding='utf-8'
)

home_page_url = 'https://tutortop.ru/'
url = 'https://tutortop.ru/courses_selection/kursy_po_devops/'


@logger.catch
def fetch_html(url: str) -> str:
    """ функция получения данных с html страницы """
    try:
        result = requests.get(url, timeout=10)
        if result.status_code == 200:
            logger.info(f"парсинг ссылки {url}")
            return result.text
        else:
            logger.error(f'Ссылка {url} недоступна, status code {result.status_code}')
            return None
    except(requests.RequestException):
        logger.error(f'Страница не доступна url={url}, проверьте интернет соединение')
        return None


@logger.catch
def load_main_page_course_links(home_page_url: str) -> Dict:
    courses_links = {}
    houme_page_soup_data = BeautifulSoup(fetch_html(home_page_url), 'lxml')
    courses_catalog = houme_page_soup_data.select(".submenu__wrap__mark")[0].select("a")
    for item in courses_catalog[1:]:
        courses_links[item.get_text()] = item['href']
    return courses_links


@logger.catch
def load_courses_data_by_categoly_url(url: str, course_category: str):
    courses_page_soup_data = BeautifulSoup(fetch_html(url), 'lxml')
    courses_data_by_categoly = fetch_all_paid_courses_data_by_categoly(courses_page_soup_data, course_category) + (
        fetch_all_free_courses_data_by_categoly(courses_page_soup_data, course_category))
    return courses_data_by_categoly


@logger.catch
def fetch_all_paid_courses_data_by_categoly(courses_page_soup_data, course_category: str):
    all_paid_couses_in_category = []
    courses_table = courses_page_soup_data.select('.tab-course-paid .tab-course-item')
    for course_item in courses_table:
        school = course_item['data-school']
        course_title = course_item.select_one('.m-course-title').get_text().strip()
        course_price = course_item['data-price']
        course_start_date = render_course_start_date(course_item)
        course_duration = f"{course_item['data-dlitelnost']} мес."
        course_link = find_course_url(course_item)
        all_paid_couses_in_category.append([
            course_category,
            course_title,
            school,
            course_price,
            course_start_date,
            course_duration,
            course_link
        ])
    return all_paid_couses_in_category


@logger.catch
def fetch_all_free_courses_data_by_categoly(courses_page_soup_data, course_category: str):
    all_free_couses_in_category = []
    courses_table = courses_page_soup_data.select('.tab-free-course .tab-course-item')
    for course_item in courses_table:
        school = course_item['data-school']
        course_title = course_item.select_one('.m-course-title').get_text().strip()
        course_price = None
        course_start_date = None
        course_duration = f"{course_item['data-dlitelnost']} зан."
        course_link = find_course_url(course_item)
        course_format = course_item.select_one('.tab-course-col-format_obucheniy').get_text().strip()
        all_free_couses_in_category.append([
            course_category,
            course_title,
            school,
            course_price,
            course_start_date,
            course_duration,
            course_link,
            course_format,
        ])
    return all_free_couses_in_category


@logger.catch
def find_course_url(course_row_data: str) -> str:
    """ Функция поиска ссылки на курс из генератора аффилированной ссылки """
    course_referal_url = course_row_data.select_one('a.tab-link-course')['href']
    course_referal_url_generator = fetch_html(course_referal_url)
    pattern_1 = r"\?dl=(.+?)(';|#|\?ref|&subid)"
    pattern_2 = r"ulp=(.+)';"
    pattern_3 = r"href\s=\s'(.+?)(\?unit|'|\?utm|\?ref)"
    if re.search(pattern_1, course_referal_url_generator):
        return re.search(pattern_1, course_referal_url_generator).group(1)
    elif re.search(pattern_2, course_referal_url_generator):
        return re.search(pattern_2, course_referal_url_generator).group(1)
    elif re.search(pattern_3, course_referal_url_generator):
        return re.search(pattern_3, course_referal_url_generator).group(1)
    else:
        logger.error(f'не удалось получить ссылку на курс для {course_referal_url}')
        return course_referal_url


@logger.catch
def render_course_start_date(course_row_data):
    """  функция определения даты начала курса """
    start_date_row_data = course_row_data['data-date']
    if start_date_row_data == "0":
        return None
    else:
        return str(datetime.fromtimestamp(int(start_date_row_data)).date())


@logger.catch
def write_data(data):
    with open('tutortop_course_data.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='|')
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    courses_category_links = load_main_page_course_links(home_page_url)
    for category, url in courses_category_links.items():
        data = load_courses_data_by_categoly_url(url, category)
        # logger.info(data)
        write_data(data)
