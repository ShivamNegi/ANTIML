import csv
from collections import OrderedDict
disease_list = ["malaria", "tuberculosis", "jaundice", "diarrhea", "diabetes", "arthritis"]
print (disease_list)
disease_dict = OrderedDict()
disease_cnt = [0, 0, 0, 0, 0, 0]
for i in disease_list:
    disease_dict[i.lower()] = []

print (disease_dict)
f = 0
with open('../data/dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
       # print row
        if line_count <= 30:
           # print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            cnt = 0
            while cnt < 6:
                disease = disease_list[cnt]
                if disease.lower() in row[3].lower():
                    if disease_cnt[cnt] <= 1500:
                        disease_dict[disease.lower()].append(row[1])
                    disease_cnt[cnt] += 1
                cnt += 1
            line_count += 1

cnt = 0

print (disease_dict)

while cnt < 6:
    print (disease_list[cnt] + ' no. of occurences = ' + str(disease_cnt[cnt]))
    cnt += 1

with open('../data/disease_cid.csv', 'wb') as f:
    writer = csv.writer(f)
    for i in disease_dict:
        ls2 = []
        ls2.append(i)
        ls2.extend(disease_dict[i])
        writer.writerow(ls2)
    #w = csv.DictWriter(f, disease_dict.keys())
    #w.writeheader()
    #w.writecol(disease_dict)
#print(disease_dict)