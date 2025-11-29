def is_eligible_for_discount (age,is_student):
    #if age  < 18:
       # print('eligible for discount' )
    #elif is_student is True :
        #print('eligible for discount')
    #else:
        #print('not eligible for discount')
        eligibility= age <18 or is_student 
        print (f'discount eligibility{eligibility}')

is_eligible_for_discount(15,False)