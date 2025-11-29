num_of_sec =int (input('enter the nunber of seconds:'))
min=num_of_sec // 60 # for the total minutes
rem_sec= num_of_sec % 60 # for the remaining seconds
print (f'{min} minutes and {rem_sec} seconds')