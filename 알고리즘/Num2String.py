'''
숫자를 문자열(영문)로 바꾸기 (백만까지만)
ex)
1->one
101 -> one hundred one
10001 -> ten thousand one
'''

dic_num = {'0':'','1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine',
           '10':'ten', '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen',
           '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen', '20':'twenty', '30':'thirty', '40':'forty',
           '50':'fifty', '60':'sixty', '70':'seventy', '80':'eighty', '90':'ninety', '100':'hundred', '1000':'thousand',
           '1000000':'million'}

def get_string(target, zero_c, stat):
    global result
    if zero_c<0:
        return
    #print(target,zero_c,result,stat)
    if target[0] == '0': #0인 경우 단위만 출력
        result.append(dic_num[f"1{'0' * (zero_c+1)}"])

    else:#단위가 dic_num에 있는지 확인하기 위해 3자리씩 끊어 보기

        if zero_c%3 ==0: #단위가 dic_num에 있는 경우
            if stat:  # 이전에 10이상 19이하를 받은 경우
                result.append(dic_num[f"1{'0' * zero_c}"])  # 단위만
                stat = False

            if len(target) > 1: #한자리 이상 남은 경우
                result.append(dic_num[target[0]] + ' ' + dic_num[f"1{'0' * zero_c}"])
            else: #한자리 남은 경우
                result.append(dic_num[target[0]])

        elif zero_c % 3 == 1: #10으로 끊는 경우
            if target[0] == '1':  # 10이상 19이하는 따로 끊을 수가 없으므로
                result.append(dic_num[target[:2]])
                stat = True  # 따로 표시
            else:
                result.append(dic_num[target[0] + '0'])
        else: #100으로 끊는 경우
            result.append(dic_num[target[0]] +' '+ dic_num['100'])
    n=1
    if stat^1:
        while n<=zero_c%3: #현재 보고 있는 범위 내에서 0인 자리 패스
            if target[n] !='0':
                break
            n+=1
        if zero_c%3 == 0 and n == 1:
            while n<len(target) and target[n] == '0':
                n+=1
    print(n, target[n:])
    return get_string(target[n:], zero_c-n,stat)

#최대 백만
N = input()
zero_c= len(N)-1
if zero_c == 0:
    if N == '0':
        print('zero')
    else:
        print(dic_num[N])
else:
    result =[]
    get_string(N[:], zero_c,False)
    print(' '.join(result))

'''
테스트)
123400
one hundred twenty three thousand four hundred

120090
one hundred twenty thousand ninety

'''