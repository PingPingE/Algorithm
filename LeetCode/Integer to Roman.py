
'''
Seven different symbols represent Roman numerals with the following values:
Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.



Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places


Constraints:

1 <= num <= 3999
'''


class Solution:
    '''
    1. num의 1의 자리부터 올라감 -> (자릿수-1)개만큼 0 붙이기
    2. sub_num이 4 or 9로 시작하는가?
    2-1 yes: upper bound - N 중 현재 숫자와 같게 만들어주는 N 찾아서 symbol로 변환
    2-2 no: lower_bound * 나눔 몫 -> sub_num에서 해당 값을 빼주고 다시 반복(sub_num이 0이 될 때까지)
    '''

    def intToRoman(self, num: int) -> str:
        prev_num = 0
        cur_num = num
        i = 10
        ret = []

        roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

        def get_upper_bound(x):
            for n, symbol in roman.items():
                if n > x:
                    return (n, symbol)

        def get_lower_bound(x):
            prev = None
            for n, symbol in roman.items():
                if n > x:
                    return prev
                else:
                    prev = (n, symbol)

            return prev

        while prev_num < num:

            sub_num = cur_num % i - prev_num
            prev_num += sub_num

            if str(sub_num).startswith('4') or str(sub_num).startswith('9'):
                upper_num, upper_symbol = get_upper_bound(sub_num)
                for n, symbol in roman.items():
                    if upper_num - n == sub_num:
                        lower_num, lower_symbol = (n, symbol)
                        break
                    else:
                        continue
                ret.append(lower_symbol + upper_symbol)

            else:
                tmp_ret = ""
                while sub_num > 0:
                    lower_num, lower_symbol = get_lower_bound(sub_num)
                    tmp_ret += lower_symbol * (sub_num // lower_num)
                    sub_num -= lower_num * (sub_num // lower_num)

                ret.append(tmp_ret)
            i *= 10

        return ''.join(ret[::-1])

