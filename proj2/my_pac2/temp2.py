import csv

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By




def test_read_csv():
    with open(r"C:\selenium\csv.csv", 'r', encoding='utf-8') as file:
     text_file = csv.reader(file)
     next(text_file)
     my_list = list(text_file)
     print(my_list[2][0])

# for x in my_list [1:] :
#     print(x[0])









