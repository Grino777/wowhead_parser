from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from html_json import parsing_data_from_html


def get_template_page(url):
    driver = webdriver.Chrome(executable_path='webdriver/chromedriver.exe')
    try:
        driver.get(url=url)
        # sleep(5)

        while True:
            find_end_element = driver.find_element(By.CLASS_NAME, 'footer-navigation')

            if driver.find_element(By.CLASS_NAME, 'listview-band-bottom'):
                html_page_code = driver.page_source
                return parsing_data_from_html(html_page_code)
            else:
                actions = ActionChains(driver)
                actions.move_to_element(find_end_element).perform()
                sleep(3)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    url = 'https://www.wowhead.com/wotlk/ru/items#items;0'
    all_items = {}
    all_items.update(get_template_page(url))
    print(all_items)


if __name__ == '__main__':
    main()
