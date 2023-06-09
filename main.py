import json
from gadget import read_csv, HashlibBasedList
from google_trans import GoogleTranslate

FILEPATH = "./Chats (EMKcUr_OjbA) (original).csv"
filtered_content = HashlibBasedList()
csv_header = ""

for row in read_csv(FILEPATH):
    if type(row) is list:
        csv_header = ",".join(row)
    else:
        filtered_content.append(row)

with open(FILEPATH + ".csv", mode="w", encoding="UTF-8") as file:
    file.write(csv_header + "\n")
    for i in filtered_content:
        file.write(i.to_csv() + "\n")

with open(FILEPATH + ".json", mode="w", encoding="UTF-8") as file:
    file.write("[")
    for i in filtered_content:
        file.write(json.dumps(i.to_json(), ensure_ascii=False) + ",")
    file.write("]")

with open(FILEPATH + ".cn.csv", mode="w", encoding="UTF-8") as file:
    file.write(csv_header + "\n")
    for j in range(len(filtered_content)):
        i = filtered_content[j]
        try:
            lang = GoogleTranslate(i.message).language()
        except Exception as e:
            file.write(i.to_csv() + "\n")
        else:
            if "zh" in lang:
                file.write(i.to_csv() + "\n")
            # print(lang)
        if j % 100 == 0:
            print(j)

