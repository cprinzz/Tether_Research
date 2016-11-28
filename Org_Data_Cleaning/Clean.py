#Creates table out of scraped TAMU organization data

import csv

with open('/Users/cprinz/Google Drive/Tether/Product/A&M Org Lists/TAMU_Orgs_Master.csv', 'rb') as f:
    reader = csv.reader(f)
    master = list(reader)

#creates list of unique organization names and features
def dedupe(myList, col):
    newList = []
    for x in range(0, len(myList)-1):
        newList.append(myList[x][col])

    uniques = set(newList)
    uniqueList = list(uniques)
    return uniqueList

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))


uniqueorgs = dedupe(master, 1)
uniquefields = dedupe(master, 2)
uniquefields.insert(0,'Category:')
uniquefields.insert(1,'Organization Name:')


#TAMU_Cleaned.csv in format:
#[[Org1, label1, value1],[Org1, label2, value2], [Org1, label3, value3], [Org2, label1, value1]...]
#note: Not all organizations have the same quantity of labels due to optional fields.

cleaned = uniquefields


with open('/Users/cprinz/Google Drive/Tether/Product/TAMU_Cleaned.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    #writes label row
    writer.writerow(uniquefields)
    #iterates through organization names
    for i in range(0, len(uniqueorgs)-1):
        orgname = uniqueorgs[i]
        r = index_2d(master, orgname)[0]
        c = index_2d(master, orgname)[1]
        #creates new row with organization category [r][0] and name [r][1]
        newrow = [master[r][0], master[r][1]]
        #iterates through labels
        for x in range(2, len(uniquefields)):
            y = r
            found = False
            #iterates through the org name column and adds values to new row according to corresponding headers
            #Adds value "Not Listed" if the organization did not fill out the field
            while master[y][1] == orgname and y < len(master)-1:
                if master[y][2] == uniquefields[x]:
                    newrow.append(master[y][3])
                    found = True
                y += 1
            if found != True:
                newrow.append("Not Listed")
        print(newrow)
        writer.writerow(newrow)
















