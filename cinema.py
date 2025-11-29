# ticketB ={
#     'desmal':'12l',
#     'clinton':'11r',
#     'milton':'2l',
#     'cynthia':'13r'
# }

#ticketB.pop('desmal')
#del ticketB['clinton']
#for k in ticketB.keys():
#for v in ticketB.values():
#for k,v in ticketB.items():
# ticketB ['mary'] = '3r'

tickets = {
    'A1': 'Alice',
    'A2': 'Kimani',
    'A3': 'Winnie',
}

seat = input('Enter the seat number: ')
if tickets.get(seat):
    print(f"Ticket ({seat}) is already booked by {tickets[seat]}")
else:
    print("Seat is available")