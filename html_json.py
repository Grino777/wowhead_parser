from bs4 import BeautifulSoup
import json

def parsing_data_from_html(template=None):
    with open(template, 'r', encoding='utf-8') as file:
        file = file.read()
        soup = BeautifulSoup(file, 'lxml')
        for i in soup.find_all('script'):
            if 'WH.Gatherer.addData' in i.text:
                i = i.text
                with open('test_wow_db.json', 'w', encoding='utf-8') as db:
                    db_to_json = i[i.index('{'):i.find('}});') + 2]
                    items_info = json.loads(db_to_json)
                    return items_info
            else:
                continue

def main():
    parsing_data_from_html()

if __name__ == '__main__':
    main()