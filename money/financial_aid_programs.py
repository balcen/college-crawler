def set_format(financial_data, money):
    for financial_datum in financial_data:
        financial_type = financial_datum["type"]
        data = financial_datum["data"]

        if financial_type == "TitleValue":
            title = data["title"]

            if title == "Federal Loans":
                money.update({
                    "federal_loan_programs": ", ".join(data["value"])
                })
            elif title == "State Loans":
                money.update({
                    "state_loan_is_available": 1 if data["value"][0] == "Available" else 0
                })
            elif title == "Other Loans":
                money.update({
                    "other_loan_programs": data["value"][0]
                })
            elif title == "Need-Based Available":
                money.update({
                    "need_based_programs": ", ".join(data["value"])
                })
            elif title == "Non-Need-Based Available":
                money.update({
                    "nonneed-based_programs": data["value"][0]
                })
            elif title == "Work-Study Programs":
                money.update({
                    "workstudy_programs": ", ".join(data["value"])
                })
            elif title == "Average Earnings from On-Campus Employment":
                if "$" in data["value"][0]:
                    money.update({
                        "workstudy_avg_earning": data["value"][0].replace(",", "").replace("$", "")
                    })
