def read_polynom():
    n = int(input())
    p = {}
    for i in range(n):
        L = input().split()
        Pi = int(L[0])
        Ci = int(L[1])
        p[Pi] = Ci
    return p


def add_polynomilas(p, q):
    r = {}
    Pis = set(p).union(q)
    for Pi in Pis:
        if Pi in p:
            Ci = p[Pi]
        else:
            Ci = 0.0
        if Pi in q:
            Ci += q[Pi]
        if Ci != 0.0:
            r[Pi] = Ci
    # print (r)
    return r
def tostring_polynom(p):
    if (p == {}):
        print ('0')
    res = ''
    first = True
    for Pi in sorted(p, reverse=True):
        Ci = p[Pi]
        if first:
            if Ci == 0 and Pi == 0:
                res = '0'
            if Ci == 1 and Pi != 0:
                pass
            elif Ci == -1 and Pi != 0:
                res = '-'
            else:           
                res = f'{int(Ci)}'
            first = False
            
        else:        
            if Ci > 0:
                res += ' + '
            elif Ci < 0:
                res += ' - '
            else:
                continue
            if (abs(Ci) == 1 and Pi != 0):
                pass
            else:
                res += f'{int(abs(Ci))}'
            # print (res)
        
        if Pi == 0:
            continue
        if Pi == 1:
            res += 'x'
        else:
            res += f'x^{Pi}'
    return res

p = read_polynom()
q = read_polynom()
r = add_polynomilas(p, q)
print(f'{tostring_polynom(r)}')
