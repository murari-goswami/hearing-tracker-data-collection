from datetime import datetime

import requests
from bs4 import BeautifulSoup
from loguru import logger
from util.gen_date import get_numerical_date


class Scrape():
    def __init__(self, uri: str):
        self.uri = uri

    def reviews(self, num_pages: int = 1):
        # master list to store end result of scraped webpage
        master_list_of_reviews = []
        review_index = 0
        curr_review_datetime = datetime.date()

        # scrape pages
        for page_number in range(num_pages):
            # if first page, don't edit url
            if page_number == 0:
                logger.info(self.uri)
                page = requests.get(self.uri, 'html5lib')
            # else add page num to url
            else:
                next_uri = self.uri + '&page=' + str(page_number)
                logger.info(next_uri)
                # get new page
                page = requests.get(next_uri, 'html5lib')

            # split html into list of tables (each post)
            soup = BeautifulSoup(page.content, 'html5lib')
            tables = soup.find_all('tr')

            # remove sponsored post from top of list on first page only
            if page_number == 0:
                tables = tables[2:]

            # loop through each post
            for table in tables:
                # set data fields to fill
                title_row = []

                responses = {}
                category = ""
                description = ""
                title = ""
                date_string = ""
                link = ""
                username = ""
                replies = 0
                views = 0
                combined_text = ""
                title_description = ""

                try:
                    review_index += 1
                except:
                    review_index = 0

                # break each post into each line as a string
                for line in str(table).split('\n'):
                    if 'Original Poster' in line:
                        username = line[line.index('=') + 2:line.index('Original') - 3]
                    if 'span class="views"' in line:
                        temp = line[line.index('span&gt;') + 11:]
                        try:
                            views = int(temp[:temp.index('<')])
                        except:
                            views = 0
                    # get num replies
                    if 'span class="posts"' in line:
                        try:
                            replies = int(line[line.index('>') + 1:line.index('/') - 1])
                            replies = replies - 1
                        except:
                            replies = 0
                    # find title and link to responses
                    if 'meta content' in str(line):
                        # differentiate between title and link
                        # get title
                        if 'https' not in line:
                            if '"position"/' not in line:
                                temp = line[line.index('=') + 2:]
                                title = temp[:temp.index('"')]
                                combined_text += title
                                combined_text += ' '
                                title_description += title
                                title_description += ' '
                        else:
                            # avoid images
                            if '.jpeg' not in line:
                                temp_link = line[line.index('=') + 2:]
                                link = temp_link[:temp_link.index('"')]
                    # find date
                    if ',' and '20' in line:
                        if len(line.strip()) <= 18:
                            date_string = get_numerical_date(line.strip())
                            dat_list = date_string.split('-')
                            curr_review_datetime = datetime(int(dat_list[2]), int(dat_list[0]), int(dat_list[1]))
                    # find category
                    if '"category-name"' in line:
                        cat = line[line.index('>') + 1:]
                        category = cat[:cat.index('<')]

                # (2) ADD TITLE DATA TO CURRENT ROW AND FIND PRESENT BRANDS AND PRODUCTS
                # add data to list
                title_row.append(curr_review_datetime)
                title_row.append(category)
                title_row.append(int(views))
                title_row.append(int(replies))
                title_row.append(username)
