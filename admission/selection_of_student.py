def set_format(data_children, admission):
    for data_child in data_children:
        child_type = data_child["type"]
        data = data_child["data"]
        title = data["title"]
        subjects = data["data"]

        if title == "Very Important":
            level = 1
        elif title == "Important":
            level = 2
        elif title == "Considered":
            level = 3
        elif title == "Not Considered":
            level = 4
        else:
            level = 4
        
        set_selection(admission, subjects, level)
        

def set_selection(admission, data, num):
    for select in data:
        admission.update({
            convert_selection(select): num
        })


def convert_selection(selection):
    if selection == "Academic GPA":
        return "impt_gpa"
    elif selection == "Rigor of Secondary School Record":
        return "impt_hs_record"
    elif selection == "Standardized Tests":
        return "impt_tests"
    elif selection == "Class Rank":
        return "impt_rank"
    elif selection == "Recommendations":
        return "impt_recommendations"
    elif selection == "Essay":
        return "impt_essay"
    elif selection == "Interview":
        return "impt_interview"
    elif selection == "Level of Applicant's Interest":
        return "impt_interest"
    elif selection == "Extracurricular Activities":
        return "impt_activities"
    elif selection == "Volunteer Work":
        return "impt_volunteering"
    elif selection == "Particular Talent/Ability":
        return "impt_talen"
    elif selection == "Character/Personal Qualities":
        return "impt_personality"
    elif selection == "First Generation to Attend College":
        return "impt_first_gen"
    elif selection == "State Residency":
        return "impt_state_residency"
    elif selection == "Geographic Residence":
        return "impt_geography"
    elif selection == "Relation with Alumnus":
        return "impt_alumnus_relationship"
    elif selection == "Religious Affiliation/Commitment":
        return "impt_religion"
    elif selection == "Ethnicity":
        return "impt_ethnicity"
    elif selection == "Work Experience":
        return "impt_work_experience"
    else:
        return ""
