def set_format(children_data, academic):
    for child_data in children_data:
        child_type = child_data["type"]
        data = child_data["data"]

        if child_type == "TitleValue":
            title = data["title"]

            if "General Education" in title:
                academic.update({
                    "has_gened": 0 if "Not required for" in data["value"][0] else 1
                })
            elif title == "Computer":
                academic.update({
                    "has_comp_req": 0 if "Students not required" in data["value"][0] else 1
                })
            elif title == "Foreign Language":
                academic.update({
                    "has_lang_req": 0 if "Not required" in data["value"][0] else 1
                })
            elif title == "Math/Science":
                academic.update({
                    "has_stem_req": 0 if "Not required" in data["value"][0] else 1
                })
