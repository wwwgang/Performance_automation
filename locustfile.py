from locust import HttpLocust, TaskSet, task
from unit.csvController import opencsv_preformance_automation, writecsv_error_info
import time

error_info = []
count = 1


class WebsiteTasks(TaskSet):

    def on_start(self):
        pass

    @task
    def request_get(self):
        global count
        for i in opencsv_preformance_automation()['GET']:
            info = []
            url = i[1]
            headers = i[2]
            data = i[4]
            req = self.client.get(url=url, headers=headers)
            if req.status_code != 200:
                info.append(count)
                count += 1
                info.append(url)
                info.append('GET')
                info.append(headers)
                info.append(data)
                info.append(req.headers.__str__())
                info.append(req.text)
                info.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                error_info.append(info)

    @task
    def request_post(self):
        global count
        for i in opencsv_preformance_automation()['POST']:
            info = []
            url = i[1]
            headers = eval(i[2])
            data = i[4]
            req = self.client.post(url=url, data=data, headers=headers)
            if req.status_code != 200:
                info.append(count)
                count += 1
                info.append(url)
                info.append('POST')
                info.append(headers)
                info.append(data)
                info.append(req.headers.__str__())
                info.append(req.text)
                info.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                error_info.append(info)

    def on_stop(self):
        writecsv_error_info(error_info)


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "http://127.0.0.1:5000"
    # wait_time = 1000
    min_wait = 1000
    max_wait = 2000
