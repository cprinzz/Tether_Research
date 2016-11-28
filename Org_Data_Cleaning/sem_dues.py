#Finds all dues values with 'semester' and assigns the corresponding number as the semesterly dues cost


import csv

with open('/Users/cprinz/Google Drive/Tether/Pitch Materials/TAMU_Dues.csv', 'rb') as f:
    reader = csv.reader(f)
    master = list(reader)

semester = master

for r in range(1, len(master)):
    text = master[r][0].lower()
    semester[r][0] = ''
    if text.find('semester') != -1:
        for i in range(text.index('semester'), -1, -1):
            letter = text[i]
            if letter.isdigit() or letter == '.':
                l = i
                while text[l].isdigit():
                    prev = semester[r][0]
                    semester[r][0] = text[l] + prev
                    l -= 1
                break

print semester

with open('/Users/cprinz/Google Drive/Tether/Pitch Materials/AM_Sem_Dues.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')

    for i in range(0, len(semester)-1):
        writer.writerow([semester[i][0]])


