def phu(x):
    if x[0] == '-':
        return x[1:]
    else:
        return '-' + x

def res(a, b):
    check = False
    ans = list(set(a+b))
    for v in ans:
        if phu(v) in ans:
            ans.remove(v)
            ans.remove(phu(v))
            check = True
    return sorted(ans), check

def robinson(TAP):
    TAP = TAP.split(',')
    dict = {}
    so = 1
    for v in TAP:
        dict[so] = sorted(v.split('v'))
        so += 1
    for key, value in dict.items():
        print(key, value)

    daDuyet = set()
    for i in list(dict.keys()):
        for j in list(dict.keys())[i:]:
            if(i,j) not in daDuyet:
                tam, check = res(dict[i], dict[j])
                daDuyet.update({(i,j), (i,so), (j, so)})
                if not check:
                    continue
                if not tam:
                    print('{}. Res({}, {}) = {}'.format(so, i, j, tam))
                    print('=> bai toan duoc chung minh')
                    return True
                if tam not in dict.values():
                    print('{}. Res({}, {}) = {}'.format(so, i, j, tam))
                    dict[so] = tam
                    so += 1

    print('Chung minh that bai')
    return False

TAP="-av-bvc,-gvd,-cvd,a,b,-d"
robinson(TAP)
