from CollegeData import CollegeData
from rich.console import Console
from UsNews import UsNews
import file
import time
import json
import logging


try:
    start = time.time()

    deter = input('college_data/us_news/all?')

    if deter == 'college_data' or deter == 'all':
        college = CollegeData()
        schools = college.get_total_school_data()
        file.store(schools)

        with open('/mnt/c/Users/baicen/Desktop/schools.json', 'w') as outfile:
            json.dump(schools, outfile)
        with open('obj/schools.json', 'w') as outfile:
            json.dump(schools, outfile)

    if deter == 'us_news' or deter == 'all':
        us_news = UsNews()
        us_news.get_data()

    end = time.time()
    print("+++++++++++++ Total +++++++++++++")
    print(end - start)
    print("+++++++++++++++++++++++++++++++++")

except Exception as e:
    console = Console()
    console.print(repr(e), style="bold red")
    # print(repr(e))

