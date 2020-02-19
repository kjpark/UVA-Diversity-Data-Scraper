# UVA Diversity Dashboard Scraper

Creates .csv files that can be used for individual analysis. All data is
pulled from the UVA Diversity Dashboard located
(here)[https://diversitydata.virginia.edu].

Already compiled .csv files can be found in the **backup_record** folder if
you don't want to run the script and just get to analyzing. This folder also
exists in the case UVA nukes the resource itself.

## Motivation
- original dashboard can be misleading (compare y-axis between demographics)
- doesn't allow for original data analysis / visualization
- generally poorly designed website: slow, ugly

## How to use
I did this on mac but any bash-like environment should work. Make sure that
python3 is installed. Could take up to a minute based on internet connection.

```
> python3 -m venv env
> source env/bin/activate
> pip install -r requirements.txt
>
> python scrape.py
> deactivate
```

## Issues and Additional Notes
- doesn't grab non-school-specific offices (like student affairs) for
faculty (yet)
- doesn't split data by gender like the website can / does
- This note is included below each table: *Beginning 2009 changes in IPEDS
definition of race and ethnicity were implemented, and many
students/faculty/staff who may have listed themselves as African American in
the earlier federal collection/reporting methodology are now being counted
in the Hispanic or Multi-Race categories. This almost certainly accounts for
some of the decline in the numbers of African American students/faculty/staff
between 2009 to the present.*

## Todo
- grab offices left out for faculty & staff
- find a way to include include gender split
- should I be using classes?