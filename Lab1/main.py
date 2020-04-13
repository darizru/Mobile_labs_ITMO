import csv
from tariffication import Tariffication

user = Tariffication("968247916")

with open('data.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['msisdn_origin'] == user.getId():
            user.addCallOutDuration(float(row['call_duration']))

        if row['msisdn_dest'] == user.getId():
            user.addCallInDuration(float(row['call_duration']))

        if row['msisdn_origin'] == user.getId():
            user.addSmsNumber(int(row['sms_number']))

user.userTariffication()

