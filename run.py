from connect import *
from CollegeData import CollegeData
from database import *
import time

try:
    start = time.time()

    college = CollegeData()
    schools = college.get_total_school_data()

    init("schools")
    init("admissions")

    for slug, school in schools.items():
        school_id = insert("schools", school["overview"])
        school["admissions"].update({
            "school_id": school_id
        })
        admissions = {k: v for k, v in school["admissions"].items() if k and k.strip()}
        insert("admissions", admissions)

    end = time.time()
    print("+++++++++++++ Total +++++++++++++")
    print(end - start)
    print("+++++++++++++++++++++++++++++++++")
finally:
    connection.close()
