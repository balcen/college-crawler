from dateutil.parser import parser
from datetime import datetime


def set_format(freshman_datas, admission):
    for freshman_data in freshman_datas:
        data_type = freshman_data["type"]
        data = freshman_data["data"]

        if data_type == "TitleValue":
            if "High School" in data["title"]:
                value = data["value"][0]
                key = "hs_diploma_policy" if "Graduation" in data["title"] else "hs_program_policy"

                admission.update({
                    key: value
                })
        elif data_type == "LabeledTable":
            if "Req" in data["valueTitles"]:
                for subject in data["data"]:
                    label = subject["label"]

                    if label == "English":
                        key1, key2 = convert_high_school_unit("english")
                    elif label == "Mathematics":
                        key1, key2 = convert_high_school_unit("math")
                    elif label == "Science":
                        key1, key2 = convert_high_school_unit("science")
                    elif label == "Foreign Language":
                        key1, key2 = convert_high_school_unit("language")
                    elif label == "Social Studies":
                        key1, key2 = convert_high_school_unit("social")
                    elif label == "History":
                        key1, key2 = convert_high_school_unit("history")
                    elif label == "Academic Electives":
                        key1, key2 = convert_high_school_unit("elective")
                    else:
                        key1 = key2 = None
                    
                    admission.update({
                        key1: int(subject["values"][0] or 0),
                        key2: int(subject["values"][1] or 0)
                    })
            else:
                for subject in data["data"]:
                    label = subject["label"]

                    if label == "SAT or ACT":
                        admission.update({
                            "satact_policy": subject["values"][0],
                            "satact_scores_due": convert_date(subject["values"][1])
                        })
                    elif label == "SAT Only":
                        admission.update({
                            "sat_policy": subject["values"][0],
                            "sat_scores_due": convert_date(subject["values"][1])
                        })
                    elif label == "ACT Only":
                        admission.update({
                            "act_policy": subject["values"][0],
                            "act_scores_due": convert_date(subject["values"][1])
                        })
                    elif label == "SAT and SAT Subject Tests, or ACT":
                        admission.update({
                            "satsat2act_policy": subject["values"][0]
                        })
                    elif label == "SAT Subject Tests Only":
                        admission.update({
                            "sat2_policy": subject["values"][0]
                        })
                    elif label == "SAT Essay Component Policy":
                        admission.update({
                            "sat_essay_policy": subject["values"][0]
                        })
                    elif label == "ACT Writing Test Policy":
                        admission.update({
                            "act_essay_policy": subject["values"][0]
                        })
                    else:
                        admission.update({
                            "essay_policy": subject["values"][0]
                        })


def convert_high_school_unit(string):
    pattern_first = f"hs_{string}_required"
    pattern_last = f"hs_{string}_recommended"

    return pattern_first, pattern_last


def convert_date(date_str):
    try:
        p = parser()
        date = p.parse(date_str, default=datetime(1970, 1, 1, 0, 0))
        return datetime.strftime(date, "%Y-%m-%d")
    except ValueError:
        return None
