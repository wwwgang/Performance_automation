from locust import HttpLocust, TaskSet, task
import requests
from unit.csvController import opencsv

count = 1


class WebsiteTasks(TaskSet):
    error_info = []

    def on_start(self):
        pass

    @task
    def request_get(self):
        global count
        for i in opencsv()['GET']:
            info = []
            url = i[1]
            headers = i[2]
            req = self.client.get(url=url, headers=headers)
            if req.status_code != 200:
                info.append(count)
                count += 1
                info.append(req.url)
                info.append('GET')
                info.append(headers)
                info.append('/NULL')
                info.append(req.headers)
                info.append(req.text)
                self.error_info.append(info)

    @task
    def request_post(self):
        global count
        for i in opencsv()['POST']:
            info = []
            url = i[1]
            headers = eval(i[2])
            data = i[4]
            req = self.client.post(url=url, data=data, headers=headers)
            if req.status_code != 200:
                info.append(count)
                count += 1
                info.append(req.url)
                info.append('POST')
                info.append(headers)
                info.append(data)
                info.append(req.headers)
                info.append(req.text)
                self.error_info.append(info)


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "http://127.0.0.1:5000"
    # wait_time = 1000
    min_wait = 1000
    max_wait = 2000
