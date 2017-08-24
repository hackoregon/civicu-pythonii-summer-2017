def distance(a, b):
    if len(a) != len(b): raise ValueError()
    count = 0
    for i, v in enumerate(a):
        if v != b[i]:
            count += 1
    return count
