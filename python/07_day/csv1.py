import csv

with open ('przykladowy.csv','r') as f:
        czytacz = csv.reader(f)
        for line in czytacz:
                print(line)
