for n in range(0, 5001):
    if (n-1) % 2:
        continue
    if (n-3) % 3:
        continue
    if (n-5) % 4:
        continue
    if (n-7) % 5:
        continue
    if (n-9) % 6:
        continue
    if (n-11) % 7:
        continue
    if (n-13) % 8:
        continue
    if (n-15) % 9:
        continue
    if (n-17) % 10:
        continue
    print(n)
    break
