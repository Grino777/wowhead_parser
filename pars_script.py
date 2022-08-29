from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



def get_template_page(url):
    # browser_options = Options()
    # browser_options.add_argument('--headless')
    # browser_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(executable_path='webdriver/chromedriver.exe')
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.maximize_window()

    try:
        driver.get(url=url)
        sleep(5)

        while True:
            # find_end_element = driver.find_element(By.TAG_NAME, 'script')
            find_end_element = driver.find_element(By.CLASS_NAME, 'footer-navigation')

            if driver.find_element(By.CLASS_NAME, 'listview-band-bottom'):
                # with open('templates/0.html', 'w', encoding='utf-8') as file:
                    # file.write(find_end_element)
                    # file.write(driver.page_source)
                break

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
    get_template_page(url)


if __name__ == '__main__':
    main()
