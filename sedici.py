for n in range(100000000, 1000000000):
    # Progress
    # if not n % 10000000:
    #     print(n)
    if "0" in str(n):
        continue
    if len(set(str(n))) < 9:
        continue
    if n % 11:
        continue
    print(n)
    break
