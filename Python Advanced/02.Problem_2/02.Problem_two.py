players = [first_player, second_player] = input().split(', ')
matrix = [list(input().split(' ')) for _ in range(6)]
winner = ''
tom_position_path = []
jerry_position_path = []
tom_positions = 0
jerry_positions = 0
is_stop = False


def calculate_position_path(tom_path, jerry_path, r, c):
    if current_player == 'Tom':
        tom_position_path.append((r, c))
    else:
        jerry_position_path.append((r, c))
    return tom_position_path, jerry_position_path


while True:
    coordinates = eval(input())
    row = coordinates[0]
    col = coordinates[1]
    current_player = players.pop(0)
    if is_stop:
        calculate_position_path(tom_position_path, jerry_position_path, row, col)
        players.append(current_player)
        is_stop = False
        continue

    if matrix[row][col] == 'E':
        winner = current_player
        print(f'{current_player} found the Exit and wins the game!')
        calculate_position_path(tom_position_path, jerry_position_path, row, col)
        break
    elif matrix[row][col] == 'S':
        is_stop = True
        calculate_position_path(tom_position_path, jerry_position_path, row, col)
        players.append(current_player)
        continue
    elif matrix[row][col] == 'B':
        if current_player == "Tom":
            tom_positions += 1
            print(f"Tom jumped from position: ({row},{col}) back to his old position: ({tom_position_path[-1]}.")
        else:
            jerry_positions += 1
            print(f"Jerry jumped from position: ({row},{col}) back to his old position: {jerry_position_path[-1]}.")

    elif matrix[row][col] == 'O':
        if current_player == 'Tom':
            winner = 'Jerry'
        else:
            winner = 'Tom'
        print(f'{current_player} is out of the game! The winner is {winner}.')
        calculate_position_path(tom_position_path, jerry_position_path, row, col)
        break

    calculate_position_path(tom_position_path, jerry_position_path, row, col)
    players.append(current_player)

if jerry_position_path:
    print(f"Jerry's path: ")
    for p in jerry_position_path:
        print(p)
if jerry_positions:
    print(f"Jerry has changed positions: {jerry_positions} times.")
if tom_position_path:
    print("Tom's path: ")
    for p in tom_position_path:
        print(p)
if tom_positions:
    print(f"Tom has changed positions: {tom_positions} times.")