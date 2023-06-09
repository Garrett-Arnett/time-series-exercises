#standard ds imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import env

sns.set()

#imports
import os
import requests
import datetime


################################## Store Acquire Function ############################  

def get_connection(db):
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{db}'


def acquire_store():
    
    filename = 'store.csv'
    
    if os.path.exists(filename):
        
        return pd.read_csv(filename)
    
    else:
        
        query = '''
                SELECT sale_date, sale_amount,
                item_brand, item_name, item_price,
                store_address, store_zipcode
                FROM sales
                LEFT JOIN items USING(item_id)
                LEFT JOIN stores USING(store_id)
                '''
        
        url = get_connection(db='tsa_item_demand')
        
        df = pd.read_sql(query, url)
        
        df.to_csv(filename, index=False)
        
        return df
    
    
################################## Planet Acquire and CSV Function ############################


def get_planet_data():
    '''
    This function creates a csv of planet data if one does not exist
    if one already exists, it uses the existing csv 
    and brings it into pandas as dataframe
    '''
    if os.path.isfile('sw_planet.csv'):
        df = pd.read_csv('sw_planet.csv', index_col=0)
    
    else:
        response = requests.get('https://swapi.dev/api/planets/')
        data = response.json()
        df = pd.DataFrame(data['results'])
        while data['next'] != None:
            print(data['next'])
            response = requests.get(data['next'])
            data = response.json()
            df = pd.concat([df, pd.DataFrame(data['results'])], ignore_index=True)
        df.to_csv('sw_planet.csv')

    return df


################################## Starships Acquire and CSV Function ############################


def get_starships_data():
    '''
    This function creates a csv of starship data if one does not exist
    if one already exists, it uses the existing csv 
    and brings it into pandas as dataframe
    '''
    if os.path.isfile('sw_starships.csv'):
        df = pd.read_csv('sw_starships.csv', index_col=0)
    
    else:
        response = requests.get('https://swapi.dev/api/starships/')
        data = response.json()
        df = pd.DataFrame(data['results'])
        while data['next'] != None:
            print(data['next'])
            response = requests.get(data['next'])
            data = response.json()
            df = pd.concat([df, pd.DataFrame(data['results'])], ignore_index=True)
        df.to_csv('sw_starships.csv')

    return df



################################## People Acquire and CSV Function ############################


def get_people_data():
    '''
    This function creates a csv of people data if one does not exist
    if one already exists, it uses the existing csv 
    and brings it into pandas as dataframe
    '''
    if os.path.isfile('sw_people.csv'):
        df = pd.read_csv('sw_people.csv', index_col=0)
    
    else:
        response = requests.get('https://swapi.dev/api/people/')
        data = response.json()
        df = pd.DataFrame(data['results'])
        while data['next'] != None:
            print(data['next'])
            response = requests.get(data['next'])
            data = response.json()
            df = pd.concat([df, pd.DataFrame(data['results'])], ignore_index=True)
        df.to_csv('sw_people.csv')

    return df


################################## Germany Acquire and CSV Function ############################


def get_germany_data():
    '''
    This function creates a csv of germany energy data if one does not exist
    if one already exists, it uses the existing csv 
    and brings it into pandas as dataframe
    '''
    if os.path.isfile('germany.csv'):
        df = pd.read_csv('germany.csv', index_col=0)
    
    else:
        url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'
        df = pd.read_csv(url)
        df.to_csv('germany.csv')

    return df
