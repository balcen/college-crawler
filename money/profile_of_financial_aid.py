import re


def set_format(profile_data, money):
    for datum in profile_data:
        profile_type = datum["type"]
        data = datum["data"]

        toggle = "freshman"
        if data.get("value", "") == "All Undergraduates":
            toggle = "undergraduates"

        if profile_type == "TitleValue":
            title = data["title"]

            if title == "Financial Aid Applicants":
                count, per = get_count_per_by_string(data["value"][0])
                if toggle == "freshman":
                    money.update({
                        "finaid_freshmen_applicant_count": count,
                        "finaid_freshmen_applicant_pct": per
                    })
                else:
                    money.update({
                        "finaid_undergrad_applicant_count": count,
                        "finaid_undergrad_applicant_pct": per
                    })
            elif title == "Found to Have Financial Need":
                count, per = get_count_per_by_string(data["value"][0])
                if toggle == "freshman":
                    money.update({
                        "finaid_freshmen_needed_count": count,
                        "finaid_freshmen_needed_pct":per
                    })
                else:
                    money.update({
                        "finaid_undergrad_needed_count": count,
                        "finaid_undergrad_needed_pct": per
                    })
            elif title == "Received Financial Aid":
                count, per = get_count_per_by_string(data["value"][0])
                if toggle == "freshman":
                    money.update({
                        "finaid_freshmen_received_count": count,
                        "finaid_freshmen_received_pct": per
                    })
                else:
                    money.update({
                        "finaid_undergrad_received_count": count,
                        "finaid_undergrad_received_pct": per
                    })
            elif title == "Need Fully Met":
                count, per = get_count_per_by_string(data["value"][0])
                if toggle == "freshman":
                    money.update({
                        "finaid_freshmen_fully_met_count": count,
                        "finaid_freshmen_fully_met_pct": per
                    })
                else:
                    money.update({
                        "finaid_undergrad_fully_met_count": count,
                        "finaid_undergrad_fully_met_pct": per
                    })
            elif title == "Average Percent of Need Met":
                count, per = get_count_per_by_string(data["value"][0])
                if toggle == "freshman":
                    money.update({
                        "finaid_freshmen_avg_pct_met": per
                    })
                else:
                    money.update({
                        "finaid_undergrad_avg_pct_met": per
                    })
            elif "Graduates Who Took Out Loans" in title:
                if "Not" not in data["value"][0]:
                    money.update({
                        "student_loans_pct": int(data["value"][0].split("%", 1)[0])
                    })
            elif title == "Merit-Based Gift":
                string = data["value"][1]
                count_pattern = r"(?<!\$)[0-9]+"
                if re.search(count_pattern, string) is not None:
                    count = int(re.search(count_pattern, string).group())
                    money.update({
                        "finaid_freshman_merit_received_count": count,
                    })

                percentage_pattern = r"[0-9.]+(?=\%)"
                if re.search(percentage_pattern, string) is not None:
                    percentage = float(re.search(percentage_pattern, string).group())
                    money.update({
                        "finaid_freshman_merit_received_pct": percentage,
                    })

                price_pattern = r"(?<=\$)[0-9,]+"
                if re.search(price_pattern, string) is not None:
                    price = int(re.search(price_pattern, string).group().replace(",", ""))
                    money.update({
                        "finaid_freshman_merit_received_avg": price,
                    })
        elif profile_type == "NestedTitleValue":
            top_title_value = data["topTitleValue"]
            if top_title_value["title"] == "Average Award":
                if "$" in top_title_value["value"][0]:
                    if toggle == "freshman":
                        money.update({
                            "finaid_freshmen_avg_award": int(top_title_value["value"][0].replace(",", "").replace("$", ""))
                        })
                    else:
                        money.update({
                            "finaid_undergrad_avg_award": int(
                                top_title_value["value"][0].replace(",", "").replace("$", ""))
                        })
            #
            #     print(next((item for item in data["children"] if item["title"] == "Merit-Based Gift"), None))
            #     if next((item for item in data["children"] if item["title"] == "Merit-Based Gift"), None) is not None:
            #         el = next(item for item in data["children"] if item["title"])
            #         try:
            #             string = el["value"][1]
            #             count_pattern = r"(?<!\$)[0-9]+"
            #             count = int(re.search(count_pattern, string).group())
            #             percentage_pattern = r"[0-9.]+(?=\%)"
            #             percentage = float(re.search(percentage_pattern, string).group())
            #             price_pattern = r"(?<=\$)[0-9,]+"
            #             price = int(re.search(price_pattern, string).group().replace(",", ""))
            #
            #             money.update({
            #                 "finaid_freshman_merit_received_count": count,
            #                 "finaid_freshman_merit_received_pct": percentage,
            #                 "finaid_freshman_merit_received_avg": price
            #             })
            #         except IndexError:
            #             pass
            elif "Average Indebtedness of" in top_title_value["title"]:
                if "$" in top_title_value["value"][0]:
                    money.update({
                        "student_indebtedness": int(top_title_value["value"][0].replace(",", "").replace("$", ""))
                    })


def get_count_per_by_string(string):
    count_pattern = r"[0-9]+(?![.\%])"
    if re.search(count_pattern, string) is not None:
        count = int(re.search(count_pattern, string).group())
    else:
        count = None

    percentage_pattern = r"[0-9.]+(?=\%)"
    if re.search(percentage_pattern, string) is not None:
        percentage = float(re.search(percentage_pattern, string).group())
    else:
        percentage = None

    return count, percentage


