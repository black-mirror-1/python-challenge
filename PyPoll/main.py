import os
import csv

electionDataCsvFile = os.path.join(os.path.dirname(__file__),"Resources","election_data.csv")

def generateElectionResults(electionDataCsvFile):
    with open(electionDataCsvFile,newline='') as electionDataCsv:
        electionDataReader = csv.reader(electionDataCsv,delimiter=',')
        if csv.Sniffer().has_header(open(electionDataCsvFile).read(1024)):
            csv_header = next(electionDataReader)
        voteCounts = {}
        totalVotes = 0
        for row in electionDataReader:
            totalVotes = totalVotes + 1
            if row[2] in voteCounts.keys():
                voteCounts[row[2]] = voteCounts[row[2]]+1
            else:
                voteCounts[row[2]] = 1
        # print(voteCounts)
    print("-------------------------")
    print("Election Results")
    print("-------------------------")
    print("Total Votes: {}".format(totalVotes))
    print("-------------------------")
    for key, value in voteCounts.items():
        print("{}: {}% ({})".format(key,round((value/totalVotes)*100,3),value))
    print("-------------------------")
    print("Winner: {}".format(max(voteCounts, key=voteCounts.get)))
    print("-------------------------")
    # print output to a file
    with open('output.txt', 'w') as f:
        print("-------------------------", file=f)
        print("Election Results", file=f)
        print("-------------------------", file=f)
        print("Total Votes: {}".format(totalVotes), file=f)
        print("-------------------------", file=f)
        for key, value in voteCounts.items():
            print("{}: {}% ({})".format(key,round((value/totalVotes)*100,3),value), file=f)
        print("-------------------------", file=f)
        print("Winner: {}".format(max(voteCounts, key=voteCounts.get)), file=f)
        print("-------------------------", file=f)

generateElectionResults(electionDataCsvFile)