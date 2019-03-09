import csv
years = []
scores = []
with open ('przykladowy.csv','r') as f:
        czytacz = csv.DictReader(f)
        for line in czytacz:
                year1 = line['Year']
                score1 = line['Score']
                years.append (int(year1))
                scores.append (int(score1))

min_score = scores[0]
min_score_rok = years[0]
max_score = scores[0]
max_score_year = years[0]
for my_year, my_score in zip(years, scores):
        print("In year ",my_year, "score was ",my_score)
        
        if min_score > my_score:
                min_score = my_score
                min_score_rok = my_year

        if max_score < my_score:
                max_score = my_score
                max_score_year = my_year 

sum_score = 0
for my_score in scores:
        sum_score += my_score
avr_score = sum_score/len(scores)             
print(years)
print(scores)
print(min_score, min_score_rok) 
print(max_score, max_score_year)
print(avr_score)
# wiersz = OrderedDict
#print(min_year)
#print(min_score)
