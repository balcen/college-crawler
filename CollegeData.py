from bs4 import BeautifulSoup
from admission import *
from money import *
from academic import *
from campus import *
from student import *
import requests
import json
import time
import pickle


def get_build_id():
    link = "https://www.collegedata.com/college-search"
    res = requests.get(link)
    soup = BeautifulSoup(res.text, "lxml")
    return json.loads(soup.find("script", id="__NEXT_DATA__").contents[0])["buildId"]


def get_total_school_nums():
    link = "https://www.collegedata.com/api/schools?pageNum=0&pageSize=0&sortOption=name&name="
    res = requests.get(link)
    return json.loads(res.text)["total"]


def get_total_school_slugs(school_nums):
    link = f"https://www.collegedata.com/api/schools?pageNum=0&pageSize={school_nums}&sortOption=name&name="
    res = requests.get(link)
    total_schools = json.loads(res.text)["results"]
    return [x["slug"] for x in total_schools]


def find_specific_function(title):
    if "Freshman" in title:
        return freshman_admission_reqs.set_format()
    elif "Applying" in title:
        return applying_for_admission()
    elif "Selection" in title:
        return selection_of_student
    else:
        return profile_of_fall_admission


class CollegeData:
    def __init__(self):
        self.build_id = get_build_id()
        school_nums = get_total_school_nums()
        self.slugs = get_total_school_slugs(school_nums)

    def get_total_school_data(self):
        school = dict()
        num = 1
        start = time.time()

        for slug in self.slugs:
            overview, admission, campus, money, academic, student = dict(), dict(), dict(), dict(), dict(), dict()
            num += 1
            print(slug)
            self.__set_overview(slug, overview, admission)
            self.__set_admission(slug, admission)
            self.__set_money(slug, money)
            self.__set_academic(slug, academic)
            self.__set_campus(slug, campus)
            self.__set_student(slug, student)
            school.update({
                slug: {
                    "overview": overview,
                    "admissions": admission,
                    "moneys": money,
                    "academics": academic,
                    "campus": campus,
                    "students": student
                }
            })

        end = time.time()

        print("++++++++ College Data Total ++++++++")
        print(end - start)
        print("++++++++++++++++++++++++++++++++++++")

        return school

    def __set_overview(self, slug, overview, admission):
        link = f"https://www.collegedata.com/_next/data/{self.build_id}/college-search/{slug}.json"
        res = requests.get(link)
        profile = json.loads(res.text)["pageProps"]["profile"]
        entrance_difficulty = profile["bodyContent"][0]["data"]["children"][0]["data"]["value"][0]

        overview.update({
            "name": profile["name"],
            "website": profile["website"],
            "overview": profile["description"]
        })

        admission.update({
            "entrance_difficulty": entrance_difficulty
        })

    def __set_admission(self, slug, admission):
        link = f"https://www.collegedata.com/_next/data/{self.build_id}/college-search/{slug}/admission.json"
        print("---- Admission -----")
        print(link)
        res = requests.get(link)
        profile = json.loads(res.text)["pageProps"]["profile"]

        for el in profile["bodyContent"]:
            data = el["data"]
            title = data["title"]

            if "Freshman" in title:
                freshman_admission_reqs.set_format(data["children"], admission)
            elif "Applying" in title:
                applying_for_admission.set_format(data["children"], admission)
            elif "Selection" in title:
                selection_of_student.set_format(data["children"], admission)
            else:
                profile_of_fall_admission.set_format(data["children"], admission)

    def __set_money(self, slug, money):
        link = f"https://www.collegedata.com/_next/data/{self.build_id}/college-search/{slug}/money-matters.json"
        print("---- Financial ----")
        print(link)
        res = requests.get(link)
        profile = json.loads(res.text)["pageProps"]["profile"]

        tuition_and_expenses.set_format(profile, money)

        for content in profile["bodyContent"]:
            data = content["data"]
            title = data["title"]

            if "Applying" in title:
                applying_for_financial_aid.set_format(data["children"], money)
            elif "Profile" in title:
                profile_of_financial_aid.set_format(data["children"], money)
            elif "Financial" in title:
                financial_aid_programs.set_format(data["children"], money)

    def __set_academic(self, slug, academic):
        link = f"https://www.collegedata.com/_next/data/{self.build_id}/college-search/{slug}/academics.json"
        print("---- Academic ----")
        print(link)
        res = requests.get(link)
        profile = json.loads(res.text)["pageProps"]["profile"]

        general_information.set_format(profile, academic)

        for content in profile["bodyContent"]:
            data = content["data"]
            title = data["title"]

            if "Undergraduate" in title:
                undergraduate_education.set_format(data["children"], academic)
            elif "Curriculum" in title:
                curriculum_and_graduation_requirements.set_format(data["children"], academic)
            elif "Faculty" in title:
                faculty_and_instruction.set_format(data["children"], academic)
            elif "Advanced" in title:
                advanced_placement.set_format(data["children"], academic)
            elif "Academic Resources" in title:
                academic_resources.set_format(data["children"], academic)
            elif "Academic Support Services" in title:
                academic_support_services.set_format(data["children"], academic)
            elif "Graduate/Professional" in title:
                school_education.set_format(data["children"], academic)

    def __set_campus(self, slug, campus):
        link = f"https://www.collegedata.com/_next/data/{self.build_id}/college-search/{slug}/campus-life.json"
        print("---- Campus ----")
        print(link)
        res = requests.get(link)
        profile = json.loads(res.text)["pageProps"]["profile"]

        for content in profile["bodyContent"]:
            data = content["data"]
            title = data["title"]

            if title == "Location and Setting":
                location_and_setting.set_format(data["children"], campus)
            elif title == "Housing":
                housing.set_format(data["children"], campus)
            elif title == "Security":
                security.set_format(data["children"], campus)
            elif title == "Personal Support Services":
                personal_support_services.set_format(data["children"], campus)
            elif title == "Sports & Recreation":
                sports_and_recreation.set_format(data["children"], campus)

    def __set_student(self, slug, student):
        link = f"https://www.collegedata.com/_next/data/{self.build_id}/college-search/{slug}/students.json"
        print("---- Student ----")
        print(link)
        res = requests.get(link)
        profile = json.loads(res.text)["pageProps"]["profile"]

        for content in profile["bodyContent"]:
            data = content["data"]
            title = data["title"]

            if title == "Student Body":
                student_body.set_format(data["children"], student)
            elif "Undergraduate Retention" in title:
                undergraduate_retention_and_graduation.set_format(data["children"], student)
            elif "After Graduation":
                after_graduation.set_format(data["children"], student)
