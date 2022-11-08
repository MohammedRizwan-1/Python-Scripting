import os
import csv

#Path to collect file from resources Folder
budget_csv = os.path.join('PyBank', 'Resources','budget_data.csv')

#Read CSV convert data into list of Dictionairies
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip title row in csv file & Create Variables
    next(csvreader)
    prof_loss = []
    date = []

    # Loop to Calculate Total Revenue and Total Months
    for row in csvreader:
        prof_loss.append(float(row[1]))
        date.append(row[0])

    




    