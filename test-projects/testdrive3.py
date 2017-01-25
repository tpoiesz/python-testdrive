rooms = {
    'Living room':
        {'description': 'This is the living room',
            'left': 'Kitchen', 'right': 'Hall', 'up': 'Balcony'},
    'Kitchen':
        {'description': 'This is the kitchen', 'right': 'Living room'},
    'Bathroom':
        {'description': "You can take a shower here, in the bathroom",
            'down': 'Living room', 'right': 'Bedroom'},
    'Bedroom':
        {'description': "This is the bedroom, you can sleep here",
            'down': 'Hall', 'left': 'Bathroom'},
    'Hall':
        {'description': "You are in the hall",
            'left': 'Living room', 'up': 'Bedroom'}
}

room = rooms['Hall']
active = True
question = 'Where do you want to go?\n'
while active:
    print(room['description'])
    direction = input(question)
    if direction == 'quit':
        active = False
    elif direction in room:
        room = rooms[room[direction]]
    else:
        print('You cannot go there!')
