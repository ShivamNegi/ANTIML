#ls={'jaundice':0,'influenza':1,'typhoid':2,'cholera':3,'tuber':4, 'food poisoning':5,'malaria':6}
#import csv
#with open('/home/test/Downloads/models-master/official/boosted_trees/tmp/all_disease_training_data5.csv' , 'wb') as fout:
#	for row in csv_reader:
#		s = ''
#		row[0] = ls[row[0].lower()]
#		ss = list(row[1])
#		ss[0] = str(ord(ss[0]) - ord('A'))
#		row[1] = ''.join(ss)
#		i = 0
#		while i < 9:
#			s = s + str(row[i]) + ','
#			i = i + 1
#		s = s + row[9] + '\n'
#		fout.write(s)

##disease malaria, tb, jaundice, diarrhea, diabetes, arthritis
#sympots order: fever, stomach, body, cold, bp

disease_symp_weights = [[1.0, 0.02227188531851494, 0.06086742843101118, 0.07724200913242009, 0.004109831982666225, 0.051621555015730666], [0.05382466572375683, 0.16265128223314107, 0.5426957925993623, 1.0, 0.17314510744545134, 0.14457531194756312], [0.5556734815476855, 0.10924538938551985, 1.0, 0.7432876712328768, 0.23011203725836424, 0.9406662036548066], [0.7979404553742906, 1.0, 0.5055740051710489, 0.3518916414170992, 0.23780189959750422, 0.24693388967291854], [0.09811592481227421, 0.024154009997084603, 0.05642071253761107, 0.09724100144776354, 1.0, 0.07353170048931598]]


def fill_ls1(l):
    ls = [0] * l
    for i in range(0, l):
        ls[i] = i
    return ls

def count(col):
    global mat
    cnt = 0
    for i in range(0, 1000):
        if mat[i][col] == 1:
            cnt = cnt + 1
    return cnt


from random import randint


def reset_mat():
    global mat
    mat = [0] * 1000
    for i in range (0, 1000):
        mat[i] =[0] * 5


mat = []
	
def shuffle(fev1_ls, stom1_ls, body1_ls, cold1_ls, blood1_ls , n):

    global mat
    while n > 0:
        len_fev     = len(fev1_ls)
        len_stom    = len(stom1_ls)
        len_body   =  len(body1_ls)
        len_cold   =  len(cold1_ls)
        len_blood   = len(blood1_ls)
        for i in range (0, len_fev):
            x = randint(0, 999)
            temp = mat[x][0]
            mat[x][0] = mat[fev1_ls[i]][0]
            mat[fev1_ls[i]][0] = temp
            fev1_ls[i] = x
        for i in range (0, len_stom):
            x = randint(0, 999)
            pos = stom1_ls[i]
            col = 1
            temp = mat[x][col]
            mat[x][col] = mat[pos][col]
            mat[pos][col] = temp
            stom1_ls[i] = x
        for i in range (0, len_body):
            col = 2
            x = randint(0, 999)
            pos = body1_ls[i]
            temp = mat[x][col]
            mat[x][col] = mat[pos][col]
            mat[pos][col] = temp
            body1_ls[i] = x
        for i in range (0, len_cold):
            col = 3
            x = randint(0, 999)
            pos = cold1_ls[i]
            temp = mat[x][col]
            mat[x][col] = mat[pos][col]
            mat[pos][col] = temp
            cold1_ls[i] = x
        for i in range (0, len_blood):
            col = 4
            x = randint(0, 999)
            pos = blood1_ls[i]
            temp = mat[x][col]
            mat[x][col] = mat[pos][col]
            mat[pos][col] = temp
            blood1_ls[i] = x
        n = n - 1
    return fev1_ls, stom1_ls, body1_ls, cold1_ls, blood1_ls


def create_matrix(percent_ls):

    fev = percent_ls[0]
    stom = percent_ls[1]
    body = percent_ls[2]
    cold = percent_ls[3]
    blood = percent_ls[4]

    global mat
    mat = [[0. for i in range(5)] for j in range(1000)]
    fev1_ls     =  fill_ls1(int(fev * 1000))
    stom1_ls    =  fill_ls1(int(stom * 1000))
    body1_ls    =  fill_ls1(int(body * 1000))
    cold1_ls    =  fill_ls1(int(cold * 1000))
    blood1_ls   =  fill_ls1(int(blood * 1000))


    len_fev     = int(fev * 1000)
    len_stom    = int(stom * 1000)
    len_body   =  int(body * 1000)
    len_cold   =  int(cold * 1000)
    len_blood   = int(blood * 1000)







    for i in range (0, 1000):
        mat[i] =[0] * 5

    for i in range (0, len_fev):
        mat[i][0] = 1
    
    for i in range (0, len_stom):
        mat[i][1] = 1

    for i in range (0, len_body):
        mat[i][2] = 1
    
    for i in range (0, len_cold):
        mat[i][3] = 1
    
    for i in range (0, len_blood):
        mat[i][4] = 1
    

   

    for i in range(0, 5):
       print(count(i))
       print('\n')

    shuffle(fev1_ls, stom1_ls, body1_ls, cold1_ls, blood1_ls, 3)

    for i in range(0, 5):
        print(count(i))
        print('\n')
    
    print('\n')
    print('\n')
    print('\n')
    print(mat)

'''
def write_to_csv(name):
    #name = 'jaundice'
    with open('./' + name + '.csv' , 'wb') as fout:
        for row in mat:
            s = name
            for i in range(0, len(row)):
                s = s + ',' + str(row[i])
            fout.write(s + '\n')
'''
import csv
diseases = ['malaria', 'tuberculosis', 'jaundice', 'diarrhea', 'diabetes', 'arthritis']
def fill_percent_ls():
    disease_cnt = 0
    with open('./'  + 'disease_symptoms.csv' , 'wb') as fout:
        while disease_cnt < 6:
            symptom_cnt = 0
            percent_ls = [0] * 5
            while symptom_cnt < 5:
                percent_ls[symptom_cnt] = disease_symp_weights[symptom_cnt][disease_cnt]
                symptom_cnt += 1
            create_matrix(percent_ls)
            data = mat

            for row in mat:
                s = diseases[disease_cnt]
                for i in range(0, len(row)):
                    s = s + ',' + str(row[i])
                fout.write(s + '\n')
            disease_cnt += 1
            reset_mat()

fill_percent_ls()
#ls={'jaundice':0,'influenza':1,'typhoid':2,'cholera':3,'tuber':4, 'food poisoning':5,'malaria':6}
#import csv
#name = 'jaundice'
#with open('./' + name + '.csv' , 'wb') as fout:
#    for row in mat:
#        s = name
#        for i in range(0, len(row)):
#            s = s + ',' + str(row[i])
#        fout.write(s + '\n')

