def set_format(children_data, campus):
    for child_data in children_data:
        child_type = child_data["type"]
        data = child_data["data"]

        if child_type == "TitleValue":
            title = data["title"]

            if title == "Athletic Conferences":
                campus.update({
                    "athletic_conference": data["value"][0]
                })
            elif title == "Mascot":
                campus.update({
                    "mascot": data["value"][0]
                })
            elif title == "School Colors":
                campus.update({
                    "school_colors": data["value"][0]
                })
            elif title == "Intramural Sports":
                campus.update({
                    "im_sports": data["value"][0]
                })
        elif child_type == "IconTable":
            if len(data["valueTitles"]) == 4:
                for subject in data["data"]:
                    label = subject["label"]

                    title = format_keys(label)
                    w, w_s, m, m_s = get_keys(title)

                    campus.update({
                        w: 1 if subject["values"][0] == "check" else 0,
                        w_s: 1 if subject["values"][1] == "dollar" else 0,
                        m: 1 if subject["values"][2] == "check" else 0,
                        m_s: 1 if subject["values"][3] == "dollar" else 0
                    })
            elif len(data["valueTitles"]) == 2:
                for subject in data["data"]:
                    label = subject["label"]

                    title = format_keys(label)
                    w = f"has_w_{title}_club"
                    m = f"has_m_{title}_club"

                    campus.update({
                        w: 1 if subject["values"][0] == "check" else 0,
                        m: 1 if subject["values"][1] == "check" else 0
                    })


def format_keys(subject):
    if subject == "Baseball":
        subject_string = "baseball"
    elif subject == "Basketball":
        subject_string = "basketball"
    elif subject == "Crew":
        subject_string = "crew"
    elif subject == "Cross-Country Running":
        subject_string = "cc"
    elif subject == "Fencing":
        subject_string = "fencing"
    elif subject == "Field Hockey":
        subject_string = "hockey"
    elif subject == "Football":
        subject_string = "football"
    elif subject == "Golf":
        subject_string = "golf"
    elif subject == "Ice Hockey":
        subject_string = "icehockey"
    elif subject == "Lacrosse":
        subject_string = "lax"
    elif subject == "Rugby":
        subject_string = "rugby"
    elif subject == "Sailing":
        subject_string = "sailing"
    elif "Cross-Country" in subject:
        subject_string = "cc_ski"
    elif "Downhill" in subject:
        subject_string = "dh_ski"
    elif subject == "Soccer":
        subject_string = "soccer"
    elif subject == "Softball":
        subject_string = "softball"
    elif subject == "Squash":
        subject_string = "squash"
    elif subject == "Swimming And Diving":
        subject_string = "swim"
    elif subject == "Tennis":
        subject_string = "tennis"
    elif subject == "Track And Field":
        subject_string = "track"
    elif subject == "Volleyball":
        subject_string = "vball"
    elif subject == "Water Polo":
        subject_string = "wpolo"
    else:
        subject_string = "wrestling"
    return subject_string


def get_keys(title):
    w = f"has_w_{title}"
    w_s = f"has_w_{title}_scho"
    m = f"has_m_{title}"
    m_s = f"has_m_{title}_scho"

    return w, w_s, m, m_s
