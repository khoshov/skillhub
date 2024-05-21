from bs4 import BeautifulSoup
from pytils.translit import slugify


def slugify_reach_text(raw_html):
    """
    Generate a slug from the given raw HTML by first cleaning the text and then creating a slug.

    :param raw_html: A string containing raw HTML that needs to be slugified.
    :return: A slugified version of the cleaned text.
    """
    clean_text = BeautifulSoup(raw_html, "lxml").text
    return slugify(clean_text)
