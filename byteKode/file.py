#Python, or similar CSV code would have been used to permanently store the user's data in an Excel spreadsheet

import csv

while(0 == 0):
    userStory = input("Share your story... ")

    file = open("Reports.csv", "a")
    file.write(userStory)
    file.write("\n")
    file.close()