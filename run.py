from CollegeData import CollegeData
from database import *
from tqdm import tqdm
import file
import time
import translation
from rich.console import Console


def init_db(args=None):
    if args is None:
        init("schools")
        init("admissions")
        init("academics")
        init("campus")
        init("moneys")
        init("students")
    else:
        for arg in args:
            init(arg)


def init_data(school_id, data):
    inited_data = {k: v for k, v in data.items() if k and k.strip()}
    inited_data.update({"school_id": school_id})
    return inited_data


def insert_data(data, args=None):
    init_db(args)

    with tqdm(total=len(data)) as bar:
        for slug, school in data.items():
            school_id = insert("schools", school["overview"])

            init_data(school_id, school)

            if args is None:
                insert("admissions", init_data(school_id, school["admissions"]))
                insert("academics", init_data(school_id, school["academics"]))
                insert("campus", init_data(school_id, school["campus"]))
                insert("moneys", init_data(school_id, school["moneys"]))
                insert("students", init_data(school_id, school["students"]))
            else:
                for arg in args:
                    insert(arg, init_data(school_id, school[arg]))

            bar.update(1)


try:
    print("crawler/load/insert")
    input_string = input()

    start = time.time()

    if "crawler" in input_string:
        college = CollegeData()
        schools = college.get_total_school_data()
        file.store(schools)
    else:
        schools = file.read("trans-schools")

    if "insert" in input_string:
        tables = ["admissions", "academics", "campus", "moneys", "students"]
        if any(v in input_string for v in tables):
            selected = [v in input_string for v in tables]
            insert_data(schools, tables)
        else:
            insert_data(schools)
    else:
        print(schools[0])

    end = time.time()
    print("+++++++++++++ Total +++++++++++++")
    print(end - start)
    print("+++++++++++++++++++++++++++++++++")
except Exception as e:
    console = Console()
    console.print(repr(e), style="bold red")
finally:
    connection.close()

