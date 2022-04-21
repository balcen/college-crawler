import json
import requests
import uuid


class UsNews:
    def __init__(self):
        self.header = {
            'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.181 Safari/537.36',
            'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
        }

        self.total_page = self.get_first_page()
        self.schools = []

    def get_first_page(self):
        url = "https://www.usnews.com/best-colleges/api/search?_sort=rank&_sortDirection=asc&_page=1"
        res = requests.get(url, headers=self.header)
        res_data = json.loads(res.text)
        data = res_data['data']
        return data['totalPages']

    def get_data(self):
        for page in range(1, self.total_page):
            url = "https://www.usnews.com/best-colleges/api/search?_sort=rank&_sortDirection=asc&_page={}".format(page)
            res = requests.get(url, headers=self.header)
            res_data = json.loads(res.text)

            schools = res_data['data']['items']
            for school in schools:
                institution = school['institution']
                name = institution['displayName']
                slug = institution['urlName']
                img_url = institution['primaryPhotoCardSmall']

                if img_url is None:
                    continue

                img = requests.get(img_url, headers=self.header)
                file_name = str(uuid.uuid4()) + '_' + slug + '_small.jpg'
                with open('/mnt/c/Users/baicen/Desktop/colleges_img/{}'.format(file_name), 'wb') as file:
                    file.write(img.content)

                self.schools.append({
                    'name': name,
                    'slug': slug,
                    'file_name': file_name
                })

        with open('obj/us_news_img.json', 'w') as outfile:
            json.dump(self.schools, outfile)

        with open('/mnt/c/Users/baicen/Desktop/us_news_img.json', 'w') as outfile:
            json.dump(self.schools, outfile)
