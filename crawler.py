import time
import pandas as pd
import config
import os
import requests

def get_simple_df(df):
    df['tags_str'] = df['tags'].apply(lambda tags: ','.join(tag['name'] for tag in tags))
    return df[['id', 'title', 'body', 'created_at', 'updated_at','likes_count', 'comments_count', 'tags_str',
               'user_permanent_id', 'user_id', 'user_description', 'user_followees_count', 'user_followers_count', 'user_items_count']]

def crawl_qiita(start, end):
    url = 'https://qiita.com/api/v2/items'
    cnf = config.Config()
    h = {'Authorization': 'Bearer '+ cnf.ApiKey}

    date_list = [d.strftime('%Y-%m-%d') for d in pd.date_range(start, end)]
    start_list = date_list[:-1]
    end_list = date_list[1:]
    
    result_dir_path = 'data/qiita'
    sleep_sec = 3.6

    for start, end in zip(start_list, end_list):
        p = {
            'per_page': 100,
            'query': 'created:>{} created:<{}'.format(start, end)
        }

        print("created_date %s : page 1" % start)
        time.sleep(sleep_sec)
        r = requests.get(url, params=p, headers=h)
        total_count = int(r.headers['Total-Count'])
        
        if total_count == 0:
            continue

        df_list = [get_simple_df(pd.io.json.json_normalize(r.json(), sep='_'))]

        if total_count > 100:
            for i in range(2, (total_count -1) // 100 + 2):
                p['page'] = i
                print("created_date %s : page %s" % (start, i))
                time.sleep(sleep_sec)
                r = requests.get(url, params=p, headers=h)
                df_list.append(get_simple_df(pd.io.json.json_normalize(r.json(), sep='_')))
        
        pd.concat(df_list, ignore_index=True).to_csv(os.path.join(result_dir_path, start + '.csv'), index=False)
