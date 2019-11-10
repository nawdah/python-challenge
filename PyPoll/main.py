import os
import csv

total_votes = 0 
election_list = {}
results = {}
candidate_percentage = []
max_index = 0


election_path = os.path.join("c:/Users/Nada/Desktop/Data_Science_Bootcamp/Python/python-challenge/PyPoll/election_data.csv")

with open(election_path, newline='') as election_file:
    election_reader = csv.reader(election_file, delimiter=',')
    next(election_reader)
    row = next(election_reader)

    for row in election_reader:
        total_votes += 1

        if row[2] not in election_list:
            election_list[row[2]] = 0
        election_list[row[2]] = election_list[row[2]] + 1
    
        results = [{row : election_list[row]} for row in election_list]
        candidates_names = [str(k) for lst in results for k, v in lst.items()]
        candidates_votes = [int(v) for lst in results for k, v in lst.items()]
    
    max_votes = candidates_votes[0]

    for count in range(len(candidates_names)):
        percentage = candidates_votes[count]/total_votes
        candidate_percentage.append(percentage)

        if candidates_votes[count] > max_votes:
            max_votes = candidates_votes[count]
            max_index = count
        
    winner = candidates_names[max_index]

    candidate_percentage = ['{:.3%}'.format(elm) for elm in candidate_percentage]

print(f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------""")
for count in range(len(candidates_names)):
        print(f"{candidates_names[count]}: {candidate_percentage[count]} ({candidates_votes[count]})")
print(f"""
-------------------------
Winner: {winner}
------------------------- """)
with open('election_data_revised.text', 'w+') as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"-------------------------\n")
    for count in range(len(candidates_names)):
        txtfile.write(f"{candidates_names[count]}: {candidate_percentage[count]} ({candidates_votes[count]})\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write(f"-------------------------")
