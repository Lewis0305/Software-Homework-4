def cube(a, b, c):
    try:
        va = int(a)
        vb = int(b)
        vc = int(c)
        if (min(va, vb, vc) > 0):
            return va * vb * vc
        else:
            return 0;
    except ValueError:
        return 0
