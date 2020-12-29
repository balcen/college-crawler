def set_format(children_data, academic):
    for child_data in children_data:
        child_type = child_data["type"]
        data = child_data["data"]

        if child_type == "TitleValue":
            title = data["title"]

            if title == "Remedial Instruction":
                academic.update({
                    "has_remedial_instruction": 0 if "No" in data["value"][0] else 1
                })
            elif title == "Tutoring":
                academic.update({
                    "has_tutoring": 1 if "Available" in data["value"][0] else 0
                })
            elif title == "Services for Learning Disabled Students":
                academic.update({
                    "has_disability_service": 1 if "Available" in data["value"][0] else 0
                })
            elif title == "Service for Physically Disabled Students":
                academic.update({
                    "disability_services": data["value"][0]
                })
