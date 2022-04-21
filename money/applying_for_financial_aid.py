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
        elif apply_type == "TitleValue":
            title = data["title"]

            if title == "Application Deadline":
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
            title = data["keyTitle"]

            if title == "Forms Required":
                for label_data in data["data"]:
                    if "FAFSA" in label_data["label"]:
                        code_pattern = r"(?<=Codeis)[0-9]+"
                        if re.search(code_pattern, label_data["label"].replace(" ", "")) is not None:
                            code = re.search(code_pattern, label_data["label"].replace(" ", "")).group()
                            money.update({
                                "finaid_fafsa_code": code,
                                "finaid_fafsa_cost": 0 if "Free" in label_data["values"][0] else label_data["values"][0]
                            })
                    elif "CSS" in label_data["label"]:
                        money.update({
                            "finaid_css_cost": label_data["values"][0]
                        })
                    elif "Farm" in label_data["label"]:
                        money.update({
                            "finaid_business_farm_supplement": label_data["values"][0]
                        })
                    elif "Noncustodial" in label_data["label"]:
                        money.update({
                            "finaid_noncustodial_statement": label_data["values"][0]
                        })


def convert_string_to_date(string):
    try:
        p = parser()
        date = p.parse(string, default=datetime(1970, 1, 1, 0, 0))
        return datetime.strftime(date, "%Y-%m-%d")
    except ValueError:
        return None
