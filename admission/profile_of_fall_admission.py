import re


def set_format(fall_datas, admission):
    for fall_data in fall_datas:
        data_type = fall_data["type"]
        data = fall_data["data"]
        title = data.get("title", None)

        if data_type == "NestedTitleValue":
            top_title = data["topTitleValue"]
            title = top_title["title"]

            if title == "Overall Admission Rate":
                percentage, num, pre_num = get_per_and_num_and_pre_num(top_title["value"][0])

                admission.update({
                    "acceptance_pct_overall": percentage,
                    "applicant_overall_count": num
                })

                for child in data["children"]:
                    if child["title"] == "Women":
                        p, n, pn = get_per_and_num_and_pre_num(child["value"][0])

                        admission.update({
                            "acceptance_pct_w": p,
                            "applicant_w_count": n
                        })
                    elif child["title"] == "Men":
                        p, n, pn = get_per_and_num_and_pre_num(child["value"][0])

                        admission.update({
                            "acceptance_pct_m": p,
                            "applicant_m_count": n
                        })
            elif title == "Students Enrolled":
                sp, sn, spn = get_per_and_num_and_pre_num(top_title["value"][0])

                admission.update({
                    "yield_pct_overall": sp,
                    "admitted_overall_count": sn,
                    "enrolled_overall_count": spn
                })

                for child in data["children"]:
                    if child["title"] == "Women":
                        p, n, pn = get_per_and_num_and_pre_num(child["value"][0])

                        admission.update({
                            "enrolled_w_count": pn,
                            "yield_pct_w": p,
                            "admitted_w_count": n
                        })
                    elif child["title"] == "Men":
                        p, n, pn = get_per_and_num_and_pre_num(child["value"][0])

                        admission.update({
                            "enrolled_m_count": pn,
                            "yield_pct_m": p,
                            "admitted_m_count": n
                        })
        elif title == "Students Offered Wait List":
            admission.update({
                "waitlist_offered_count": int(data["value"][0].replace(",", ""))
            })
        elif title == "Students Accepting Wait List Position":
            admission.update({
                "waitlist_accepted_count": int(data["value"][0].replace(",", ""))
            })
        elif title == "Students Admitted From Wait List":
            admission.update({
                "waitlist_admitted_count": int(data["value"][0].replace(",", ""))
            })
        elif data_type == "BarGraph":
            if title == "":
                for grade in data["data"]:
                    if grade["label"] == "3.75 and Above":
                        admission.update({
                            "gpa375_pct": grade["value"]
                        })
                    elif grade["label"] == "3.50 - 3.74":
                        admission.update({
                            "gpa350_pct": grade["value"]
                        })
                    elif grade["label"] == "3.25 - 3.49":
                        admission.update({
                            "gpa325_pct": grade["value"]
                        })
                    elif grade["label"] == "3.00 - 3.24":
                        admission.update({
                            "gpa300_pct": grade["value"]
                        })
                    elif grade["label"] == "2.50 - 2.99":
                        admission.update({
                            "gpa250_pct": grade["value"]
                        })
                    elif grade["label"] == "2.00 - 2.49":
                        admission.update({
                            "gpa200_pct": grade["value"]
                        })
            elif "SAT Math" in title:
                a, n, x = get_average_and_range(title)

                admission.update({
                    "avg_sat_math": a,
                    "avg_sat_math_min": n,
                    "avg_sat_math_max": x
                })

                for level in data["data"]:
                    label = level["label"]

                    if "700 - 800" in label:
                        admission.update({
                            "sat_math700_pct": level["value"]
                        })
                    elif "600 - 700" in label:
                        admission.update({
                            "sat_math600_pct": level["value"]
                        })
                    elif "500 - 600" in label:
                        admission.update({
                            "sat_math500_pct": level["value"]
                        })
                    elif "400 - 500" in label:
                        admission.update({
                            "sat_math400_pct": level["value"]
                        })
                    elif "300 - 400" in label:
                        admission.update({
                            "sat_math300_pct": level["value"]
                        })
                    elif "200 - 300" in label:
                        admission.update({
                            "sat_math200_pct": level["value"]
                        })
            elif "SAT EBRW" in title:
                a, n, x = get_average_and_range(title)

                admission.update({
                    "avg_sat_e": a,
                    "avg_sat_english_min": n,
                    "avg_sat_english_max": x
                })

                for level in data["data"]:
                    label = level["label"]

                    if "700 - 800" in label:
                        admission.update({
                            "sat_english700_pct": level["value"]
                        })
                    elif "600 - 700" in label:
                        admission.update({
                            "sat_english600_pct": level["value"]
                        })
                    elif "500 - 600" in label:
                        admission.update({
                            "sat_english500_pct": level["value"]
                        })
                    elif "400 - 500" in label:
                        admission.update({
                            "sat_english400_pct": level["value"]
                        })
                    elif "300 - 400" in label:
                        admission.update({
                            "sat_english300_pct": level["value"]
                        })
                    elif "200 - 300" in label:
                        admission.update({
                            "sat_english200_pct": level["value"]
                        })
            else:
                a, n, x = get_average_and_range(title)

                admission.update({
                    "avg_act": a,
                    "avg_act_min": n,
                    "avg_act_max": x
                })

                for level in data["data"]:
                    label = level["label"]

                    if "36" in label:
                        admission.update({
                            "avg_act30_pct": level["value"]
                        })
                    elif "29" in label:
                        admission.update({
                            "avg_act24_pct": level["value"]
                        })
                    elif "23" in label:
                        admission.update({
                            "avg_act18_pct": level["value"]
                        })
                    elif "17" in label:
                        admission.update({
                            "avg_act12_pct": level["value"]
                        })
                    elif "11" in label:
                        admission.update({
                            "avg_act6_pct": level["value"]
                        })
                    else:
                        admission.update({
                            "avg_act0_pct": level["value"]
                        })
        elif title == "High School Class Rank":
            for level in data["value"]:
                pct_pattern = r"[0-9]+(?=\%)"
                if re.search(pct_pattern, level) is not None:
                    pct = int(re.search(pct_pattern, level).group())
                else:
                    pct = None

                if "tenth" in level:
                    admission.update({
                        "hs_rank_10_pct": pct
                    })
                elif "quarter" in level:
                    admission.update({
                        "hs_rank_25_pct": pct
                    })
                else:
                    admission.update({
                        "hs_rank_50_pct": pct
                    })
        elif title == "National Merit Scholar":
            admission.update({
                "national_merit_pct": get_percent_in_no_reported(data["value"][0])
            })
        elif title == "Valedictorian":
            admission.update({
                "valedictorian_pct": get_percent_in_no_reported(data["value"][0])
            })
        elif title == "Class President":
            admission.update({
                "class_president_pct": get_percent_in_no_reported(data["value"][0])
            })
        elif title == "Student Government Officer":
            admission.update({
                "student_gov_pct": get_percent_in_no_reported(data["value"][0])
            })


def get_per_and_num_and_pre_num(string):
    string = string.replace(" ", "").replace(",", "")
    per_pattern = r"[0-9]+(?=\%)"
    if re.search(per_pattern, string) is not None:
        percentage = int(re.search(per_pattern, string).group())
    else:
        percentage = None

    num_pattern = r"(?<=of)[0-9]+"
    if re.search(num_pattern, string) is not None:
        num = int(re.search(num_pattern, string).group().replace(',', ''))
    else:
        num = None

    pre_num_pattern = r"[0-9,]+(?=\([0-9]+%\))"
    if re.search(pre_num_pattern, string) is not None:
        pre_num = int(re.search(pre_num_pattern, string).group().replace(',', ''))
    else:
        pre_num = None

    return percentage, num, pre_num


def get_average_and_range(string):
    avg_pattern = r"[0-9]+(?=\saverage)"
    if re.search(avg_pattern, string) is not None:
        avg = int(re.search(avg_pattern, string).group())
    else:
        avg = None

    range_pattern = r"[0-9]{3}\-[0-9]{3}"
    if re.search(range_pattern, string) is not None:
        rang = re.search(range_pattern, string).group().split("-")
        mini = int(rang[0])
        maxi = int(rang[1])
    else:
        mini = None
        maxi = None
    
    return avg, mini, maxi


def get_percent_in_no_reported(string):
    pattern = r"[0-9]{1,3}(?=\%)"
    if re.search(pattern, string) is not None:
        return re.search(pattern, string).group()
    else:
        return 0
