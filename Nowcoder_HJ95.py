while True:
    try:
        pref = "人民币"
        s =""
        integ, decim = map(str, input().split("."))
        yuan = ''
        if integ != '0': yuan = '元'
        num_dic = {'0':'零', '1':'壹', '2':'贰', '3':'叁', '4':'肆', '5':'伍', '6':'陆', \
                '7':'柒', '8':'捌', '9':'玖'}
        unit_dic = ["", "拾", "佰", "仟", "万", "拾", "佰", "仟", "亿", "拾",\
        "佰", "仟", "万", "拾", "佰", "仟","万" ]
        for i in range(len(integ)):
            if int(integ[i]) != 0: ##该位不是0，应带单位
                if i > 0 and integ[i-1]=='0':
                    s += num_dic['0']
                s += num_dic[integ[i]]
                s += unit_dic[len(integ)-int(i)-1]
            else: ##该位是0，则不读，但是在万亿位时应输出单位
                if (len(integ) - int(i) -1)%4 == 0:
                    num_yi = (len(integ) - int(i) -1)//8
                    num_wan = ((len(integ) - int(i) -1)%8)//4
                    s += unit_dic[8] * num_yi + unit_dic[4] * num_wan
            if s.startswith("壹拾"):
                s = s[1:]
        zheng, jiao, fen = '', '', ''
        if decim == '00':
            zheng = '整'
        else:
            jiao = num_dic[decim[0]] + '角' if decim[0] != '0' else ''
            fen = num_dic[decim[1]] + '分' if decim[1] != '0' else ''
        if integ == '0' and decim == '00':
            print(pref+'零元' + zheng)

        else:
            print(pref + s + yuan + zheng+ jiao + fen)
    except: break