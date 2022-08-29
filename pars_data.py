import os
import os.path
import json
from auc_scan_data import DATABASE


def main_data_from_lua():
    wow_auction_db = f'E:\Games\Sirus\World of Warcraft Sirus\WTF\Account\GRINO111\SavedVariables\Auctionator.lua'
    file_auc_db = os.path.abspath(wow_auction_db)
    with open(file_auc_db, 'r', encoding='utf-8') as f:
        bd_line = """ """
        for line in f:
            bd_line += line

    AUC_price_db = bd_line.split('AUCTIONATOR_PRICE_')[1].split('AUCTIONATOR_POSTING_HISTORY')[0]
    AUC_price_db = AUC_price_db.replace('=', ':').replace('[', '').replace(']', '')
    name_var, data_var = AUC_price_db[:8], AUC_price_db[10:]
    AUC_price_db = name_var + "=" + data_var

    with open('auc_scan_data.py', 'w', encoding='utf-8') as f:
        f.write(AUC_price_db)

    main_data = DATABASE["Sirus x5 - 3.3.5a+"]

    for item in main_data.keys():
        if type(main_data[item]) == dict:
            main_data[item] = main_data[item]['m']
            main_data[item] = {'price': main_data[item] / 10000}

    # for item in main_data.keys():
    #     if type(main_data[item]) == dict:
    #         main_data[item] = main_data[item]['m']
    #         # print(main_data[item]['m'])
    #     main_data[item] = {'price' : main_data[item] / 10000}

    # with open('auction_prices.json', 'w', encoding='utf-8') as f:
    #     json.dump(DATABASE, f, indent=4, ensure_ascii=False)

    with open('wow_database/auction_prices.json', 'w', encoding='utf-8') as f:
        json.dump(main_data, f, indent=4, ensure_ascii=False)


main_data_from_lua()
