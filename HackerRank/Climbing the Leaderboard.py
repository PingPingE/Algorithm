'''
An arcade game player wants to climb to the top of the leaderboard and track their ranking. 
The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

Function Description)
Complete the climbingLeaderboard function in the editor below.

climbingLeaderboard has the following parameter(s):

int ranked[n]: the leaderboard scores
int player[m]: the player's scores


Returns)

int[m]: the player's rank after each new score

'''

#!/bin/python3

import math
import os
import random
import re
import sys

def climbingLeaderboard(ranked, player):
    # Write your code here
    cur_rank = sorted(set(ranked), reverse= True)
    res = []
    for e,p in enumerate(player,1):
        #먼저 양쪽 끝단값부터 확인 후 처리
        if p >= cur_rank[0]:
            res.append(1)
        elif p == cur_rank[-1]:
            res.append(len(cur_rank))
        elif p < cur_rank[-1]:
            res.append(len(cur_rank)+1)
        else:
            #이분탐색으로 적절한 자리 찾기
            l,r= 0, len(cur_rank)
            done = set()
            stat=  False
            while l<=r and not stat:
                m = (l+r)//2
                if m in done:
                    stat = True
                else:
                    done.add(m)
                    
                if cur_rank[m] == p:
                    res.append(m+1)
                    break
                
                elif cur_rank[m] > p:
                    if stat:
                        res.append(m+2)
                        break
                    l = m+1
                    
                else:
                    if stat:
                        res.append(m+1)
                        break
                    r = m-1
            # print(l,r)
            if len(res) == e: continue
            
            #아직 순위가 정해지지 못한경우
            if cur_rank[l] < p:
                res.append(l+1)
            else:
                res.append(l+2)
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
