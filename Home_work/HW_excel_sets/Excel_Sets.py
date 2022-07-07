import openpyxl
import re

wb = openpyxl.load_workbook('data.xlsx')
sheet = wb.active

log = dict()
# перебираем ячейки 1-го столбца и группируем по времени лога
for c in sheet['A''B''C''D''E''F''G''H''I''J''K']:
    key = c.value[:8]
    val = c.value[10:]
    log[key] = log.get(key,'') + val

rc = re.compile(r"(\d+-\d+-\d+) (\d+:\d+:\d+).*?Flow (\d+).*?POS:.*?(\d+)")
new_data = []
for key, val in log.items():
    m = rc.search(val)
    if m:
        new_data.append(m.groups())

# наши разбитые данные
print('new data:', new_data)
