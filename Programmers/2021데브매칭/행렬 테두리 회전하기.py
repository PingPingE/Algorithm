'''
문제 설명)
rows x columns 크기인 행렬이 있습니다. 행렬에는 1부터 rows x columns까지의 숫자가 한 줄씩 순서대로 적혀있습니다.
이 행렬에서 직사각형 모양의 범위를 여러 번 선택해, 테두리 부분에 있는 숫자들을 시계방향으로 회전시키려 합니다. 
각 회전은 (x1, y1, x2, y2)인 정수 4개로 표현하며, 그 의미는 다음과 같습니다.

x1 행 y1 열부터 x2 행 y2 열까지의 영역에 해당하는 직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전합니다.

행렬의 세로 길이(행 개수) rows, 가로 길이(열 개수) columns, 그리고 회전들의 목록 queries가 주어질 때, 
각 회전들을 배열에 적용한 뒤, 그 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 
return 하도록 solution 함수를 완성해주세요.

제한사항)
- rows는 2 이상 100 이하인 자연수입니다.
- columns는 2 이상 100 이하인 자연수입니다.
- 처음에 행렬에는 가로 방향으로 숫자가 1부터 하나씩 증가하면서 적혀있습니다.
- 즉, 아무 회전도 하지 않았을 때, i 행 j 열에 있는 숫자는 ((i-1) x columns + j)입니다.
- queries의 행의 개수(회전의 개수)는 1 이상 10,000 이하입니다.
- queries의 각 행은 4개의 정수 [x1, y1, x2, y2]입니다.
- x1 행 y1 열부터 x2 행 y2 열까지 영역의 테두리를 시계방향으로 회전한다는 뜻입니다.
- 1 ≤ x1 < x2 ≤ rows, 1 ≤ y1 < y2 ≤ columns입니다.
- 모든 회전은 순서대로 이루어집니다.
- 예를 들어, 두 번째 회전에 대한 답은 첫 번째 회전을 실행한 다음, 그 상태에서 두 번째 회전을 실행했을 때 이동한 숫자 중 최솟값을 구하면 됩니다.
'''

def solution(rows, columns, queries):
    answer = []
    board = [list(range(n,n+columns)) for n in range(1,rows*columns+1,columns)]
    
    def rotation(x1,y1,x2,y2):
        nonlocal answer
        #이번 회전에서 이동한 숫자 중 최솟값 저장을 위한 변수 선언
        mini = 10001
        
        #갱신될 부분의 크기만큼의 배열 선언
        new_board=[[0]*(y2-y1) for _ in range(x2-x1)]
        
        #왼쪽
        for new_i,i in zip(range(x2-x1),range(x1,x2)):
            if i+1 < x2 and new_board[new_i][0]==0:
                new_board[new_i][0] = board[i+1][y1]
                mini = min(mini, board[i+1][y1])
        
        #윗쪽
        for new_j,j in zip(range(y2-y1),range(y1,y2)):
            if j-1>= y1 and new_board[0][new_j]==0:
                new_board[0][new_j] = board[x1][j-1]
                mini = min(mini,board[x1][j-1])
            
        #오른쪽
        for new_i,i in zip(range(x2-x1),range(x1,x2)):
            if i-1 >= x1 and  new_board[new_i][-1] ==0:
                new_board[new_i][-1] = board[i-1][y2-1]
                mini =min(mini,board[i-1][y2-1])
            
        #아랫쪽
        for new_j,j in zip(range(y2-y1),range(y1,y2)):
            if j+1 < y2 and new_board[-1][new_j]==0:
                new_board[-1][new_j] = board[x2-1][j+1]
                mini = min(mini,board[x2-1][j+1])
                
        #이번 회전에서 이동한 숫자 중 최솟값 추가
        answer.append(mini)   
        return new_board
    
    for x1,y1,x2,y2 in queries:
        new_board = rotation(x1-1, y1-1, x2, y2)
        
        #board 갱신
        for r,i in enumerate(range(x1-1, x2)):
            for c,j in enumerate(range(y1-1,y2)):
                if new_board[r][c]!=0:
                    board[i][j] = new_board[r][c]
    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.11ms, 10.3MB)
테스트 2 〉	통과 (0.09ms, 10.3MB)
테스트 3 〉	통과 (892.85ms, 12MB)
테스트 4 〉	통과 (382.89ms, 11.4MB)
테스트 5 〉	통과 (710.99ms, 11.7MB)
테스트 6 〉	통과 (590.65ms, 11.9MB)
테스트 7 〉	통과 (673.93ms, 12.1MB)
테스트 8 〉	통과 (402.73ms, 11.5MB)
테스트 9 〉	통과 (578.12ms, 11.9MB)
테스트 10 〉	통과 (462.79ms, 11.5MB)
테스트 11 〉	통과 (445.00ms, 11.6MB)
'''