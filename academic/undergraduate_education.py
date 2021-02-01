def set_format(children_data, academic):
    for child_data in children_data:
        child_type = child_data["type"]
        data = child_data["data"]

        if child_type == "TitleValue":
            title = data["title"]

            if title == "Most Popular Disciplines":
                academic.update({
                    "popular_majors": ", ".join(data["value"])
                })
            elif "Combined Liberal" in title:
                academic.update({
                    "la_pd_programs": data["value"][0]
                })
            elif title == "Special Programs":
                academic.update({
                    "special_programs": ", ".join(data["value"])
                })
            elif title == "Study Abroad":
                academic.update({
                    "has_study_abroad": 1 if "Offered" in data["value"][0] else 0
                })
            elif title == "Online Degrees":
                academic.update({
                    "has_online_degree": 0 if "No" in data["value"][0] else 1
                })
