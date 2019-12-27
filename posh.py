def consec(n):
    count = 0
    for x in range(n // 2 + 1):
        if 2 * x + 1 == n:
            count += 1
    return count

print(consec(15))