import csv


def opencsv():
    data = {
        'GET': [],
        'POST': []
    }
    with open('./preformance_automation.csv') as csvfile:
        reader = csv.reader(csvfile)
        for r in reader:
            if 'GET' in r[3]:
                data['GET'].append(r)
            elif 'POST' in r[3]:
                data['POST'].append(r)
    return data


if __name__ == '__main__':
    print(opencsv()['GET'])
    print(opencsv()['POST'])
    print(opencsv()['GET'][0][4])
