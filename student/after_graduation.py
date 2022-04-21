def set_format(children_data, student):
    for child_data in children_data:
        child_type = child_data["type"]
        data = child_data["data"]

        if child_type == "TitleValue":
            title = data["title"]

            if title == "Graduates Offered Full-Time Employment Within 6 Months":
                if "Not" not in data["value"][0]:
                    student.update({
                        "employment_pct": int(data["value"][0].replace("%", ""))
                    })
            elif title == "Graduates Pursuing Advanced Study Directly":
                if "Not" not in data["value"][0]:
                    student.update({
                        "pursue_grad_studies_pct": float(data["value"][0].replace(",", "").replace("%", ""))
                    })
            elif title == "Disciplines Pursued":
                if "Not" not in data["value"][0]:
                    student.update({
                        "grad_disciplines_pursued": data["value"][0]
                    })
