# making a list for the cities visited
# cities=[]
# for i in range (5):
#     city= input(f'enter city visited{i+1}: ')
#     # append the city to the list
#     cities.append(city)

# print(f'you have visited:{cities}')
# cities.sort()# the sort is outside the loop
# print(f'sorted list:{cities}')

cities = []
def listCities():
    try:
        for i in range(5):
            city = input(f'Enter city {i+1}: ')
            cities.append(city)

        print(f'current list:{cities}') # check list after addition
        print(cities) # print the final list
    except ValueError:
        print('invalid input')

def addCity():
    try:
        newCity = input('Add new city: ')
        cities.append(newCity)
        print(f'You have added ({newCity}) to the list of cities')
    except ValueError:
        print('something went wrong')
def display_cities():
    if cities:
        print(f'you have visited :{cities}')


while True:
    print('==welcome==')
    print('\n1. List visited cities')   
    print('\n2. Add new city')
    print('\n3. diplay the cities')
    print('\n4. Exit application')

    option = input('Choose an option above: ')
    if option == '1':
        listCities()
    elif option == '2':
        addCity()
    elif option == '3':
        display_cities()
    elif option == '4':
       break