def set_format(children_data, campus):
    for child_data in children_data:
        child_type = child_data["type"]
        data = child_data["data"]

        if child_type == "TitleValue":
            title = data["title"]

            if "24-Hour Emergency Phone" in title:
                campus.update({
                    "has_alarm_devices": 1 if "Available" in data["value"][0] else 0
                })
            elif title == "24-Hour Security Patrols":
                campus.update({
                    "has_security": 1 if "Available" in data["value"][0] else 0
                })
            elif "Late-Night Transport" in title:
                campus.update({
                    "has_escort": 1 if "Available" in data["value"][0] else 0
                })
            elif "Electronically Operated" in title:
                campus.update({
                    "has_e_entrance": 1 if "Available" in data["value"][0] else 0
                })
            elif title == "Other":
                campus.update({
                    "other_security_resources": data["value"][0]
                })
