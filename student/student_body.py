import re


def set_format(children_data, student):
    for child_data in children_data:
        child_type = child_data["type"]
        data = child_data["data"]

        if child_type == "TitleValue":
            title = data["title"]

            if title == "Coeducational":
                if "Yes" in data["value"][0]:
                    coed = "Coed"
                elif "women only" in data["value"][0]:
                    coed = "Women Only"
                else:
                    coed = "Men only"

                student.update({
                    "coed": coed
                })
            elif title == "Full-Time Undergraduates":
                if "Not" not in data["value"][0]:
                    student.update({
                        "fulltime_undergrad_count": int(data["value"][0].replace(",", ""))
                    })
            elif title == "International Students":
                if "Not" not in data["value"][0]:
                    c, p = get_count_and_pct(data["value"][0])
                    student.update({
                        "intl_pct": p,
                        "intl_countries_count": c
                    })
            elif title == "Average Age":
                student.update({
                    "avg_age": int(round(float(data["value"][0])))
                })
            elif title == "All Graduate Students":
                if "Not" not in data["value"][0]:
                    student.update({
                        "grad_count": int(data["value"][0].replace(",", ""))
                    })

        elif child_type == "NestedTitleValue":
            top = data["topTitleValue"]
            title = top["title"]

            if title == "All Undergraduates":
                if "Not" in top["value"][0]:
                    student.update({
                        "undergrad_count": int(top["value"].replace(",", ""))
                    })

                for e in data["children"]:
                    c, p = get_count_and_pct(e["value"][0])
                    if e["title"] == "Women":
                        student.update({
                            "undergrad_w_count": c,
                            "undergrad_w_pct": p
                        })
                    else:
                        student.update({
                            "undergrad_m_count": c,
                            "undergrad_m_pct": p
                        })

        elif child_type == "BarGraph":
            if data["title"] == "Ethnicity of Students from U.S.":
                for e in data["data"]:
                    label = e["label"]

                    if label == "American Indian/Alaskan Native":
                        student.update({
                            "indian_pct": e["value"]
                        })
                    elif label == "Asian":
                        student.update({
                            "asian_pct": e["value"]
                        })
                    elif label == "Black/African-American":
                        student.update({
                            "black_pct": e["value"]
                        })
                    elif label == "Hispanic/Latino":
                        student.update({
                            "hispanic_pct": e["value"]
                        })
                    elif "Multi-race" in label:
                        student.update({
                            "mixed_pct": e["value"]
                        })
                    elif "Native Hawaiian" in label:
                        student.update({
                            "pi_pct": e["value"]
                        })
                    elif label == "White":
                        student.update({
                            "white_pct": e["value"]
                        })
                    else:
                        student.update({
                            "unknown_pct": e["value"]
                        })


def get_count_and_pct(string):
    count_pattern = r"[0-9,]+(?!\%)"
    if re.search(count_pattern, string) is not None:
        count = int(re.search(count_pattern, string).group().replace(",", ""))
    else:
        count = None

    pct_pattern = r"[0-9.]+(?=\%)"
    if re.search(pct_pattern, string) is not None:
        pct = float(re.search(pct_pattern, string).group())
    else:
        pct = None

    return count, pct

