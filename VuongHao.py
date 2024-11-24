def phu(x):
    if x[0] == '-':
        return x[1:]
    else:
        return '-' + x

def chuyenve(dong):
    vetrai = dong[1]
    vephai = dong[2]

    for v in vetrai[:]:
        if v and 'v' not in v:
            if v[0] == '-':
                vetrai.remove(v)
                vephai.append(phu(v))

    for v in vephai[:]:
        if v and '^' not in v:
            if v[0] == '-':
                vephai.remove(v)
                vetrai.append(phu(v))

    return [dong[0], vetrai, vephai]

def tach(tap, phep):
    res1 = tap.copy()
    res2 = tap.copy()

    for i in range(len(tap)):
        if phep in tap[i]:
            for j in range(len(tap[i])):
                if phep == tap[i][j]:
                    res1[i] = tap[i][:j]
                    res2[i] = tap[i][j+1:]
                    return res1, res2

def showTach(dong, dong1, dong2):
    print('ta tach dong {} thanh dong {} va dong {}'.format(dong[0], dong1[0], dong2[0]))
    print('{}. {} => {}'.format(dong1[0], ','.join(dong1[1]), ','.join(dong1[2])))
    print('{}. {} => {}'.format(dong2[0], ','.join(dong2[1]), ','.join(dong2[2])))

def chungminh(dong):
    vetrai = dong[1]
    vephai = dong[2]
    a = set(vephai) & set(vetrai)
    if a:
        print('{}. {} => {} Menh de duoc chung minh vi co chung {}'.format(dong[0], ','.join(vetrai), ','.join(vephai), a))
        return 0
    for v in vetrai:
        if 'v' in v:
            return 1
    for v in vephai:
        if '^' in v:
            return 2
    print('{}. {} => {} Menh de khong duoc chung minh vi co chung {}'.format(dong[0], ','.join(vetrai), ','.join(vephai), a))
    return 3

def VuongHao(GT, KL):
    GT = GT.split(',')
    KL = KL.split(',')
    dict = []
    dong = chuyenve(['1', GT, KL])
    dict.append(dong)
    print('Ta co: {}. {} => {}'.format(dong[0], ','.join(dong[1]), ','.join(dong[2])))

    while dict:
        duyet = dict.pop()
        tam = chungminh(duyet)
        if tam == 0:
            continue
        if tam == 3:
            return False
        if tam == 1:
            tt1, tt2 = tach(duyet[1], 'v')
            dong1 = [duyet[0] + '.1', tt1, duyet[2]]
            dong2 = [duyet[0] + '.2', tt2, duyet[2]]
        if tam == 2:
            tt1, tt2 = tach(duyet[2], '^')
            dong1 = [duyet[0] + '.1', duyet[1], tt1]
            dong2 = [duyet[0] + '.2', duyet[1], tt2]

        showTach(duyet, dong1, dong2)
        dict.extend([chuyenve(dong1), chuyenve(dong2)])

    print("Tat ca cac dong duoc chung minh")
    print("Vay bai toan duoc chung min")
    return True

# Test the function with sample data
GT = "-av-bvc,-gvd,-cvd,a,b"
KL = 'd'

VuongHao(GT, KL)
