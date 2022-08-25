import re
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# url = 'https://www.wowhead.com/wotlk/ru/items'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
sp_urls = [f'https://www.wowhead.com/wotlk/ru/items#items;{i}' for i in range(0, 1000, 50)]


def get_data_from_wowhead(*args, **kwargs):
    template = re.compile(r'[*(\d)]{3,}')
    all_data = dict()
    data_elements = driver.find_elements(By.CLASS_NAME, "listview-row")

    for element in data_elements:
        x = element.find_elements(By.TAG_NAME, 'td')
        item_info = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
        item_id = re.search(template, item_info).group(0)

        var = {item_id: {
            'item_name': x[2].text.split('\n')[0],
            'item_level': x[3].text,
            'item_slot': x[9].text,
            'item_type': x[11].text,
        }}

        all_data.update(var)

    return all_data


def main():
    try:
        for page_url in sp_urls:
            bd_wow = get_data_from_wowhead(driver.get(url=page_url))
            # sleep(random.randrange(1, 5))
            sleep(2)

        # with open('../DB_WOW.json', 'w', encoding='UTF-8') as file:
        #     json.dump(bd_wow, file, indent=4, ensure_ascii=False)

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
