from googletrans import Translator
from tqdm import tqdm
import json
import database
import file


def trans(string, to=None):
    # Initial
    translator = Translator()
    translator.raise_Exception = True

    dest = 'en' if to is None else to

    return translator.translate(string, dest=dest).text


def translate_file():
    schools = database.select("schools")
    schools_file = file.read()
    result = dict()
    
    for i, school in schools:
        tmp = dict()

        tmp.update({
            "name": json.dumps({
                "en": school["name_en"],
                "tw": school["name_tw"],
                "cn": school["name_cn"]
            }),
            "overview": school["overview"],
            "website": school["website"]
        })


def translate_school(schools):
    with tqdm(total=len(schools)) as bar:
        result = dict()
        for slug, school in schools.items():
            info = school["overview"]
            tmp = dict()

            if info["name_en"] is not None:
                tmp.update({
                    "name": json.dumps({
                        "en": info["name_en"],
                        "tw": trans(info["name_en"], "zh-tw"),
                        "cn": trans(info["name_en"], "zh-cn")
                    })
                })

            # if info["overview"] is not None:
            #     # print(info["overview"])
            #     # print(trans(info["overview"], "zh-tw"))
            #     # print(trans(info["overview"], "zh-cn"))
            #     tmp.update({
            #         "overview": json.dumps({
            #             "en": info["overview"],
            #             "tw": trans(info["overview"], "zh-tw"),
            #             "cn": trans(info["overview"], "zh-cn")
            #         })
            #     })

            result[slug] = tmp
            bar.update(1)
            break

        return result
