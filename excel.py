import numpy as np
import pandas as pd
import file
import json


def set_pkl_to_excel(name=None):
    name = name if name is not None else "schools"
    schools = file.read(name)

    overview = set_school_content(schools, "overview")
    admissions = set_school_content(schools, "admissions")
    moneys = set_school_content(schools, "moneys")
    academics = set_school_content(schools, "academics")
    campus = set_school_content(schools, "campus")
    students = set_school_content(schools, "students")

    overview_df = pd.DataFrame(overview).T
    admissions_df = pd.DataFrame(admissions).T
    moneys_df = pd.DataFrame(moneys).T
    academics_df = pd.DataFrame(academics).T
    campus_df = pd.DataFrame(campus).T
    students_df = pd.DataFrame(students).T

    overview_df.to_excel(f"obj/{name}_overview.xlsx", sheet_name="Sheet1")
    admissions_df.to_excel(f"obj/{name}_admissions.xlsx", sheet_name="Sheet1")
    moneys_df.to_excel(f"obj/{name}_moneys.xlsx", sheet_name="Sheet1")
    academics_df.to_excel(f"obj/{name}_academics.xlsx", sheet_name="Sheet1")
    campus_df.to_excel(f"obj/{name}_campus.xlsx", sheet_name="Sheet1")
    students_df.to_excel(f"obj/{name}_students.xlsx", sheet_name="Sheet1")


def set_school_content(schools, target):
    return {k: v[target] for k, v in schools.items()}


def set_excel_to_pkl(name=None):
    name = name if name is not None else "schools"

    en_df = pd.read_excel(f"obj/{name}.xlsx", sheet_name="en")
    cn_df = pd.read_excel(f"obj/{name}.xlsx", sheet_name="cn")
    tw_df = pd.read_excel(f"obj/{name}.xlsx", sheet_name="tw")

    en_df.set_index('slug_en', inplace=True)
    cn_df.set_index('slug_cn', inplace=True)
    tw_df.set_index('slug_tw', inplace=True)

    en = en_df.to_dict(orient="index")
    cn = cn_df.to_dict(orient="index")
    tw = tw_df.to_dict(orient="index")

    schools = file.read()
    for k, v in en.items():
        schools[k].update({
            "overview": {
                "name": json.dumps({
                    "en": v["name"],
                    "cn": cn[k]["name"],
                    "tw": tw[k]["name"]
                }),
                "overview": json.dumps({
                    "en": "" if pd.isnull(v["overview"]) else en[k]["overview"],
                    "cn": "" if pd.isnull(v["overview"]) else cn[k]["overview"],
                    "tw": "" if pd.isnull(v["overview"]) else tw[k]["overview"]
                }),
                "website": v["website"]
            }
        })

    file.store(schools, "trans-schools")


set_excel_to_pkl("schools_overview")
