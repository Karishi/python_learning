def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    if ax1 < bx2 and ax2 > bx1 and ay1 < by2 and ay2 > by1:
        overlap = (min(bx2, ax2) - max(bx1, ax1)) * (min(by2, ay2) - max(by1, ay1))
    else:
        overlap = 0
    return abs(ax1-ax2) * abs(ay1-ay2) + abs(bx1-bx2) * abs(by1-by2) - overlap

ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2
print(computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))