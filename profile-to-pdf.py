import pdfkit
import random

def outputPDF(urlList, directory):
    #Sampling 35 since some profiles spit back errors
    sample = random.sample(urlList, 35)
    i = 1
    for profile in sample:
        try:
            pdfkit.from_url(profile, directory + str(i) + 'profile.pdf')
            i += 1
        except IOError:
            print("Warning, following profile not obtained: " + profile)

directoryList = ["18women/", "50women/", "18men/", "50men/"]
splitLoc = ["50+ ladies", "18-21 men", "50+ men"]
fullList = [line.rstrip('\n') for line in open("uniquelinks.txt")]

# Split up the list into groups. Couldn't think of better way.
indSplit = []
indSplit.append(fullList.index(splitLoc[0]))

w18List = fullList[:indSplit[0]]
w18List.pop(0)

indSplit.append(fullList.index(splitLoc[1]))
w50List = fullList[indSplit[0]:indSplit[1]]
w50List.pop(0)

indSplit.append(fullList.index(splitLoc[2]))
m18List = fullList[indSplit[1]:indSplit[2]]
m18List.pop(0)

m50List = fullList[indSplit[2]:]
m50List.pop(0)

superList = [w18List, w50List, m18List, m50List]

for ind in range(0, 4):
    outputPDF(superList[ind], directoryList[ind])

