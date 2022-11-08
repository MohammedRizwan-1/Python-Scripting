#Importing Dependancies
import os
import csv

# Variable to load data file from path.
election_csv = os.path.join('PyPoll', 'Resources','election_data.csv')

#Read CSV 
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skipping first row (headers)
    next(csvreader)
    
    # Variables as List 
    Total_Votes = 0
    # Dictionaries 
    Candidates = []
    Winner = []
    Candidates_Votes = {}

    # Election Winner
    Win_Candidate = ""
    Win_count  = 0 
    Win_Perc = 0

    # For each Row in File: 
    #for row in csvreader:
       # Total_Votes += 1
   # print("Total Votes: ", Total_Votes) 

    # Loop To Calculate Candidates Votes
    for row in csvreader:
        # Adding to Entire Voting Count
        Total_Votes += 1
        # Collect candidate name from each row.
        Candidate_Name = row[2]

        #If Candidate Name not in Candidate List
        if Candidate_Name not in Candidates:
            # Add Candidates Name to the list
            Candidates.append(Candidate_Name)
            # Count votes for new candidate.
            Candidates_Votes[Candidate_Name] = 0
        # For Candidates already in list 
        Candidates_Votes[Candidate_Name] += 1
           
#   Output File Path
    output_file_path = os.path.join('Pypoll', 'Analysis', "Analysis.txt")
with open(output_file_path, "w") as text_file:


     #   Print Final Results to Terminal and as Text
    Election_Results = (
            f"Election Results\n"
            f"---------------------\n"
            f"Total Votes: {Total_Votes}\n"
            f"---------------------\n")
    
    print(Election_Results)
    #   Save to text file 
    text_file.write(Election_Results)

    # Retreiving Candidate Voting Information for each candidate
    for Candidate_Name in Candidates_Votes:
    #   Votes for said candidate
        Votes = Candidates_Votes[Candidate_Name]
    #   Percentage of votes for candidate
        Vote_percentage = round(float(Votes) / float(Total_Votes) * 100, 2)
    #   Candidate Results
        Candidate_Results = (f"{Candidate_Name}: {Vote_percentage}% ({Votes})\n")
        print(Candidate_Results)
        text_file.write(Candidate_Results)
    
    #Determining the winner 
        if (Votes > Win_count) and (Vote_percentage > Win_Perc):
            Win_count = Votes
            Win_Candidate = Candidate_Name
    
    Election_Winner = (
        f"-----------------------\n"
        f"Winner: {Win_Candidate}\n"
        f"-----------------------\n")
    print(Election_Winner)
    text_file.write(Election_Winner)



  
    

        

        






