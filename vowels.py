text =input('enter text:')
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count+=1
    print('number of vowels:',count)
