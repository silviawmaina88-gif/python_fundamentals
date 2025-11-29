word=input("enter a word:").strip()
letter_count=input("enter the letter you want to count:").strip()
if len(letter_count) != 1: # check if the letter is a single character
    print("please enter a single letter.")
else:
    count=word.lower().count(letter_count.lower()) # find no of occurence
        
print(f"the letter {letter_count} appears {count} times")