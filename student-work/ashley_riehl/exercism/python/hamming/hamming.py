def distance(a, b):
    if len(a) != len(b): raise ValueError()
    count = 0
    for i, v in enumerate(a): #could zip instead
        if v != b[i]:
            count += 1
    return count
