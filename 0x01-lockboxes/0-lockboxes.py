#!/usr/bin/python3
""" lock boxes alx interview """


def canUnlockAll(boxes):
    """ boxes : A list of lists
    canUnlockAll function """
    result = False
    list = []
    Box = []
    index = -1
    if boxes is None:
        return False
    if len(boxes) == 1:
        return True
    for i in range(len(boxes)):
        index += 1
        if index == 0:
            for ele in boxes[i]:
                list.append(ele)
            continue
        if index > 0 and index in list:
            for ele in boxes[i]:
                list.append(ele)
            continue
        elif index in boxes[i] and len(boxes[i]) == 1:
            for ele in boxes[i]:
                list.append(ele)
            continue
        else:
            # mark the index of the box that didnt open
            Box.append(i)
    # settlethe unlocked boxes
    lel = len(Box)
    for j in range(lel):
        if len(Box) == 0:
            break
        if Box[0] in list:
            for ele in boxes[Box[0]]:
                list.append(ele)
            Box.pop(0)
    for k in range(len(Box) - 1, -1, -1):
        if len(Box) == 0:
            break
        if Box[len(Box) - 1] in list:
            for ele in boxes[Box[len(Box) - 1]]:
                list.append(ele)
            Box.pop(len(Box) - 1)
    if len(Box) > 0:
        return False
    else:
        return True
