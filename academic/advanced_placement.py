def set_format(children_data, academic):
    for child_data in children_data:
        child_type = child_data["type"]
        data = child_data["data"]

        if child_type == "TitleValue":
            title = data["title"]

            if title == "International Baccalaureate":
                academic.update({
                    "accepts_ib": 1 if "Accepted" in data["value"][0] else 0
                })
            elif "Advanced Placement" in title:
                academic.update({
                    "accepts_ap": 1 if "Accepted" in data["value"][0] else 0
                })
            elif title == "Sophomore Standing":
                academic.update({
                    "has_sophomore_standing": 1 if "Available" in data["value"][0] else 0
                })
