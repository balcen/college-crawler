def set_format(profile_data, academic):
    head_content = profile_data["headerCardContent"]

    for content in head_content:
        content_type = content["type"]
        data = content["data"]

        if content_type == "TitleValue":
            title = data["title"]

            if title == "Academic Calendar System":
                academic.update({
                    "calendar_system": data["value"][0]
                })
            elif title == "Summer Session":
                academic.update({
                    "has_summer_session": 1 if "Offered" in data["value"][0] else 0
                })
        elif content_type == "TitleLink":
            title = data["title"]

            if "Catalogue" in title:
                academic.update({
                    "catalog_type": data["text"]
                })
