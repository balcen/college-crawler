def set_format(apply_datas, admission):
    for apply_data in apply_datas:
        data_type = apply_data["type"]
        if data_type == "CategoryDivider":
            continue
        data = apply_data["data"]
        title = data["title"]
        if title == "Address":
            admission.update({
                "ao_address": data["value"][0],
                "ao_city": data["value"][1],
                "ao_state": data["value"][2],
                "ao_zipcode1": data["value"][3]
            })
        elif title == "Phone":
            admission.update({
                "ao_phone": data["value"][0]
            })
        elif title == "E-mail":
            admission.update({
                "ao_email": data["value"][0]
            })
        elif title == "Regular Admission Deadline":
            admission.update({
                "rd_deadline_is_rolling": 1 if "Rolling" in data["value"][0] else 0,
                "rd_deadline": data["value"][0]
            })
        elif title == "Application Fee":
            if "-" in data["value"][0]:
                fee_arr = data["value"][0].replace("$", "").strip().split("-")
                fee = round((int(fee_arr[0]) + int(fee_arr[1])) / 2)
            elif "No" in data["value"][0]:
                fee = 0
            else:
                fee = int(data["value"][0].replace("$", ""))
            admission.update({
                "application_fee": fee
            })
        elif title == "Application Fee Waiver":
            admission.update({
                "has_application_fee_waiver": 1 if data["value"][0] == "Available" else 0
            })
        elif title == "Regular Admission Notification":
            admission.update({
                "rd_notification_date_is_rolling": 1 if "Rolling" in data["value"] else 0,
                "rd_notification_date": data["value"][0]
            })
        elif title == "Accept Offer of Admission":
            admission.update({
                "accept_offer_admission_date": data["value"][0]
            })
        elif title == "Waiting List Used":
            admission.update({
                "has_waitlist": 1 if data["value"][0] == "Yes" else 0
            })
        elif title == "Defer Admission":
            admission.update({
                "can_defer": 0 if "cannot" in data["value"][0] else 1
            })
        elif title == "Transfer Admission":
            admission.update({
                "can_transfer": 0 if "not" in data["value"][0] else 1
            })
        # TODO
        elif title == "Early Decision Offered":
            pass
        elif title == "Common Application":
            admission.update({
                "accepts_commonapp": 0 if "Not accepted" in data["value"][0] else 1,
                "has_commonapp_supplement": 1 if "Accepted" in data["value"][0] or "supplemental forms required" in
                                                 data["value"][0] else 0
            })
        elif title == "Universal College Application":
            admission.update({
                "accepts_universalapp": 0 if "Not accepted" in data["value"][0] else 1,
                "has_universalapp_supplement": 1 if "Accepted" in data["value"][0] or "supplemental forms required" in
                                                    data["value"][0] else 0
            })
        elif title == "Electronic Application":
            admission.update({
                "accepts_electronicapp": 0 if "Not accepted" in data["text"] else 1,
                "has_electronic_supplement": 1 if "Accepted" in data["text"] or "supplemental forms required" in
                                                  data["text"] else 0
            })
        elif title == "Interview":
            admission.update({
                "interview_policy": data["value"][0]
            })
        elif title == "Essay or Personal Statement":
            admission.update({
                "college_essay_policy": data["value"][0]
            })
        elif title == "Letter of Recommendation":
            admission.update({
                "recommendation_policy": data["value"][0]
            })
        elif title == "Other":
            admission.update({
                "app_other_policy": data["value"][0]
            })
        elif title == "Financial Need":
            admission.update({
                "financial_need_considered": 0 if "not" in data["value"][0] else 1
            })
