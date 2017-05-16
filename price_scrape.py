from __future__ import print_function
import os.path
from collections import defaultdict
import string
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

url_list = ['https://factory.jcrew.com/mens-clothing/shirts.jsp?iNextCategory=-1',
'https://factory.jcrew.com/mens-clothing/sweaters.jsp?iNextCategory=-1',
'https://factory.jcrew.com/mens-clothing/tees_polos_fleece.jsp?iNextCategory=-1',
'https://factory.jcrew.com/mens-clothing/sweatshirts_sweatpants.jsp?iNextCategory=-1',
'https://factory.jcrew.com/mens-clothing/jackets_outerwear.jsp?iNextCategory=-1',
'https://factory.jcrew.com/mens-clothing/denim_sm.jsp?iNextCategory=-1',
'https://factory.jcrew.com/mens-clothing/pants.jsp?iNextCategory=-1',
'https://factory.jcrew.com/mens-clothing/shorts.jsp?iNextCategory=-1',
'https://factory.jcrew.com/mens-clothing/suiting.jsp?iNextCategory=-1',
'https://factory.jcrew.com/mens-clothing/ties_pocket_squares.jsp?iNextCategory=-1',
'https://factory.jcrew.com/mens-clothing/accessories.jsp?iNextCategory=-1',
'https://factory.jcrew.com/mens-clothing/socks.jsp?iNextCategory=-1',
'https://factory.jcrew.com/mens-clothing/boxers_sleepwear.jsp?iNextCategory=-1']

for url in url_list:
    result = requests.get(url)
    c = result.content
    soup = BeautifulSoup(c, 'html.parser')

    summary = soup.find("div", {"id": "prodArray"})
    products = summary.find_all("ul", {"id": "arrayProdInfo"})

    prod_link = []
    prod_name = []
    red_price = []

    for row in products:
        infos = row.find_all('li')

        col_0 = infos[0].find('a')
        prod_link.append(col_0)

        col_1 = infos[0].string.strip()
        prod_name.append(col_1)

        col_2 = infos[2].find('span',{'class':'priceDifferentFromLabel'}).string.strip()
        red_price.append(float(col_2[1:]))

    fields = {'prod_link': prod_link, 'prod_name': prod_name, 'red_price': red_price}
    df = pd.DataFrame(fields)
    print(df)