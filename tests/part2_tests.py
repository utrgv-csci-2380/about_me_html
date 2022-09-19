from bs4 import BeautifulSoup
import os
import sys
import re

# container
def test_container():
    soup = BeautifulSoup(open('./about_me_part2.html'), "html.parser")
    try:
        cont = soup.select(".container")
    except:
        cont = None
    assert cont is not None

# row
def test_row():
    soup = BeautifulSoup(open('./about_me_part2.html'), "html.parser")
    try:
        cont = soup.select(re.compile("row"))
    except:
        cont = None
    assert cont is not None

# container
def test_column():
    soup = BeautifulSoup(open('./about_me_part2.html'), "html.parser")
    try:
        cont = soup.select(re.compile("row"))
    except:
        cont = None
    assert cont is not None

# h1
def test_header():
    soup = BeautifulSoup(open('./about_me_part2.html'), "html.parser")
    try:
        header = soup.find("h1")
    except:
        header = None
    assert header is not None

# p
def test_p():
    soup = BeautifulSoup(open('./about_me_part2.html'), "html.parser")
    try:
        p = soup.find("p")
    except:
        p = None
    assert p is not None

# image
def test_img():
    soup = BeautifulSoup(open('./about_me_part2.html'), "html.parser")
    try:
        img = soup.find("img")
    except:
        img = None
    assert img is not None
    assert img.attr['src'] is not None

# table
def test_table():
    soup = BeautifulSoup(open('./about_me_part2.html'), "html.parser")
    try:
        table = soup.find("table")
    except:
        table = None
    assert table is not None

# table headers
def test_tableHeaders():
    soup = BeautifulSoup(open('./about_me_part2.html'), "html.parser")
    try:
        th = soup.find("table").find_all("th")
    except:
        th = None
    assert th is not None

# table rows
def test_tableRows():
    soup = BeautifulSoup(open('./about_me_part2.html'), "html.parser")
    try:
        tr = soup.find("table").find_all("tr")
    except:
        tr = None
    assert tr is not None

# table data
def test_tableData():
    soup = BeautifulSoup(open('./about_me_part2.html'), "html.parser")
    try:
        td = soup.find("table").find_all("td")
    except:
        td = None
    assert td is not None

# unordered list
def test_ul():
    soup = BeautifulSoup(open('./about_me_part2.html'), "html.parser")
    try:
        ul = soup.find("ul")
    except:
        ul = None
    assert ul is not None

# list items x5
def test_li():
    soup = BeautifulSoup(open('./about_me_part2.html'), "html.parser")
    try:
        li = soup.find("ul").find_all("li")
    except:
        li = None
    assert li is not None

# link
def test_link():
    soup = BeautifulSoup(open('./about_me_part2.html'), "html.parser")
    try:
        img = soup.find("a")
    except:
        img = None
    assert img is not None