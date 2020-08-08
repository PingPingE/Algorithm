#include <string>
#include <vector>
#include<queue>
using namespace std;
int dy[4]= {-1,1,0,0};
int dx[4]= {0,0,-1,1};
const int INF = 9876543;
int solution(vector<vector<int>> board) {
    int N = board.size();
    for(int i=0;i<N; i++)
    {
        for(int j=0; j<N; j++)
        {
            if(board[i][j] == 1)
                board[i][j] = -1;
            else
                board[i][j] = INF;
        }
    }
    board[0][0] = 0;
    priority_queue<vector<int>> que;
    que.push({0,0,0,-1});
    while(!que.empty())
    {
        int cur_cost = que.top()[0];
        int r = que.top()[1];
        int c = que.top()[2];
        int cur_dir = que.top()[3];
        que.pop();
        for(int d=0; d<4; d++)
        {
            int nr = r+dy[d];
            int nc = c+dx[d];
            int cost = cur_cost+100;
            if(nr<0 || nc<0 || nr>=N || nc>=N || board[nr][nc] == -1)
                continue;
            if(((cur_dir==0 || cur_dir==1)&&(d==2||d==3) )||((cur_dir ==2 || cur_dir ==3) &&(d==1 || d==0)))
                cost+=500;
            if(cost <= board[nr][nc])
            {
                board[nr][nc] = cost;
                que.push({cost,nr,nc,d});
            }                
        }
    }
    return board[N-1][N-1];
}
/*

정확성  테스트
테스트 1 〉	통과 (0.00ms, 3.84MB)
테스트 2 〉	통과 (0.00ms, 3.75MB)
테스트 3 〉	통과 (0.00ms, 3.91MB)
테스트 4 〉	통과 (0.01ms, 3.76MB)
테스트 5 〉	통과 (0.01ms, 3.92MB)
테스트 6 〉	통과 (0.29ms, 3.9MB)
테스트 7 〉	통과 (0.33ms, 3.79MB)
테스트 8 〉	통과 (0.29ms, 3.8MB)
테스트 9 〉	통과 (0.29ms, 3.78MB)
테스트 10 〉	통과 (7.81ms, 3.8MB)
테스트 11 〉	통과 (30.32ms, 3.86MB)
테스트 12 〉	통과 (42.74ms, 3.88MB)
테스트 13 〉	통과 (0.03ms, 3.77MB)
테스트 14 〉	통과 (0.07ms, 3.89MB)
테스트 15 〉	통과 (1.38ms, 3.93MB)
테스트 16 〉	통과 (3.18ms, 3.79MB)
테스트 17 〉	통과 (3.81ms, 3.8MB)
테스트 18 〉	통과 (11.91ms, 3.89MB)
테스트 19 〉	통과 (27.98ms, 3.77MB)
테스트 20 〉	통과 (0.05ms, 3.85MB)
테스트 21 〉	통과 (0.04ms, 3.84MB)
테스트 22 〉	통과 (0.01ms, 3.76MB)
테스트 23 〉	통과 (0.01ms, 3.92MB)
*/