def set_format(children_data, student):
    for child_data in children_data:
        child_type = child_data["type"]
        data = child_data["data"]

        if child_type == "TitleValue":
            title = data["title"]

            if title == "First-Year Students Returning":
                if "Not" not in data["value"][0] and data["value"][0]:
                    student.update({
                        "return_rate": float(data["value"][0].replace("%", ""))
                    })
            elif title == "Students Graduating Within 4 Years":
                if "Not" not in data["value"][0]:
                    student.update({
                        "graduate_4_yrs": float(data["value"][0].replace("%", ""))
                    })
            elif title == "Students Graduating Within 5 Years":
                if "Not" not in data["value"][0]:
                    student.update({
                        "graduate_5_yrs": float(data["value"][0].replace("%", ""))
                    })
            elif title == "Students Graduating Within 6 Years":
                if "Not" not in data["value"][0]:
                    student.update({
                        "graduate_6_yrs": float(data["value"][0].replace("%", ""))
                    })
