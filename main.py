import os
import sys
import rich
def clear_terminal():
    os.system('cls')

with open('list.txt', 'r') as todo:
    clear_terminal()
    for items in todo:
        print(items)