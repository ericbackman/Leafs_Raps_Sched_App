import requests

def get_schedule():
    url = "https://statsapi.web.nhl.com/api/v1/schedule?teamId=10&startDate=2018-09-01&endDate=2018-12-01"
    for i in range(5):
        try:
            r = requests.get(url, timeout=10)
            print(r.status_code)
            if r.status_code == 200:
                print(r.text)
                return r.text
        except:
            print('Error on attempt {}/5').format(i)


get_schedule()
