#import modules and csv file
import os
import csv

#counter used for counting candidates names
from collections import Counter

#file path for csv
election_data = os.path.join( 'Resources', 'election_data.csv')

#open and read csv 
with open(election_data, 'r') as file:

  #loop through the data     
  for row in file: 
  
    #creating reference for votes to count from "Candidates" row indexed from file (counter method inspir by stu_resume_analysis activity)
    candidate_votes =[row[2] for row in csv.reader(file)]

    # use counter tool to count the votes for each candidate and store it in a "counter" dictionary (reference docs.pytohn.org 8.3 collections for methodology)
    candidate_vote_count = Counter(candidate_votes) 

    #finds the candidate with the most votes (reference methodolgy "geeksforgeeks.org")
    max_candidate_vote_count = max(candidate_vote_count.values())

    #establishes candidate winner's name using key value from candidate with most votes and store in a list (reference "geeksforgeeks.org")
    first = [win for win in candidate_vote_count.keys() if candidate_vote_count[win]==  max_candidate_vote_count]

    #calculate total number of votes cast(reference docs.pytohn.org 8.3 collections for methodology)
    total_votes = sum(candidate_vote_count.values())

    #make results of counter of candidate votes into a regular dictionary(reference docs.pytohn.org 8.3 collections for methodology)
    dict_candidate_vote_count = dict(candidate_vote_count)

#print script for election results header                                
print("Election Results")

#print formatting
print("---------------------------------------")

#print total votes cast
print(f"Total Votes: {total_votes}")

#print formatting
print("---------------------------------------")

#create variable to reference the keys from the regular dictionary(used reference info from compciv.org)
for key in dict_candidate_vote_count:

  #create varible to reference the values from the regular dictionary(used reference info from compciv.org)
  val = dict_candidate_vote_count[key]

  #calculate rounded percent of votes won for each candidate using the values variable created 
  percent = round(val / total_votes *100, 3)

  #print the candidates with percent of votes won and total votes for each candidate
  print(key , ':', percent, '%', '(',val,')' )

#print formatting 
print("---------------------------------------")

#print the winner of the election (reference methodolgy "geeksforgeeks.org")
print(f"Winner: {sorted(first)[0]}")

#print formatting
print("---------------------------------------")

 #output_pypoll = os.path.join('analysis', "main.txt")
 #with open(output_pypoll, "w") as txt.file:

  