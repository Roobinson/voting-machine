import csv

print("-------------------------------------------")
print("*******************************************")
print("*******************************************")
print("************* Election Machine ************")
print("*******************************************")
print("*******************************************")
print("-------------------------------------------")

first_name = input("Please enter your first name: ")
surname = input("Please enter your surname: ")
#print("Thank you for signing up,", first_name, surname, "\nPlease answer a few more questions so that we can contact you.")
post_code = input("Please enter your post code: ")
door_number = input("Please enter your door number: ")

print("-------------------------------------------")
print("* Please select a number for the party of your choice:")
print("* 1 Labour")
print("* 2 Conservatives")
print("* 3 Liberal Democrats")
print("* 4 Green")
print("* 5 Spoil ballot")
print("-------------------------------------------")

vote = input("Please enter a number for the corresponding party: ")

with open('election.csv', 'r', newline='') as csvfile:
    csv_headings = next(csvfile)
    if (csv_headings[0] == "f"):
        #if our file does start with an f (first_name), don't add fieldnames
        csvfile.close()
        file2 = open('election.csv', 'a')
        fieldnames = ['first_name', 'surname', 'post_code', 'door_number']
        writer = csv.writer(file2)
        #writer.writeheader()
        #writer.writerow({'first_name': first_name, 'surname': surname, 'post_code': post_code, 'door_number': door_number, 'vote': vote})
        writer.writerow([first_name,surname,post_code,door_number,vote])
        file2.close()
    else:
        #if our file doesn't start with an f (first_name), add fieldnames first
        #csvfile.close()
        file2 = open('election.csv', 'a')
        fieldnames = ['first_name', 'surname', 'post_code', 'door_number', 'vote']
        writer = csv.DictWriter(file2, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'first_name': first_name, 'surname': surname, 'post_code': post_code, 'door_number': door_number, 'vote': vote})
        file2.close()
#using with means we don't need to close the file

print("Thank you for voting!" )
