



f = {}


def bestFunction(str,features):
    x = str.split(';')
    for i in range(len(x)):
        try:
            y = str.split(';')[i].split('"')[1]
            sp = y.split("=")
            key = sp[0].split('<')[0].strip()
            if check(key,features) == True :
                val = sp[2].split('\\n')[0].strip()
                if key in f:
                    f[key] = f[key]+float(val)
                else:
                    f[key] = float(val)
        except:
            pass

    import operator
    bg = max(f.items(), key=operator.itemgetter(1))[0]
    return f,bg


def check(key,features):
    for x in features:
        if key == x :
            return True
    return False









