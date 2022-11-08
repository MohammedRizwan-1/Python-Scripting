import os
import csv

#Path to collect file from resources Folder
budget_csv = os.path.join('PyBank', 'Resources','budget_data.csv')

#Read CSV convert data into list of Dictionairies
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Skip title row in csv file & Create Variables
    next(csvreader)
    prof_loss = []
    date = []
    revenue_change = []
    average_revenue_change = []
    min_prof_loss_change = []
    max_prof_loss_change = []

    # Loop to Calculate Total Revenue and Total Months
    for row in csvreader:
        prof_loss.append(float(row[1]))
        date.append(row[0])

    #Loop to Calculate Revenue Change
    for i in range(1,len(prof_loss)):

        #Total Change in Revenue
        revenue_change.append(prof_loss[i] - prof_loss[i-1])

        #Average Change in Revenue
        average_revenue_change = sum(revenue_change)/len(revenue_change)
    
        #Greatest decrease in Profit and The Date
        min_prof_loss_change = min(revenue_change)
        min_prof_loss_change_date = str(date[revenue_change.index(min(revenue_change))+1])

        #Greatest increase in Profit and The Date
        max_prof_loss_change = max(revenue_change)
        max_prof_loss_change_date = str(date[revenue_change.index(max(revenue_change))+1])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", int((sum(prof_loss))))
    print("Average Change: $", round((average_revenue_change),2))
    print("Greatest Increase in Revenue :", max_prof_loss_change_date, "($",int(max_prof_loss_change),")")
    
    print("Greatest Decrease in Revenue :", min_prof_loss_change_date, "($",int(min_prof_loss_change),")")

    #Output File as Text File 

    output_file = os.path.join('PyBank', 'Analysis', "Analysis.txt")
    with open(output_file, "w") as text_file:
         text_file.write (f"Financial Analysis\n")
         text_file.write (f"-------------------------------\n")
         text_file.write (f"Total Months: " + str(len(date)) + "\n")
         text_file.write (f"Total Revenue: " + str(int((sum(prof_loss)))) + "\n")
         text_file.write (f"Average Change:" + str(round((average_revenue_change),2)) + "\n")
         text_file.write (f"Greatest Increase in Revenue:" + str(" ") + str( max_prof_loss_change_date) + (" ")  + str("$") + str(int(max_prof_loss_change)) + "\n")
         text_file.write (f"Greatest Increase in Revenue:" + str(" ") + str( min_prof_loss_change_date) + (" ")  + str("$") + str(int(min_prof_loss_change)) + "\n")


        
    







    