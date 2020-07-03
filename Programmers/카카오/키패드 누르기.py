#include <string>
#include <vector>
#include<map>
#include<cmath>

using namespace std;
string solution(vector<int> numbers, string hand) {
    string answer = "";
    map<int,pair<int,int>> dir;
    int y=0, x=0;
    for(int i=1; i<=9;i++)
    {
        dir[i] = make_pair(int(y++/3), x++%3);
    }
    dir[0] = make_pair(3,1);
    dir['*'] =make_pair(3,0);
    dir['#'] = make_pair(3,2);
    
    //오,왼손의 현위치
    int cur_r[2] ={3,2};
    int cur_l[2] = {3,0};
    for(auto n:numbers)
    {
        if(n==3 || n==6 || n==9)
        {
            answer+="R";
            cur_r[0] = dir[n].first;
                    cur_r[1] = dir[n].second;
        }
        else if(n==1 || n==4 || n==7)
        {
            answer+="L";
            cur_l[0] = dir[n].first ;
                cur_l[1] = dir[n].second;
        }
        else
        {
            int target[2];
            target[0] = dir[n].first;
            target[1] = dir[n].second;
            
            int left= abs(cur_l[0]-target[0]) + abs(cur_l[1]-target[1]);
            int right= abs(cur_r[0]-target[0]) + abs(cur_r[1]-target[1]);
            if (left >right)
            {
               cur_r[0] = dir[n].first;
                    cur_r[1] = dir[n].second;; 
                answer+='R';
            }
            else if(right>left)
            {
               cur_l[0] = dir[n].first ;
                cur_l[1] = dir[n].second;
                answer+='L';
            }
            else
            {
                if(hand=="right")
                {
                    cur_r[0] = dir[n].first;
                    cur_r[1] = dir[n].second;
                    answer += 'R';
                    }
                else
                {
                    cur_l[0] = dir[n].first ;
                    cur_l[1] = dir[n].second;
                    answer+='L';
                }    
            }
        }
    }
    return answer;
}