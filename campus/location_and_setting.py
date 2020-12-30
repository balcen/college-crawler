import re


def set_format(children_data, campus):
    for child_data in children_data:
        child_type = child_data["type"]
        data = child_data["data"]

        if child_type == "TitleValue":
            title = data["title"]

            if "Population" in title:
                if "Not" not in data["value"][0]:
                    pattern = r"[0-9]+"
                    campus.update({
                        "city_population": int(re.search(pattern, data["value"][0]).group().replace(",", ""))
                    })
            elif title == "Nearest Metropolitan Area":
                campus.update({
                    "nearest_metro": data["value"][0]
                })
            elif title == "Campus Size":
                if "Not" not in data["value"][0]:
                    pattern = r"[0-9,]+"
                    campus.update({
                        "campus_size_acre": int(re.search(pattern, data["value"][0]).group().replace(",", ""))
                    })
            elif title == "Avg Low In Jan":
                if "Not" not in data["value"][0]:
                    campus.update({
                        "temp_low": float(data["value"][0][:-1])
                    })
            elif title == "Avg Hgigh In Sep":
                if "Not" not in data["value"][0]:
                    campus.update({
                        "temp_high": float(data["value"][0][:-1])
                    })
            elif title == "Rainy Days / Year":
                if "Not" not in data["value"][0]:
                    pattern = r"[0-9]+"
                    campus.update({
                        "rain_days": int(re.search(pattern, data["value"][0]).group())
                    })
            elif title == "Nearest Bus Station":
                if "Not" not in data["value"][0]:
                    campus.update({
                        "nearest_bus_dist_mi": get_miles(data["value"][0])
                    })
            elif title == "Nearest Tran Station":
                if "Not" not in data["value"][0]:
                    campus.update({
                        "nearest_tran_dist_mi": get_miles(data["value"][0])
                    })

        elif child_type == "TitleLink":
            title = data["title"]

            if title == "Campus Map":
                campus.update({
                    "map_url": data["link"]
                })


def get_miles(string):
    pattern = r"[0-9]+(?=\smile)"
    if re.search(pattern, string) is not None:
        return int(re.search(pattern, string).group())
    return None
