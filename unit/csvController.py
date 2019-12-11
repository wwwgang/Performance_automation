import csv


def opencsv_preformance_automation():
    data = {
        'GET': [],
        'POST': []
    }
    with open('./preformance_automation.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for r in reader:
            if 'GET' in r[3]:
                data['GET'].append(r)
            elif 'POST' in r[3]:
                data['POST'].append(r)
    return data


def writecsv_error_info(data):
    with open('./error_info.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

def opencsv_error_info():
    data=[]
    with open('./error_info.csv','r') as csv_file:
        reader=csv.reader(csv_file)
        for r in reader:
            data.append(r)
    return data