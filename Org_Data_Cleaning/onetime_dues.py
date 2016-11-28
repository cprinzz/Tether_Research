#Finds all dues values without 'year', 'yr', or 'semester' and assigns the corresponding number as the one-time dues cost


import csv

with open('/Users/cprinz/Google Drive/Tether/Pitch Materials/TAMU_Dues.csv', 'rb') as f:
    reader = csv.reader(f)
    master = list(reader)

onetime = master

for r in range(1, len(master)):
    text = master[r][0].lower()
    onetime[r][0] = ''
    if text.find('semester') == -1 and text.find('year') == -1 and text.find('yr') == -1:
        for i in range(len(text)-1, -1, -1):
            letter = text[i]
            if letter.isdigit() or letter == '.':
                l = i
                while text[l].isdigit() and l >=0:
                    prev = onetime[r][0]
                    onetime[r][0] = text[l] + prev
                    l -= 1
                break
            onetime[r][0] = '0'

print onetime

with open('/Users/cprinz/Google Drive/Tether/Pitch Materials/AM_Onetime_Dues.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')

    for i in range(0, len(onetime)-1):
        writer.writerow([onetime[i][0]])
