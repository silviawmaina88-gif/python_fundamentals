cat1 = 15
cat2  = 15
avgCat = (cat1 + cat2)/2
mainExam = 50
totalMark = avgCat + mainExam
if totalMark >= 70:
    print('Grade A')
elif totalMark >= 60:
    print('Grade B')
    print('Congrats')
elif totalMark >= 50:
    print('Grade C')
elif totalMark >= 40:
    print('Grade D')
else:
    print('Failed')