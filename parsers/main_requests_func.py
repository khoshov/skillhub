""" парсер курсов geekbrains.ru """
import csv
from datetime import datetime, date

import requests
from bs4 import BeautifulSoup
from fake_headers import Headers


month_dict = {
    "01": ("январь", "янв"),
    "02": ("февраль", "фев"),
    "03": ("март", "мар"),
    "04": ("апрель", "апр"),
    "05": ("май"),
    "06": ("июнь", "июн"),
    "07": ("июль", "июл"),
    "08": ("август", "авг"),
    "09": ("сентябрь", "сен"),
    "10": ("октябрь", "окт"),
    "11": ("ноябрь", "ноя"),
    "12": ("декабрь", "дек")
}


base_url = 'https://gb.ru/courses?tab=courses'

def fetch_html(url: str):
    """ функция получения данных с html страницы """
    headers = Headers(headers=True).generate()
    try:
        result = requests.get(url, headers=headers, timeout=10)
        if result.status_code == 200:
            print(f'Ссылка {url} доступна')
            # print(result.content)
            return result.text
        else:
            print(f'Ссылка {url} недоступна, status code {result.status_code}')
            return None
    except(requests.RequestException):
        print(f'Страница не доступна url={url}, проверьте интернет соединение')
        return None


def fetch_all_courses_urls(all_courses_list_page) -> list:
    soup_data = BeautifulSoup(all_courses_list_page, 'lxml')
    url_courses = soup_data.select('#courses-tab a')
    return [f"https://gb.ru{item['href']}" for item in url_courses]


def generate_course_start_year(month: str) -> str:
    """ функция принимает на вход месяц начала курсов в формате "01"-"12" и в зависимости от 
        текущего месяца определяет начнется курс в этом году или следующем"""
    date_today = date.today()
    if date_today.month <= int(month):
        year = date_today.year
    else:
        year = date_today.year + 1
    return year


def find_course_start_date(course_main_info_field) -> list or None:
    if course_main_info_field.select('.courses__inf-column .courses__inf-row'):
        start_dates = []
        for row in course_main_info_field.select('.courses__inf-column .courses__inf-row'):
            day = row.select_one('.day').get_text().strip()
            month = row.select_one('.month').get_text().strip()
            for key, value in month_dict.items():
                if month in value:
                    month = key
                    break
            year = generate_course_start_year(month)
            start_date = datetime.strptime(f'{day} {month} {year}', "%d %m %Y").date()
            start_dates.append(start_date)
    else:
        start_dates = None
    return start_dates


def find_course_price(soup_course_data) -> str:
    course_price_field = soup_course_data.select_one(".course__price")
    if course_price_field.select_one(".course__price__actual"):
        course_price = course_price_field.select_one(
            ".course__price__actual").get_text().strip().replace(' ', '')
    else:
        course_price = course_price_field.get_text().strip().lower()
    return course_price

def load_course_data(main_url):
    all_courses_list_page = fetch_html(main_url)
    all_courses_data = []
    if all_courses_list_page:
        urls = fetch_all_courses_urls(all_courses_list_page)
        for url in urls:
            course_data = fetch_html(url)
            if course_data:
                soup_course_data = BeautifulSoup(course_data, 'lxml')
                if soup_course_data.select_one(".gb__main-wrapper"):
                    # название курса
                    course_name = f'''{soup_course_data.select_one('h1[property="name"]').get_text()}. '''\
                                  f'''{soup_course_data.select_one('div.h2').get_text()}.'''
                    # основная информация о курсе
                    course_main_info_field = soup_course_data.select_one('.courses__inf')
                    for row in course_main_info_field.select('.courses__inf-row'):
                        if row.select_one(".pull-left").get_text().strip().lower() == "формат":
                            course_type = row.select_one(".pull-right").get_text().strip().lower()
                        elif row.select_one(".pull-left").get_text().strip().lower() == "длительность":
                            course_duration = row.select_one(".pull-right").get_text().strip().lower()
                    # дата начала курсов
                    start_dates = find_course_start_date(course_main_info_field)
                    course_price = find_course_price(soup_course_data)

                    full_course_data = [url, course_name, course_type, course_duration, start_dates, course_price]
                    all_courses_data.append(full_course_data)
                else:
                    all_courses_data.append([f'{url} содержит нестандартный шаблон'])
            else:
                all_courses_data.append([f'{url} не доступна'])
    return all_courses_data


def write_data(data):
    with open('gb_course_data.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='|')
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    data = load_course_data(base_url)
    write_data(data)
