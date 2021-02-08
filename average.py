def average(list):
    for n in list:
        try:
            vn = n + 1
        except:
            return 0
    if len(list) > 0:
        return sum(list) / len(list)
    else:
        return 0
