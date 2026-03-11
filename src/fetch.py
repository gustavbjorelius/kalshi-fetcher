#!/bin/python3 

import requests

def fetch_markets():
    """ f that fetches market live-data """

    url = "https://api.elections.kalshi.com/trade-api/v2/markets?limit=100"
    r = requests.get(url)
    data = r.json()
    return data

def print_markets(data):
    """print selected markets """

    
    for i, market in enumerate(data['markets']): 
    # but i thought we shold not not use for looks for dicts
        
        print(market['title'], market['last_price'])
    

if __name__ == '__main__':
    data = fetch_markets()
    print_markets(data)
