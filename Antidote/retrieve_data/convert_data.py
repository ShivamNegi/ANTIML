from Bio import Entrez
from Bio import Medline
from Bio import *
from pubchempy import *

Entrez.email = "A.N.Other@example.com"



def fx(pmid1):
	handle1 = Entrez.esummary(db="mesh", id=pmid1)
	record1 = Entrez.read(handle1)
	return record1
	#print (record1)


def disp(obj):
    x = obj[0]['DS_IdxLinks'][0]
    return x['TreeNum']
	#for i in obj:
	#	#print (i)
	#	for j in i:
	#		print(str(j) + '\t' + str(i[j]) + '\n')
	#	print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
	


#handle = Entrez.esummary(db="mesh", id=r['IdList'][0])
#record = Entrez.read(handle)



#pmid = "c106856"
#record = Entrez.read(Entrez.elink(dbfrom="mesh", id=pmid))
#print(record)




def pre_fx(pmid):
    print(pmid)
    h = Entrez.esearch(db='mesh', retmode='text', term=pmid)
    r = Entrez.read(h)
    ls =[]
    ls2 = []
    try:
        handle = Entrez.esummary(db="mesh", id=r['IdList'][0])
        record = Entrez.read(handle)
        if len(record[0]['DS_HeadingMappedToList']) == 0:
            ls2.append(disp(record))
            return ls2
        for i in record[0]['DS_HeadingMappedToList']:
            ls.append(i)
    except:
        print ("except")
    for i in ls:
	    obj = fx(str(i))
	    print (i)
	    ls2.append(disp(obj))
    return ls2


import csv
def create_csv(row_num, filename):
    with open('../data/' + filename ,'w') as op:
        with open('../data/disease_cid.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            count = 0
            n = 0
            for i in csv_reader:
                if n == int(row_num):
                    n = n + 1
                    row = i
                    for cell in row:
                        #print (cell)
                        if count == 0:
                            print (cell + '\n')
                            count = count + 1
                            #op.write(cell + ',')
                        else:
                            x = pre_fx(cell)
                            for k in x:
                                    op.write(str(row[0]+','+k + '\n'))
                    break
                else:
                    n = n + 1
                        #op.write('\n')


def main1():
    row_num = input("row num:\n")
    file_name = input("file name? \n")
    create_csv(row_num, file_name)

main1()

#pre_fx("C471674")
#print (r)
#handle = Entrez.esummary(db="mesh", id=r['IdList'][0])
#record = Entrez.read(handle)
#disp(record)
#
#'''
#for i in record:
#	print (i)
#	for j in i:
#		print(str(j) + '\t' + str(i[j]) + '\n')
#	print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
#'''
#print('\n\n\n')
#ls = []
#for i in record[0]['DS_HeadingMappedToList']:
#	ls.append(i)
#
#for i in ls:
#	obj = fx(str(i))
#	print (i)
#	disp(obj)
#	
##D03.633.100.810.835.322.500