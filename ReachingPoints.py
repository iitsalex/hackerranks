import sys
from timeit import default_timer as timer


def canReach(x1, y1, x2, y2):
    sys.setrecursionlimit(x2 + y2 + 5)
    return canReachRecurse(x1, y1, x2, y2)


def canReachRecurse(x1, y1, x2, y2):
    if x1 > x2 or y1 > y2:
        return 'No'
    elif x1 == x2 and y1 == y2:
        return 'Yes'
    else:
        return max(canReachRecurse(x1 + y1, y1, x2, y2),
                   canReachRecurse(x1, y1 + x1, x2, y2))


def canReachRecurseMemo(x1, y1, x2, y2, visited):
    if x1 == x2 and y1 == y2:
        return 'Yes'
    if x1 > x2 or y1 > y2 or visited[x1][y1] == 1:
        return 'No'
    visited[x1][y1] = 1
    return max(canReachRecurseMemo(x1 + y1, y1, x2, y2, visited),
               canReachRecurseMemo(x1, y1 + x1, x2, y2, visited))


def canReachMemo(x1, y1, x2, y2):
    visited = [[0 for _ in range(y2 + 1)] for _ in range(x2 + 1)]
    sys.setrecursionlimit(y2 + x2 + 5)
    return canReachRecurseMemo(x1, y1, x2, y2, visited)


canReach(1, 4, 5, 9)

start = timer()
canReach(1, 1, 1000, 1000)
end = timer()
print(end - start)

start = timer()
canReachMemo(1, 1, 1000, 1000)
end = timer()
print(end - start)

#
# def canReach(x1, y1, x2, y2, dist=float('Inf')):
#     if x1 > x2 or y1 > y2 or (x2-x1 + y2-y1) > dist:
#         return 'No'
#     elif x1 == x2 and y1 == y2:
#         return 'Yes'
#     else:
#         return max(canReach(x1+y1, y1, x2, y2, (x2-x1 + y2-y1)),
#                    canReach(x1, y1+x1, x2, y2, (x2-x1 + y2-y1)))

# def canReach(x1, y1, x2, y2):
#     while x1 < x2 or y1 < y2:
#         if x2 > y2:
#             x2 %= y2
#         else:
#             y2 %= x2
#     if x1-x2 % y1 == 0 or y1-y2 % x1 == 0:
#         return 'Yes'
#     else:
#         return 'No'
