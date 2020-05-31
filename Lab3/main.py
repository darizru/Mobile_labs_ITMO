from docxtpl import DocxTemplate
from datetime import datetime
from num2words import num2words
import os
import comtypes.client

NDS = 18  #ставка НДС
bill_number = 0

#заполнение формальных полей
doc = DocxTemplate("bill_template.docx")
bill_number+=1
account_number = str(bill_number)
INN = "7722737363"
KPP = "772303001"
BIK = "044525703"
bank_account = "30101810200000000300"
receiver = "ООО\"Василек\""
receiver_account = "40703810900000002353"
cur_date = datetime.today().strftime("%d.%m.%Y")
client = "ООО\"Лагуна\", ИНН 7777789463, КПП 772555001, 119361, Москва г, Тульская ул, дом №4, строение 1"
provider = "ООО\"Василек\", ИНН 7722789363, КПП 772303781, 109052, Москва г, Добрынинская ул, дом №70, корпус 2, тел.:"
reason = "№20023316 от 13.02.2016"
bank = "\"АО Стоун банк\" г. Москва"

context = {'INN': INN, 'KPP': KPP, 'BIK': BIK, 'bank': bank, 'bank_account': bank_account, 'receiver': receiver, 'receiver_account': receiver_account,'account_number': account_number, 'date': cur_date, 'provider': provider, 'client': client, 'reason': reason}
doc.render(context)

#заполнение таблицы с перечнем услуг
table = doc.tables[3]
f = open('source.txt', 'r', encoding='utf-8')
i = 1
sum = 0
flag = 0
for line in f:
    service, kol, tarif, cost = [i for i in line.split(';')]
    if kol != 0:
        if flag:
            table.add_row()
        table.cell(i, 0).text = str(i)
        table.cell(i, 1).text = str(service)
        table.cell(i, 2).text = str(kol)
        table.cell(i, 3).text = str(tarif)
        table.cell(i, 4).text = str(cost)
        sum += float(cost)
        flag = 1
        i += 1
f.close()

#заполнение полей с итогами
table = doc.tables[4]
table.cell(0, 1).text = str(sum)
table.cell(1, 1).text = str(round(sum*NDS/100, 2))
table.cell(2, 1).text = str(sum)
table.cell(3, 1).text = "Всего наименований " + str(i-1) + ", на сумму " + str(sum) + " руб."
kop = int(round((sum - int(sum)), 2)*100)
table.cell(4, 1).text = num2words(int(sum), lang='ru') + " рублей " + str(kop) + " копеек"

#заполнение полей для подписи
table = doc.tables[5]
table.cell(0, 1).text = "Семенов Д.А."
table.cell(0, 3).text = "Семенов Д.А."

#сохранение счета на оплату в формате .docx
doc.save('bill.docx')

#конвертация в формат .pdf
wdFormatPDF = 17
in_file = os.path.abspath('bill.docx')
out_file = os.path.abspath("bill.pdf")
word = comtypes.client.CreateObject('Word.Application', dynamic = True)
word.Visible = True
doc = word.Documents.Open(in_file)

doc.SaveAs(out_file, wdFormatPDF)
doc.Close()
word.Quit()
