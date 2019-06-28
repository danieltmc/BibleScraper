#!/usr/bin/env python3
import requests
from contextlib import closing
from bs4 import BeautifulSoup

base_url = "https://www.biblegateway.com/passage/?search="

book = str(input("Please enter the book of the Bible to scrape"))
translation = str(input("Please enter the translation to use")).upper()
chapter = 1

if not os.path.exists("Bible"):
    os.mkdir("Bible")
if not os.path.exists("Bible/" + translation):
	os.mkdir("Bible/" + translation)
if not os.path.exists("Bible/" + translation + "/" + book)
	os.mkdir("Bible/" + translation + "/" + book)

full_url = base_url + book + "+" str(chapter) + "&version=" + translation

page = requests.get(full_url)
