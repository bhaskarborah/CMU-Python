def bigger_rectangle(x1, y1, x2, y2, x3, y3, x4, y4):
    # compare sizes, return either 1 or 2
    area1 = (x2-x1) * (y1-y2)
    area2 = (x4-x3) * (y3-y4)
    if area1 > area2:
        return 1
    elif area1 == area2:
        return "tie"
    else:
        return 2

# Needs parentheses when calculating area
# Was returning 1 and 2 in the wrong places

print(bigger_rectangle(0, 5, 6, 0, 1, 4, 2, 3))
