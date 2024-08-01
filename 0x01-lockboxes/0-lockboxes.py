#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ a method that determines
    if all the boxes can be opened
    """
    if not boxes:
        return False

    n = len(boxes)
    opened = set()
    to_open = [0]

    while to_open:
        current_box = to_open.pop()
        if current_box not in opened:
            opened.add(current_box)
            for key in boxes[current_box]:
                if key < n and key not in opened:
                    to_open.append(key)
    return len(opened) == n
