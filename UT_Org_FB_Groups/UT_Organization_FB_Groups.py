#Uses UT organization spreadsheet to determine if

import csv

#Creates a list of facebook group/page ID's from a csv of URLs

filepath = '/Users/cprinz/Google Drive/Tether/Product/Org Lists/UT Org Lists/UT_Master.csv'

with open(filepath, 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)

facebook_URLs = []
groups = [[]]

#Populates groups
for row in data:
    if row[7] != '':
        groups.append([row[0], row[7], '', '', ''])

#Removes 2 rows of headers
groups.pop(0)
groups.pop(0)

#Determines if the param is a FB group or page ID
def isID(name):
    try:
        int(name)
        return True
    except ValueError:
        return False

for row in groups:
    url = row[1]
    page_group = row[2]
    search_term = row[3]
    id = row[4]
    name_index = 0

    #Removes query tags from url
    url_query = url.split('?')

    #Creates list of url elements
    url_elements = url_query[0].split('/')

    if 'groups' in url_elements:
        page_group = 'group'
        name_index = url_elements.index('groups') + 1
        if isID(url_elements[name_index]):
            id = url_elements[name_index]
        else:
            search_term = url_elements[name_index]
            try:
                isID(url_elements[name_index + 1])
                id = url_elements[name_index + 1]
            except IndexError:
                id = 'not found'

    elif 'pages' in url_elements:
        page_group = 'page'
        name_index = url_elements.index('pages') + 1
        if isID(url_elements[name_index]):
            id = url_elements[name_index]
        else:
            search_term = url_elements[name_index]
            try:
                isID(url_elements[name_index + 1])
                id = url_elements[name_index + 1]
            except IndexError:
                id = 'not found'

    else:
        page_group = 'unknown'
        try:
            name_index = url_elements.index('www.facebook.com') + 1
        except ValueError:
            print "www.facebook.com not in list"
        try:
            name_index = url_elements.index('facebook.com') + 1
        except ValueError:
            print "facebook.com not in list"

        if isID(url_elements[name_index]):
            id = url_elements[name_index]
        else:
            search_term = url_elements[name_index]

    row[2] = page_group
    row[3] = search_term
    row[4] = id


print groups

#Verifying counts of IDs and search terms
#
# countID = 0
# countName = 0
# both = 0
# total = 0
#
# for row in groups:
#     if row[3] != '':
#         countName += 1
#     if row[4] != '':
#         countID += 1
#     if row[3] != '' and row[4] != '':
#         both += 1
#     total +=1
#
# print 'countID: ' + str(countID)
# print 'countName: ' + str(countName)
# print 'both: ' + str(both)
# print 'total: ' + str(total)

#Initializes facebook API

import facebook

graph = facebook.GraphAPI(access_token='EAACEdEose0cBALJN3IW2dyHM8lqKF5vLs5rW2TgBDVMdV5stHV43oPjaIBeUZC6Kd61bA6YdBk0ZChniWTaJZAK5ScrkBG0gllThUZAm0icEk5oZCCvwzKpMWQartQ10s0UKfewLEb3RwoXEwy9iSGqlJ1AdZAhbefuqspVSkHzAZDZD', version='2.8')

org_fb_info = []

#Creates search results for groups with no id
for row in groups:
    if row[3] != '':
        if row[2] == 'group':
            try:
                data = graph.request('/search?q='+row[3] + '&type=group')
                group = data[data.keys()[1]][0] #first search result
                print "Adding Group: " + str(group['name'])
                org_fb_infofind.append([group['name'], group['id'],'Group', group['privacy']])
            except IndexError, UnicodeEncodeError:
                print "No Group Search Results"
        else:
            try:
                data = graph.request('/search?q='+row[3] + '&type=page')
                page = data[data.keys()[1]][0] #first search result
                print "Adding Page: " + str(page['name'])
                org_fb_info.append([page['name'], page['id'], 'Page'])
            except IndexError, UnicodeEncodeError:
                print "No Page Search Results"


#Identifies group privacy setting and pulls group description

# for row in groups:
#     try:
#         group = graph.get_object(row[4])
#         print group
#         if 'privacy' in group and group['privacy'] == 'OPEN':
#             group = graph.get_object(row[4], fields='description')
#             print group['description']
#     except facebook.GraphAPIError:
#         print "Graph API Error on ID: " + row[4]





