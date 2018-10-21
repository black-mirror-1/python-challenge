import os
import csv

budgetDataCsvFile = os.path.join(os.path.dirname(__file__),"Resources","budget_data.csv")

def budgetDataReportV1(budgetDataCsvFile):
    with open(budgetDataCsvFile,newline='') as budgetDataCsv:
        budgetDataReader = csv.reader(budgetDataCsv, delimiter=',')
        indexProfitLoss = 1
        if csv.Sniffer().has_header(open(budgetDataCsvFile).read(1024)):
            csv_header = next(budgetDataReader)
            indexProfitLoss = csv_header.index('Profit/Losses')
        profitLossList = []
        months = []
        for row in budgetDataReader:
            months.append(row[0])
            profitLossList.append(int(row[indexProfitLoss]))
        print("-------------------------------------")
        print("Financial Analysis")
        print("-------------------------------------")
        print("Total Months: {}".format(len(months)))
        print("Total: ${}".format(sum(profitLossList)))
        print("Average  Change: ${}".format(round(float(sum(profitLossList))/float(len(profitLossList)),2)))
        print("Greatest Increase in Profits: {} (${})".format(months[profitLossList.index(max(profitLossList))],max(profitLossList)))
        print("Greatest Decrease in Profits: {} (${})".format(months[profitLossList.index(min(profitLossList))],min(profitLossList)))

def budgetDataReportV2(budgetDataCsvFile):
    with open(budgetDataCsvFile,newline='') as budgetDataCsv:
        budgetDataReader = csv.reader(budgetDataCsv, delimiter=',')
        indexProfitLoss = 1
        if csv.Sniffer().has_header(open(budgetDataCsvFile).read(1024)):
            csv_header = next(budgetDataReader)
            indexProfitLoss = csv_header.index('Profit/Losses')
        totalMonths = 0
        totalRev = 0.0
        avgChange = 0.0
        greatestIncreaseInProfits = None
        greatestDecreaseInProfits = None
        greatestIncreaseInProfitsMonth = 0
        greatestDecreaseInProfitsMonth = 0
        for row in budgetDataReader:
            totalMonths = totalMonths+1
            totalRev = totalRev+int(row[1])
            if not greatestIncreaseInProfits or greatestIncreaseInProfits < int(row[1]):
                greatestIncreaseInProfits = int(row[indexProfitLoss])
                greatestIncreaseInProfitsMonth = row[0]
            if not greatestDecreaseInProfits or greatestDecreaseInProfits > int(row[1]):
                greatestDecreaseInProfits = int(row[indexProfitLoss])
                greatestDecreaseInProfitsMonth = row[0]
        avgChange = totalRev/totalMonths
        print("-------------------------------------")
        print("Financial Analysis")
        print("-------------------------------------")
        print("Total Months: {}".format(totalMonths))
        print("Total: ${}".format(totalRev))
        print("Average  Change: ${}".format(round(avgChange,2)))
        print("Greatest Increase in Profits: {} (${})".format(greatestIncreaseInProfitsMonth,greatestIncreaseInProfits))
        print("Greatest Decrease in Profits: {} (${})".format(greatestDecreaseInProfitsMonth,greatestDecreaseInProfits))


# Call both methods
budgetDataReportV1(budgetDataCsvFile)
budgetDataReportV2(budgetDataCsvFile)
