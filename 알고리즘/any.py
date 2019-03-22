def maxProfit(stock): #주식에서 가장 큰 이윤 얻기
    mini = 0 #가장 낮을때
    profit =  stock[len(stock)-1]-stock[mini] #이윤 초기화(마지막값-처음값)

    for i in range(1,len(stock)-1): #인덱스 1 부터 마지막-1 까지 (살 수 있는 범위)
        if stock[mini] > stock[i]: #작은 값 찾기
            mini = i
    for j in range(mini+1,len(stock)-1): #mini+1부터 팔면 가장 이윤이 클 시기찾기
        if stock[j]-stock[mini]>profit:
            profit = stock[j]-stock[mini]

    return profit #가장 큰 이윤 리턴
        
        
stock = [10300, 9600, 9800,8200, 7800, 8300, 9500,9800,10200, 9500]
print(maxProfit(stock))

#사각나선 그리기
import turtle as t

def draw(size): 
    if  size <3: #재귀호출 종료 조건
        return 
    t.forward(size) #선 긋기
    t.right(90) #90도 오른쪽으로 회전 (초기방향: ->)
    draw(size-3)#재귀호출(간격은 3만큼)
        
draw(100)
t.hideturtle()

        
        
        
        
