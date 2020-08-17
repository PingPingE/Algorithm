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


def to_string(target, zero_c, stat):  # stat은 0이 아닌 숫자이지만 단위가 출력되는걸 방지하기위함
    if len(target) == 0 or zero_c < 0:
        return
    #3개씩 끊어서 보기
    if zero_c % 3 == 0: #1000의 자리까지 봐야하는 경우: 단위 붙이기
        zero = '0' * zero_c
        if zero == '':
            if target[0] != '0':
                result.append(dic_num[target[0]])
                stat = False
        else:
            if target[0] != '0':
                result.append(dic_num[target[0]])
                stat = False

            # 1,000,000의 경우 -> one million 먼저 넣고(stat = True) /  0,000 -> 여기서 이쪽으로 들어오게 된다.
            # 위 if문에서 '0'이 아닌 경우는 stat=False로 바꾸어 밑 if문에 들어가게 되는데
            # 0,000의 경우, 범위를 한번 더 출력할 필요가 없으므로 지나친다.

            if stat ^ 1:
                result.append(dic_num['1' + zero])
                stat = True

    elif zero_c % 3 == 1: #십의 자리 까지 봐야하는 경우
        if target[0] == '1':  # 10~19는 한자리씩 끊어서 넣지 못하므로
            result.append(dic_num[target[:2]])
            target = target[0] + '0' + target[2:]  # 이미 target[0]과 합쳐서 result에 넣었으니 target[1] -> '0'
            stat = False
        else:
            if target[0] != '0':
                result.append(dic_num[target[0] + '0'])
                stat = False

    else:#백의 자리 까지 봐야하는 경우
        if target[0] != '0':
            result.append(dic_num[target[0]])
            result.append(dic_num['100'])
            stat = False

    return to_string(target[1:], zero_c - 1, stat)

N = input()
zero_c= len(N)-1
if N == '0':
    print('zero')
else:
    result =[]
    to_string(N[:], zero_c,False)
    print(' '.join(result))

'''
테스트)
123400
one hundred twenty three thousand four hundred

120090
one hundred twenty thousand ninety

1000000
one million

1010101
one million ten thousand one hundred one

1234567
one million two hundred thirty four thousand five hundred sixty seven

100000
one hundred thousand

'''