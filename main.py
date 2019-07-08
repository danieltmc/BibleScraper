#!/usr/bin/env python3
import os
import requests
from contextlib import closing
from bs4 import BeautifulSoup

base_url = "https://www.biblegateway.com/passage/?search="

book = str(input("Please enter the book of the Bible to scrape.\n"))
translation = str(input("Please enter the translation to use.\n")).upper()
chapter_num = 1
verse_num = 1

if not os.path.exists("Bible"):
    os.mkdir("Bible")
if not os.path.exists("Bible/" + translation):
	os.mkdir("Bible/" + translation)
if not os.path.exists("Bible/" + translation + "/" + book):
	os.mkdir("Bible/" + translation + "/" + book)

full_url = base_url + book + "+" + str(chapter_num) + "&version=" + translation

page = requests.get(full_url)
soup = BeautifulSoup(page.text, "html.parser")

verse = soup.find(class_="text" + book + "-" + str(chapter_num) + "-" + str(verse_num))
verse_list = soup.find(class_="BodyText")
verse_list_contents = verse_list.find_all("a")
