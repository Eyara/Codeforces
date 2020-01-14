import sys
# 10 - number of rooms
room_state = list(''.join('0' * 10))
length = int(sys.stdin.readline())
room_actions = sys.stdin.readline()[:-1]

for action in room_actions:
    if action in ('L', 'R'):
        if action == 'R':
            room_state = room_state[::-1]
        for i in range(length):
            if room_state[i] == '0':
                room_state[i] = '1'
                break
        if action == 'R':
            room_state = room_state[::-1]
    else:
        room_state[int(action)] = '0'
room_state = "".join(room_state)
print(room_state)