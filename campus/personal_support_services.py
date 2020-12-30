def set_format(children_data, campus):
    for child_data in children_data:
        child_type = child_data["type"]
        data = child_data["data"]

        if child_type == "TitleValue":
            title = data["title"]

            if title == "Health Service":
                campus.update({
                    "has_health_serv": 1 if "Offered" in data["value"][0] else 0
                })
            elif title == "Personal Counseling":
                campus.update({
                    "has_counseling": 1 if "Offered" in data["value"][0] else 0
                })
            elif title == "Child Care":
                campus.update({
                    "has_childcare": 1 if "Offered" in data["value"][0] else 0
                })
