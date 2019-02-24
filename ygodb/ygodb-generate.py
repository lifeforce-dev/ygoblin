# ygodb-generate.py
#
# Extract a plain text list of all yu-gi-oh card names in existence from html
# fetched from an online db.
#

import logging
import os
import re
import requests
import string
import sys
import time

from lxml import html
from retrying import retry
from scrapy import Selector

GENERATED_DIR_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  'generated')
LOG_FILE_DIR_NAME = os.path.join(GENERATED_DIR_NAME, 'logs')
HTML_DUMP_DIR_NAME = os.path.join(GENERATED_DIR_NAME, 'html-dumps')
CARD_NAMES_FILE_PATH = os.path.join(GENERATED_DIR_NAME, 'card-name-list.txt')
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR_NAME, 'log.txt')


def clear_file(file_name):
    if os.path.isfile(file_name):
        file = open(file_name, 'w')
        file.close()


def clear_files(files):
    for file in files:
        clear_file(file)


def write_card_names_to_file(names, file):
    file.flush()
    for name in names:
        encoded_name = name
        print(encoded_name)
        file.write(encoded_name + ',')


def extract_card_names_from_set(html_content):
    # Grabs all of the card names from the html file.
    return html_content.xpath('//*[@class="card_status"]/strong/text()')


def on_fetch_decoded_html_failed(url, e):
    logging.error('Error fetching url.'
                  + ' error=' + e
                  + ' url=' + url)


def write_html_to_file(set_name, pid, html_text):
    # On NTFS, ':' specifies multiple data streams and are not considered as
    # part of the file name.
    # https://docs.microsoft.com/en-us/sysinternals/downloads/streams
    set_name = set_name.replace(':', '-')

    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    file_name = ''.join(c for c in set_name if c in valid_chars)
    file_name = file_name.replace(' ', '_')
    file_name = "{0}-{1}.html".format(file_name, pid)

    path = os.path.join(HTML_DUMP_DIR_NAME, file_name)

    try:
        with open(path, "w+", encoding='utf-8') as html_dump_file:
            html_dump_file.write(html_text)
    except OSError as e:
        logging.error('Failed to create html dump. '
                      + ' error=' + e.strerror
                      + ' file_name=' + path)


@retry(stop_max_attempt_number=10, wait_exponential_multiplier=2000,
       wait_exponential_max=10000)
def fetch_decoded_html_content(url):
    try:
        html_text = requests.get(url).text
    except Exception as e:
        on_fetch_decoded_html_failed(url, e)

    return html_text


def build_sets_from_content(html_content):
    # Gather pids from links, gather set names, zip em up
    links = html_content.xpath('//*[@class="link_value"]/@value')
    p = re.compile(r'(\d{8})')

    pids = [p.search(link).group() for link in links]

    set_names = html_content.xpath('//*[@class="pack pack_en"]/strong/text()')
    return zip(pids, set_names)


def generate(sets, output_file):
    for pid, set_name in sets:
        print('Downloading card names for ' + set_name + ' , ' + pid + '...')

        set_url = ('https://www.db.yugioh-card.com/yugiohdb/card_search.action'
                   '?ope=1&sess=1&pid=' + pid + '&rp=99999')

        set_html_content = fetch_decoded_html_content(set_url)
        write_html_to_file(set_name, pid, set_html_content)

        names = extract_card_names_from_set(html.fromstring(set_html_content))
        write_card_names_to_file(names, output_file)


def initialize_dirs():
    os.makedirs(GENERATED_DIR_NAME, exist_ok=True)
    os.makedirs(LOG_FILE_DIR_NAME, exist_ok=True)
    os.makedirs(HTML_DUMP_DIR_NAME, exist_ok=True)


def main():
    # TODO: Arg Parse to allow for downloading a specified set only.
    initialize_dirs()

    logging.basicConfig(filename=LOG_FILE_PATH, level=logging.INFO)
    files_to_clear = [CARD_NAMES_FILE_PATH, LOG_FILE_PATH]
    clear_files(files_to_clear)

    html_content = fetch_decoded_html_content('https://www.db.yugioh-card.com/'
                                              'yugiohdb/card_list.action')
    sets = build_sets_from_content(html.fromstring(html_content))

    with open(CARD_NAMES_FILE_PATH, 'a+', encoding='utf-8') as card_names_file:
        generate(sets, card_names_file)

        # Remove last delimiter. Readability over performance here.
        # This only happens once.
        card_names_file.seek(card_names_file.seek(0, os.SEEK_END) - 1)
        if card_names_file.buffer.peek(1) == b',':
            card_names_file.truncate()

    print("done...")

if __name__ == "__main__":
    main()
