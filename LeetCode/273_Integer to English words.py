'''
273. Integer to English Words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.
Example 1:
Input: 123
Output: "One Hundred Twenty Three"

Example 2:
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''

#28 ms	13.6 MB
class Solution:
    def __init__(self):
        self.result = []
        self.dic_num = {'0':'','1':'One', '2':'Two', '3':'Three', '4':'Four','5':'Five',
                   '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine',
                   '10':'Ten', '11':'Eleven', '12':'Twelve', '13':'Thirteen',
                   '14':'Fourteen', '15':'Fifteen','16':'Sixteen', '17':'Seventeen',
                   '18':'Eighteen', '19':'Nineteen',
                   '20':'Twenty', '30':'Thirty', '40':'Forty',
                   '50':'Fifty', '60':'Sixty', '70':'Seventy', '80':'Eighty',
                   '90':'Ninety', '100':'Hundred', '1000':'Thousand',
                   '1000000':'Million', '1000000000':'Billion'}
      
    def to_string(self,target, zero_c,stat):#stat은 0이 아닌 숫자이지만 단위가 출력되는걸 방지하기위함
        if len(target) == 0 or zero_c < 0:
            return
        if zero_c % 3 == 0:  #단위 붙이기
            zero = '0' * zero_c
            if zero == '':
                if target[0] != '0':
                    self.result.append(self.dic_num[target[0]])
                    stat = False
            else:
                if target[0] != '0':
                    self.result.append(self.dic_num[target[0]])
                    stat = False
                
                if stat^1: #
                    self.result.append(self.dic_num['1' + zero])
                    stat=True
                

        elif zero_c % 3 == 1:
            if target[0] == '1': #10~19는 한자리씩 끊어서 넣지 못하므로
                self.result.append(self.dic_num[target[:2]])
                target=target[0]+'0'+target[2:]  #이미 target[0]과 합쳐서 result에 넣었으니 target[1] -> '0'
                stat = False
            else:
                if target[0] != '0':
                    self.result.append(self.dic_num[target[0] + '0'])
                    stat = False

        else:
            if target[0] != '0':
                self.result.append(self.dic_num[target[0]])
                self.result.append(self.dic_num['100'])
                stat = False
        #print(target, zero_c, stat, self.result)
        return self.to_string(target[1:], zero_c - 1,stat)
    
    def numberToWords(self, num: int) -> str:
        num = str(num)
        if num =='0':
            return 'Zero'
        self.to_string(num, len(num)-1,False)
        return' '.join(self.result)