import logging

class ScrapeHearingTracker(object):
    
    def scrape_reviews(url: string, num_pages: int = '1'):
        self.num_pages = num_pages
        self.url = url
        # (1) GET HTML OF MAIN PAGE OF TITLES AND LOOP THROUGH AND SAVE META DATA
        #master list to store end result of scraped webpage
        masterListOfReviews = []

        #scrape pages
        for pageNumber in range(num_pages):
            #if first page, don't edit url
            if pageNumber == 0:
                page = requests.get(url, 'html5lib')
            #else add page num to url
            else:
                nextUrl = url + '&page=' + str(pageNumber)
                logging.info("nextUrl")
                #get new page
                page = requests.get(nextUrl, 'html5lib')
            #split html into list of tables (each post)
            soup = BeautifulSoup(page.content, 'html5lib')
            tables = soup.find_all('tr')

            #remove sponsored post from top of list on first page only
            if pageNumber == 0:
                tables = tables[2:]
                    

        

