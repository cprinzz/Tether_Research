#Finds all dues values with 'year' or 'yr' and assigns the corresponding number as the yearly dues cost


import csv

with open('/Users/cprinz/Google Drive/Tether/Pitch Materials/TAMU_Dues.csv', 'rb') as f:
    reader = csv.reader(f)
    master = list(reader)

year = master


for r in range(1, len(master)):
    text = year[r][0].lower()
    year[r][0] = ''
    if text.find('year') != -1:
        for i in range(text.index('year'), -1, -1):
            letter = text[i]
            if letter.isdigit() or letter == '.':
                l = i
                while text[l].isdigit():
                    prev = year[r][0]
                    year[r][0] = text[l] + prev
                    l -= 1
                break
    elif text.find('yr') != -1:
        for i in range(text.index('yr'), -1, -1):
            letter = text[i]
            if letter.isdigit() or letter == '.':
                l = i
                while text[l].isdigit():
                    prev = year[r][0]
                    year[r][0] = text[l] + prev
                    l -= 1
                break

print year

with open('/Users/cprinz/Google Drive/Tether/Pitch Materials/AM_Yr_Dues.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')

    for i in range(0, len(year)-1):
        writer.writerow([year[i][0]])
