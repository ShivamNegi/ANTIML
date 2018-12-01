import csv





ls={'jaundice':[],'influenza':[],'typhoid':[],'cholera':[],'tuber':[], 'food poisoning':[],'malaria':[]}
import csv
with open('/home/test/Downloads/models-master/official/boosted_trees/tmp/all_disease_training_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        l = len(row)
        s = ''
        for i in range(1, l - 1):
            s = s + str(row[i]) + '.'
        s = s + str(row[l-1])
        ls2 = ls[row[0].lower()]
        ls2.append(s)

q = 'D10,251,355,255,550,200,200'
q = q.replace(',', '.')


def match(query, s):
    print(s )
    q_ls = query.split('.')
    s_ls = s.split('.')

    s_l1 = len(s_ls)
    q_l1 = len(q_ls)
    l = min(s_l1, q_l1)
    for i in range(0, l):
        if s_ls[i] != q_ls[i]:
            return i
    return l




res={'jaundice':0,'influenza':0,'typhoid':0,'cholera':0,'tuber':0, 'food poisoning':0,'malaria':0}
percent = {'jaundice':0.0,'influenza':0.0,'typhoid':0.0,'cholera':0.0,'tuber':0.0, 'food poisoning':0.0,'malaria':0.0}
wt = {'jaundice':0.0,'influenza':0.0,'typhoid':0.0,'cholera':0.0,'tuber':0.0, 'food poisoning':0.0,'malaria':0.0}

for i in ls:
    cnt = 0
    for j in ls[i]:
        x = int(match(q, j))
        if x > res[i]:
            res[i] = x
            cnt = 1
        elif x == res[i]:
            cnt = cnt + 1
    if len(ls[i]) != 0 :
        percent[i] = (float(cnt) / float(len(ls[i])))
        #wt[i] = (float(cnt) / float(len(ls[i]))) * (float(res[i]) / float(q.count('.')))


print(res)
print(percent)
#print(wt)