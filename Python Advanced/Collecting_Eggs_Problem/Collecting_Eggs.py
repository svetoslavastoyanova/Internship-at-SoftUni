from collections import deque

eggs = deque([int(c) for c in input().split(', ')])
pieces_of_paper = list(map(int, input().split(", ")))
total_box_filled = 0
box_size = 50

while eggs:
    if not pieces_of_paper:
        break

    first_egg = eggs.popleft()
    last_piece_of_paper = pieces_of_paper[-1]

    if first_egg <= 0:
        continue

    if first_egg == 13 and len(pieces_of_paper) > 1 and eggs:
        first_paper = pieces_of_paper[0]
        last_paper = pieces_of_paper[-1]
        pieces_of_paper[-1] = first_paper
        pieces_of_paper[0] = last_paper
        continue

    if first_egg == 13 and not len(pieces_of_paper) > 1 and not eggs or \
            first_egg == 13 and len(pieces_of_paper) > 1 and not eggs:
        break

    if first_egg + last_piece_of_paper <= box_size:
        total_box_filled += 1
        pieces_of_paper.pop()


if not pieces_of_paper and eggs:
    eggs = ', '.join(list(map(str, eggs)))
    print(f"Not all eggs are collected.")
    print(f"Eggs left: {eggs}")
if not eggs and pieces_of_paper and total_box_filled > 0:
    print(f"All eggs are successfully collected!")
    print(f"Total boxes filled: {total_box_filled}")
    pieces_of_paper = ', '.join(list(map(str, pieces_of_paper)))
    print(f"Pieces of paper left: {pieces_of_paper}")
if not eggs and not pieces_of_paper and total_box_filled > 0:
    print(f"All eggs are successfully collected!")
    print(f"Total boxes filled: {total_box_filled}")
    print(f"Pieces of paper left: 0")
if total_box_filled == 0:
    print("Sorry! You couldn't fill any boxes!")
