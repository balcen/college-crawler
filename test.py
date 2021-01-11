import database
import json
import file


schools = database.select("schools")

new_schools = list()
for school in schools:
    tmp = {
        "name": json.dumps({
            "en": school["name_en"],
            "tw": school["name_tw"],
            "cn": school["name_cn"],
        }),
        "overview": school["overview"],
        "website": school["website"]
    }

    new_schools.append(tmp)

old_schools = file.read()

index = 0
for slug, old_school in old_schools.items():
    if "name_en" in old_school:
        del old_school["name_en"]
    old_school.update({
        "overview": new_schools[index]
    })
    index += 1

file.store(old_schools, "trans-schools")
