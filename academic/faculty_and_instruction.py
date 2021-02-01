def set_format(children_data, academic):
    for child_data in children_data:
        child_type = child_data["type"]
        data = child_data["data"]

        if child_type == "TitleValue":
            title = data["title"]

            if title == "Full-Time Faculty":
                if "Not" not in data["value"][0]:
                    academic.update({
                        "fulltime_faculty_count": int(data["value"][0].replace(",", ""))
                    })
            elif title == "Part-Time Faculty":
                if "Not" not in data["value"][0]:
                    academic.update({
                        "parttime_faculty_count": int(data["value"][0].replace(",", ""))
                    })
            elif "Ph.D./Terminal Degree" in title:
                if "Not" not in data["value"][0]:
                    academic.update({
                        "phd_faculty_pct": int(data["value"][0].replace("%", ""))
                    })
        elif child_type == "BarGraph":
            title = data["title"]

            if title == "Regular Class Size":
                for el in data["data"]:
                    if "2-9" in el["label"]:
                        academic.update({
                            "class_size_9_pct": el["value"]
                        })
                    elif "10-19" in el["label"]:
                        academic.update({
                            "class_size_19_pct": el["value"]
                        })
                    elif "20-29" in el["label"]:
                        academic.update({
                            "class_size_29_pct": el["value"]
                        })
                    elif "30-39" in el["label"]:
                        academic.update({
                            "class_size_39_pct": el["value"]
                        })
                    elif "40-49" in el["label"]:
                        academic.update({
                            "class_size_49_pct": el["value"]
                        })
                    elif "50-99" in el["label"]:
                        academic.update({
                            "class_size_99_pct": el["value"]
                        })
                    elif "100" in el["label"]:
                        academic.update({
                            "class_size_100_pct": el["value"]
                        })
            elif "Section/Lab" in title:
                for el in data["data"]:
                    if "2-9" in el["label"]:
                        academic.update({
                            "section_size_9_pct": el["value"]
                        })
                    elif "10-19" in el["label"]:
                        academic.update({
                            "section_size_19_pct": el["value"]
                        })
                    elif "20-29" in el["label"]:
                        academic.update({
                            "section_size_29_pct": el["value"]
                        })
                    elif "30-39" in el["label"]:
                        academic.update({
                            "section_size_39_pct": el["value"]
                        })
                    elif "40-49" in el["label"]:
                        academic.update({
                            "section_size_49_pct": el["value"]
                        })
                    elif "50-59" in el["label"]:
                        academic.update({
                            "section_size_99_pct": el["value"]
                        })
                    elif "100" in el["label"]:
                        academic.update({
                            "section_size_100_pct": el["value"]
                        })

