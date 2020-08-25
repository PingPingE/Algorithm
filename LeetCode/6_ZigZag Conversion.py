'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''
#1232 ms 20.8 MB
#sol1) 규칙을 찾아 구현
#변수 i(index)로 문자열 s를 모두 순회, res 2차원 list의 e자리에 값을 넣음
#연결부분(대각선)이 아닌 부분은 현위치에서(e) numRows만큼 밑으로(행++)가며 s[i]를 넣어줌
#대각선 부분은 numRows-2만큼 현위치에서 대각선으로(행--, 열++)가며 s[i]를 넣어줌  
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [['' for _ in range(len(s))] for _ in range(numRows)] 
        i,n = 0,0
        while i<len(s):
            try:
                e = 0
                for i in range(i,i+numRows): #밑으로
                    res[e][n] = s[i]
                    e+=1
                i+=1
                e-=1
                n+=1
                
                for k in range(numRows-2): #대각선
                    res[e-1][n] = s[i] 
                    i+=1
                    n+=1
                    e-=1
                
            except:
                break
        ans =[]
        for r in res:
            ans.append(''.join(r))
            
        return ''.join(ans)

#52 ms	13.9 MB
#sol2) 위와 똑같은 방식 but res가 2차원 배열이 아닌, 1차원 배열
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ['' for _ in range(numRows)] #numRows개의 행만을 가지는 list
        i=0 #열을 가리키던 변수n 필요X
        while i<len(s):
            try:
                e = 0
                for i in range(i,i+numRows): #밑으로
                    res[e] += s[i]
                    e+=1
                i+=1
                e-=1
                
                for k in range(numRows-2): #대각선
                    res[e-1] += s[i] 
                    i+=1                 
                    e-=1
                
            except:
                break
          
        return ''.join(res) #sol1처럼 ans를 따로 선언 할 필요 없고, 추가 연산 할 필요도X