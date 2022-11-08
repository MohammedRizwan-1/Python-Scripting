import os
import csv

#Path to collect file from resources Folder
budget_csv = os.path.join('PyBank', 'Resources','budget_data.csv')

#Read CSV convert data into list of Dictionairies
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    