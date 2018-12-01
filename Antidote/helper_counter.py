#disease malaria, tb, jaundice, diarrhea, diabetes, arthritis
#sympots order: fever, stomach, body, cold, bp
disease_cnt = [89510, 248340, 40695, 109500, 648445, 312447]
symptoms = [[89510, 5531, 2477, 8458, 2665, 16129],[125, 1048, 573, 2841, 2913, 1172],[11, 6, 9, 18, 33, 65],[322+272, 736+3001, 258+130, 1440+625, 2179+729, 932+523],[612, 418, 160, 742, 45187, 1601]]
percent_symptoms = [[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]

cnt1 = 0

while cnt1 < 6:
    cnt2 = 0
    while cnt2 < 5:
        percent_symptoms[cnt2][cnt1] = float(symptoms[cnt2][cnt1]) / float(disease_cnt[cnt1])
        cnt2 += 1
    cnt1 += 1

print (percent_symptoms)
print ('\n')
cnt1 = 0
while cnt1 < 5:
    curr_max = max(percent_symptoms[cnt1])
    cnt2 = 0;
    while cnt2 < 6:
        percent_symptoms[cnt1][cnt2] = float(percent_symptoms[cnt1][cnt2]) / float(curr_max)
        cnt2 += 1
    cnt1 += 1

print (percent_symptoms)