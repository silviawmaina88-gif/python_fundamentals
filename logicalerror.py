# error 1:off by one error
#def print_numbers(n):
  #  """print numbers from 1 to n(intended)"""
   # for i in range(n): # bug :range(n)goes from 0 to n-1
        #print(i)

#print_numbers(5)
#output : 01234 should be(12345)
 #correction
#def print_numbers_correct(n):
 #  for i in range(1, n+1):
  #    print(i)

#print_numbers_correct(5)

#error2:wrong formula
#def calculate_circle_area(radius):
  #  """calculate the area of a circle"""
 #   return 3.14 * radius # bug: should be pi * radius^2
#area=calculate_circle_area(5)
#print(f"Area:{area :,.2f}")
# output is 15.7 (should be 78.5)
#correction
#def calculate_circle_area(radius):
  #  import math
 #   return math.pi * radius ** 2

#area=calculate_circle_area(5)
#print(f"Area:{area :,.2f}")


#error3:incorrecct condition
#def is_even(number):
    #"""check if number is even"""
   # if number % 2 == 1: #bug:this checks for odd number
  #      return True
 #   return False

#print(is_even(4))
#output:false (should be true)

#correction
#def is_even_correct(number):
   # if number % 2 == 0:
  #      return True
 #   return False

#print(is_even_correct(4))

#error4:variable scope issue
#total=0
#def add_to_total(value):
 #   """add value to total"""
  #  total=total + value # bug:unbound local error
   # return total

#print(add_to_total(6))

#corrrection
total=0
def add_to_total_correct(value):
    global total
    total=total + value
    return total

print(add_to_total_correct(9))