def set_format(children_data, academic):
    for child_data in children_data:
        child_type = child_data["type"]
        data = child_data["data"]

        if child_type == "TitleValue":
            title = data["title"]

            if title == "Library Available on Campus":
                academic.update({
                    "has_campus_library": 1 if "Yes" in data["value"][0] else 0
                })
            elif title == "Holdings":
                if "Not" not in data["value"][0]:
                    academic.update({
                        "library_holdings_count": int(data["value"][0].replace(",", ""))
                    })
            elif title == "Computers Available on Campus":
                if "Not" not in data["value"][0]:
                    academic.update({
                        "campus_computers_count": int(data["value"][0].replace(",", ""))
                    })
            elif title == "Internet/E-mail Access":
                academic.update({
                    "has_internet_access": 0 if "Not reported" == data["value"][0] else 1
                })
