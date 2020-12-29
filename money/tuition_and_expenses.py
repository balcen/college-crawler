def set_format(profile_data, money):
    money.update({
        "total_tuition": money_string_to_int(profile_data["attendanceCost"][0]),
        "tuition_fee": money_string_to_int(profile_data["tuitionFeesCost"][1]),
        "room_fee": money_string_to_int(profile_data["roomBoardCost"]),
        "books_fee": money_string_to_int(profile_data["suppliesCost"]),
        "other_fee": money_string_to_int(profile_data["otherExpensesCost"]),
        "payment_plans": merge_plans(profile_data["paymentPlans"])
    })


def money_string_to_int(string):
    if "$" in string:
        if "Out-of-state" in string:
            cost = string.split("Out-of-state:")[1]
            return cost.replace(" ", "").replace("$", "").replace(",", "")
        else:
            return int(string.replace(",", "").replace("$", ""))
    return None


def merge_plans(plan_list):
    plan_list = [v + " plan" for v in plan_list]
    return ", ".join(plan_list)
