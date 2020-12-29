from dateutil.parser import parser
from datetime import datetime
import re


def set_format(apply_data, money):
    for datum in apply_data:
        apply_type = datum["type"]
        data = datum["data"]

        if apply_type == "TitleLink":
            title = data["title"]

            if title == "Email":
                money.update({
                    "finaid_email": data["text"]
                })
            elif title == "Website":
                money.update({
                    "finaid_website": data["link"]
                })
            elif title == "Net Price Calculator":
                money.update({
                    "finaid_net_price_calc_website": data["link"]
                })
            elif title == "Application Deadline":
                money.update({
                    "finaid_app_priority_deadline": convert_string_to_date(data["value"][0])
                })
                if len(data["value"]) > 1:
                    money.update({
                        "finaid_app_final_deadline": convert_string_to_date(data["value"][1])
                    })
            elif title == "Award Notification":
                money.update({
                    "finaid_notification_date": data["value"][0]
                })
            elif title == "Methodology For Awarding Institutional Aid":
                money.update({
                    "finaid_methodology": data["value"][0]
                })
        elif apply_type == "LabeledTable":
            for label in data["data"]:
                if "FAFSA" in label["label"]:
                    code_pattern = r"(?<=Codeis)[0-9]+"
                    if re.search(code_pattern, label["label"]) is not None:
                        code = re.search(code_pattern, label["label"].replace(" ", "")).group()
                        money.update({
                            "finaid_fafsa_code": code,
                            "finaid_fafsa_cost": label["values"][0]
                        })
                elif "CSS" in label["label"]:
                    money.update({
                        "finaid_css_cost": label["values"][0]
                    })
                elif "Farm" in label["label"]:
                    money.update({
                        "finaid_business_farm_supplement": label["values"][0]
                    })
                elif "Noncustodial" in label["label"]:
                    money.update({
                        "finaid_noncustodial_statement": label["values"][0]
                    })


def convert_string_to_date(string):
    try:
        p = parser()
        date = p.parse(string, default=datetime(1970, 1, 1, 0, 0))
        return datetime.strftime(date, "%Y-%m-%d")
    except ValueError:
        return None
