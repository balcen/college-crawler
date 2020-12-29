import re


def set_format(children_data, campus):
    for child_data in children_data:
        child_type = child_data["type"]
        data = child_data["data"]

        if child_type == "TitleValue":
            title = data["title"]

            if title == "College Housing":
                campus.update({
                    "has_housing": 1 if "College offers" in data["value"][0] else 0
                })
            elif title == "Types of Housing":
                campus.update({
                    "housing_type": data["value"][0]
                })
            elif title == "Students in College Housing":
                if "Not" not in data["value"][0]:
                    campus.update({
                        "housing_pct": get_percentage(data["value"][0])
                    })
            elif title == "Housing Requirements":
                campus.update({
                    "housing_requirement": data["value"][0]
                })
            elif title == "Freshman Housing Guarantee":
                campus.update({
                    "housing_guarantee": data["value"][0]
                })
            elif "Students Living Off Campus" in title:
                if "Not" not in data["value"][0]:
                    campus.update({
                        "offcampus_pct": get_percentage(data["value"][0])
                    })
            elif title == "Off-Campus Housing Assistance":
                campus.update({
                    "offcampus_assistance": data["value"][0]
                })

def get_percentage(string):
    pattern = r"[0-9]+(?=\%)"
    if re.search(pattern, string) is not None:
        return int(re.search(pattern, string).group())
    else:
        return None
