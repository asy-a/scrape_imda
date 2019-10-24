import warnings, sys, time, os
import pandas as pd
import re
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

def scrape_page1(url, chromedriver_path):

    page_list = []
    film_title_list = []
    award_name_list = []
    description_list = []
    produced_by_list = []
    produced_by_links_list = []
    producer_list = []
    producer_links_list = []
    director_list = []
    director_link_list = []
    genre_list = []
    language_list = []
    running_time_list = []
    format_list = []
    key_cast_list = []
    international_sales_distribution_list = []
    contact_list = []
    release_year_list = []

    for i in range(1, 13):

        browser = webdriver.Chrome(executable_path=chromedriver_path)
        browser.get(url)

        page = 1

        browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/div/section[2]/div[1]/div[2]/div/div[{}]/a'.format(i)).click()
        print('clicked film')

        film_title = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/div/div/h1').text
        print('film_title' + ': ' + str(film_title))

        try:
            award_name = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/section/section/div/div[2]/div[1]/div/ul/li/span[1]').text
            print('award_name' + ': ' + str(award_name))
            awarding_organisation = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/section/section/div/div[2]/div[1]/div/ul/li/span[2]').text
            print('awarding_organisation' + ': ' + str(awarding_organisation))
        except:
            pass
            print('no award for ' + str(film_title))
            award_name = 'None'
            awarding_organisation = 'None'

        description = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/section/section/div/div[2]/div[2]/p').text
        print('film_description' + ': ' + str(description))

        produced_by = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/section/section/div/div[2]/div[2]/section/div[1]/div').text
        print('produced_by' + ': ' + str(produced_by))
        try:
            try:
                produced_by_links = []
                for num in range(1,6):
                    produced_by_link = browser.find_element_by_xpath('//*[@id="content_0_ctl03_ProducedBy"]/a[{}]'.format(num)).get_attribute('href')
                    produced_by_links.append(produced_by_link)
                    print('produced_by_link' + ': ' + str(produced_by_link))
            except:
                pass
                produced_by_links = ', '.join(produced_by_links)
        except:
            pass

        producer = browser.find_element_by_xpath('//*[@id="content_0_ctl03_Producers"]').text
        print('producer' + ': ' + str(producer))
        try:
            try:
                producer_links = []
                for num in range(1,6):
                    producer_link = browser.find_element_by_xpath('//*[@id="content_0_ctl03_Producers"]/a[{}]'.format(num)).get_attribute('href')
                    producer_links.append(producer_link)
                    print('producer_link' + ': ' + str(producer_link))
            except:
                pass
                producer_links = ', '.join(producer_links)
        except:
            pass

        director = browser.find_element_by_xpath('//*[@id="content_0_ctl03_DirectedBy"]').text
        print('director' + ': ' + str(director))

        try:
            director_link = browser.find_element_by_xpath('//*[@id="content_0_ctl03_DirectedBy"]/a').get_attribute('href')
            print('director_link' + ': ' + str(director_link))
        except:
            pass
            print('no director link for ' + str(film_title))
            director_link = 'None'

        genre = browser.find_element_by_xpath('//*[@id="content_0_ctl03_Genre"]').text
        print('genre' + ': ' + str(genre))

        language = browser.find_element_by_xpath('//*[@id="content_0_ctl03_Language"]').text
        print('language' + ': ' + str(language))

        running_time = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/section/section/div/div[2]/div[2]/section/div[6]/div/p').text
        print('running_time' + ': ' + str(running_time))

        format = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/section/section/div/div[2]/div[2]/section/div[7]/div/p').text
        print('format' + ': ' + str(format))

        key_cast = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/section/section/div/div[2]/div[2]/section/div[8]/div').text
        print('key_cast' + ': ' + str(key_cast))

        international_sales_distribution = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/section/section/div/div[2]/div[2]/section/div[9]/div').text
        print('international_sales_distribution' + ': ' + str(international_sales_distribution))

        contact = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/section/section/div/div[2]/div[2]/section/div[10]/div').text
        print('contact' + ': ' + str(contact))

        release_year = browser.find_element_by_xpath('//*[@id="content_0_ctl03_YearOfRelease"]').text
        print('release_year' + ': ' + str(release_year))

        page_list += [page]
        film_title_list += [film_title]
        award_name_list += [award_name]
        description_list += [description]
        produced_by_list += [produced_by]
        produced_by_links_list += [produced_by_links]
        producer_list += [producer]
        producer_links_list += [producer_links]
        director_list += [director]
        director_link_list += [director_link]
        genre_list += [genre]
        language_list += [language]
        running_time_list += [running_time]
        format_list += [format]
        key_cast_list += [key_cast]
        international_sales_distribution_list += [international_sales_distribution]
        contact_list += [contact]
        release_year_list += [release_year]

    data = {'page': page_list, 'film_title': film_title_list, 'award_name': award_name_list,
            'description': description_list, 'produced_by': produced_by_list, 'produced_by_links': produced_by_links_list,
            'producer': producer_list, 'producer_links': producer_links_list, 'director': director_list, 'director_link': director_link_list,
            'genre': genre_list, 'language': language_list, 'running_time': running_time_list, 'format': format_list,
            'key_cast': key_cast_list, 'international_sales_distribution': international_sales_distribution_list, 'contact': contact_list, 'release_year': release_year_list}
    df = pd.DataFrame(data)

    return df

    # film = BeautifulSoup(browser.page_source, 'html.parser')
    #
    # title = film.title
    # print(title)
    # awards = film.find_all('ul', attrs={'class': 'awards__list'})
    # print(awards)
    # info = film.find_all('div', attrs={'class': 'info'})
    # print(info)

    a=1


def get_links(pg_list, chromedriver_path, link1, img_dir):

    df_list = []

    for pg_idx in pg_list:
        link_search = 'https://www2.imda.gov.sg/api/SearchResult/filmDirectory?itemperpage=12&page={}&search=&year=&language=&genre=&feature='.format(pg_idx)
        r = requests.get(link_search)
        json_data = r.json()
        l = json_data['listing']
        films = [d['link'] for d in l]

        page_list = []
        film_title_list = []
        award_name_list = []
        awarding_organisation_list = []
        description_list = []
        produced_by_list = []
        produced_by_links_list = []
        producer_list = []
        producer_links_list = []
        director_list = []
        director_link_list = []
        genre_list = []
        language_list = []
        running_time_list = []
        format_list = []
        key_cast_list = []
        international_sales_distribution_list = []
        contact_list = []
        release_year_list = []
        trailer_link_list = []
        img_links_list = []

        film_num = len(films)

        for index, film_idx in enumerate(films):

            print('Downloading {} of {} film at page {}'.format(index + 1, film_num, pg_idx))

            url_full = link1 + film_idx
            browser = webdriver.Chrome(executable_path=chromedriver_path)
            browser.get(url_full)

            film_title = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/div/div/h1').text
            print('film_title: ' + str(film_title))

            try:
                award_name = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/section/section/div/div[2]/div[1]/div/ul/li/span[1]').text
                print('award_name' + ': ' + str(award_name))
                awarding_organisation = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/section/section/div/div[2]/div[1]/div/ul/li/span[2]').text
                print('awarding_organisation' + ': ' + str(awarding_organisation))
            except:
                pass
                print('no award for ' + str(film_title))
                award_name = 'None'
                awarding_organisation = 'None'

            description = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/section/section/div/div[2]/div[2]/p').text
            print('film_description: ' + str(description))

            produced_by = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/section/section/div/div[2]/div[2]/section/div[1]/div').text
            print('produced_by' + ': ' + str(produced_by))
            try:
                try:
                    produced_by_links = []
                    for num in range(1,4):
                        produced_by_link = browser.find_element_by_xpath('//*[@id="content_0_ctl03_ProducedBy"]/a[{}]'.format(num)).get_attribute('href')
                        produced_by_links.append(produced_by_link)
                        print('produced_by_link: ' + str(produced_by_link))
                except:
                    pass
                    produced_by_links = ', '.join(produced_by_links)
            except:
                pass

            producer = browser.find_element_by_xpath('//*[@id="content_0_ctl03_Producers"]').text
            print('producer' + ': ' + str(producer))
            try:
                try:
                    producer_links = []
                    for num in range(1,4):
                        producer_link = browser.find_element_by_xpath('//*[@id="content_0_ctl03_Producers"]/a[{}]'.format(num)).get_attribute('href')
                        producer_links.append(producer_link)
                        print('producer_link: ' + str(producer_link))
                except:
                    pass
                    producer_links = ', '.join(producer_links)
            except:
                pass

            director = browser.find_element_by_xpath('//*[@id="content_0_ctl03_DirectedBy"]').text
            print('director: ' + str(director))

            try:
                director_link = browser.find_element_by_xpath('//*[@id="content_0_ctl03_DirectedBy"]/a').get_attribute('href')
                print('director_link: ' + str(director_link))
            except:
                pass
                print('no director link for ' + str(film_title))
                director_link = 'None'

            genre = browser.find_element_by_xpath('//*[@id="content_0_ctl03_Genre"]').text
            print('genre: ' + str(genre))

            language = browser.find_element_by_xpath('//*[@id="content_0_ctl03_Language"]').text
            print('language: ' + str(language))

            running_time = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/section/section/div/div[2]/div[2]/section/div[6]/div/p').text
            print('running_time: ' + str(running_time))

            format = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/section/section/div/div[2]/div[2]/section/div[7]/div/p').text
            print('format: ' + str(format))

            key_cast = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/section/section/div/div[2]/div[2]/section/div[8]/div').text
            print('key_cast: ' + str(key_cast))

            international_sales_distribution = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/section/section/div/div[2]/div[2]/section/div[9]/div').text
            print('international_sales_distribution: ' + str(international_sales_distribution))

            contact = browser.find_element_by_xpath('//*[@id="form1"]/div[4]/section/section/section/section/div/div[2]/div[2]/section/div[10]/div').text
            print('contact: ' + str(contact))

            release_year = browser.find_element_by_xpath('//*[@id="content_0_ctl03_YearOfRelease"]').text
            print('release_year' + ': ' + str(release_year))

            # read the html of each film page
            r2 = requests.get(url_full)
            html_doc = r2.text
            film_pg = BeautifulSoup(html_doc)


            for link in film_pg.findAll('iframe', attrs={'src': re.compile("^ https://www.youtube|^https://player|^https://www.youtube")}):
                print('trailer link: ' + link.get('src'))
                trailer_link = link.get('src')

            # get the links for images stored in page and put into list to click and save using Selenium
            img_partial_link = []
            for link in film_pg.findAll('a', attrs={'href': re.compile("^/-/media/Imda/Images/SFC/Film-Photo-Gallery")}):
                print(link.get('href'))
                img_partial_link.append(link.get('href'))

            img_full_link = []
            for i in img_partial_link:
                img_link2 = link1 + i
                img_full_link.append(img_link2)
            img_links_record = ', '.join(img_full_link)

            # append all records into a list for each film
            page_list += [pg_idx]
            film_title_list += [film_title]
            award_name_list += [award_name]
            awarding_organisation_list += [awarding_organisation]
            description_list += [description]
            produced_by_list += [produced_by]
            produced_by_links_list += [produced_by_links]
            producer_list += [producer]
            producer_links_list += [producer_links]
            director_list += [director]
            director_link_list += [director_link]
            genre_list += [genre]
            language_list += [language]
            running_time_list += [running_time]
            format_list += [format]
            key_cast_list += [key_cast]
            international_sales_distribution_list += [international_sales_distribution]
            contact_list += [contact]
            release_year_list += [release_year]
            trailer_link_list += [trailer_link]
            img_links_list += [img_links_record]

            # call function to save images in list of jpg links
            # save_images(img_dir, img_full_link, film_title)

        # save the lists of film records into a dictionary for each page
        data = {'page': page_list, 'film_title': film_title_list, 'award_name': award_name_list, 'awarding_organisation': awarding_organisation_list,
                'description': description_list, 'produced_by': produced_by_list, 'produced_by_links': produced_by_links_list,
                'producer': producer_list, 'producer_links': producer_links_list, 'director': director_list, 'director_link': director_link_list,
                'genre': genre_list, 'language': language_list, 'running_time': running_time_list, 'format': format_list,
                'key_cast': key_cast_list, 'international_sales_distribution': international_sales_distribution_list, 'contact': contact_list, 'release_year': release_year_list,
                'trailer_link': trailer_link_list, 'img_links': img_links_list}

        # convert dictionary into a dataframe for each page
        df_append = pd.DataFrame(data)
        # list of dataframes keep appending for each page
        df_list.append(df_append)

    # concatenate all pages
    df = pd.concat(df_list)

    return df


def save_images(img_dir, img_full_link, film_title):

    length = len(img_full_link)
    fname = re.sub('[/:><=]\s?', '_', film_title)

    for index, img in enumerate(img_full_link):
        print('Downloading {0} of {1} images'.format(index + 1, length))
        with open('{}/{}_{}.jpg'.format(img_dir, fname, index + 1), "wb") as f:
            f.write(requests.get(img).content)


def main():

    # url = 'https://www2.imda.gov.sg/for-industry/sectors/Media/film/directory?search='

    # df1 = scrape_page1(url, chromedriver_path)
    # df1.to_csv('imda_page1.csv')
    #
    # page = 5
    # df2 = scrape_page(url, chromedriver_path, page)
    # df2.to_csv('imda_page5.csv')

    # for pg_idx in range(1,3):
    #     df = connect_site(url, chromedriver_path, pg_idx)
    #     df = df.append(df)

    # pg_list = [1, 5, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    pg_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    chromedriver_path = '../webdriver/chromedriver.exe'
    link1 = 'https://www2.imda.gov.sg'
    img_dir = '../../../imda_images'
    df = get_links(pg_list, chromedriver_path, link1, img_dir)

    df.to_csv('imda_all_img.csv')


if __name__ == "__main__":

    main()