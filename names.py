def name(first, last):
    try:
        vfirst = str(first)
        vlast = str(last)
        if (min(len(vfirst), len(vlast)) > 0):
            return vfirst + " " + vlast
        else:
            return "";
    except ValueError:
        return ""
