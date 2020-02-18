import requests
from bs4 import BeautifulSoup
import csv
import re

BASE_URL = "https://diversitydata.virginia.edu"
PATHS = {
    "undergrad": "/Home/Details/Undergraduate%20Students",
}

page = requests.get(BASE_URL + PATHS["undergrad"])
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find("table")

def nl_rm(text):
    # removes newline characters and commas
    return re.sub(r'[\r\n,]', '', text)

def clean(text):
    text = nl_rm(text)
    if text[0] == ' ':
        text = text.split()[0]
    return text

# thx to https://stackoverflow.com/questions/38917958/convert-html-into-csv
# for the table -> csv code
# don't use .encode("utf-8") bc makes everything show up like b'haha'
headers = [clean(th.text) for th in table.select("tr th")]

with open("output.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(headers)
    wr.writerows([[clean(td.text) for td in row.find_all("td")] for row in table.select("tr + tr")])