import requests
from bs4 import BeautifulSoup
import csv
import re
import os

BASE_URL = "https://diversitydata.virginia.edu"
PATHS = {
    "undergrad": "/Home/Details/Undergraduate%20Students",
    "graduate": "/Home/Details/Graduate%20Students",
    "staff": "/Home/Details/Staff",
    "faculty": "/Home/Details/Faculty",
}

SCHOOLS = {
    "": "",
    "ARCH": "/?group=ARCH%20SCHL",
    "CLAS": "/?group=ARTS%20%26%20SCI",
    "BATT": "/?group=BATTEN%20SCHL",
    "COMM": "/?group=COMM%20SCHL",
    "DARD": "/?group=DARD%20SCHL",
    "EDUC": "/?group=EDUC%20SCHL",
    "ENGR": "/?group=ENGR%20SCHL",
    "LAWS": "/?group=LAW%20SCHL",
    "MEDS": "/?group=MED%20SCHL",
    "NURS": "/?group=NURS%20SCHL",
    "PBPM": "/?group=PBPM",
    "VISI": "/?group=VISITING",
    "MEDG": "/?group=MED%20GRAD",
    "SCPS": "/?group=SCPS",
    "SEMS": "/?group=SEM%20AT%20SEA",
}

def clean(text):
    # rm newlines and commas
    text = re.sub(r'[\r\n,]', '', text)
    if text[0] == ' ':
        text = text.split()[0]
    return text

def scrape_table(path, school=""):
    page = requests.get(BASE_URL + PATHS[path] + SCHOOLS[school])
    table = BeautifulSoup(page.content, 'html.parser').find("table")

    headers = [clean(th.text) for th in table.select("tr th")]

    with open(f"./outputs/{path}_{school}.csv", "w") as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        wr.writerows([[clean(td.text) for td in row.find_all("td")] for row in table.select("tr + tr")])

# begin scraping
os.system('mkdir outputs')
for path in PATHS.keys():
    for school in SCHOOLS.keys():
        print(f'GET: {path} {school}')
        scrape_table(path, school)