#include <string>
#include <vector>
#include<set>
#include<map>
#include<algorithm>
using namespace std;
vector<int> solution(vector<string> gems) {
	vector<int> answer;
	map<string, int> jew_map;
	set<string> jew_set;
	for (int i = 0; i < gems.size(); i++)
	{
		jew_set.insert(gems[i]);
	}
	int cnt = 0;
	for(auto i : jew_set)
	{
		jew_map[i] = cnt++;
	}
	int s = 0, e = 0;
	int total = gems.size(); //전체 보석 수
	int goal = jew_set.size(); // 보석 종류 수
	vector<int> jew_vec(goal, 0);
	int minn[2] = { 0,total };//시작인덱스, 길이
	if (goal == total)
		return {1,total};
	while (s <= e && e < total)
	{
		if (e - s >= minn[1])
		{
			jew_vec[jew_map[gems[s++]]] -= 1;
		}
		else if (*min_element(jew_vec.begin(), jew_vec.end()) > 0)
		{
			if (e - s < minn[1])
			{
				minn[0] = s;
				minn[1] = e - s;
			}
			else if (e - s == minn[1] && s < minn[0])
				minn[0] = s;
			jew_vec[jew_map[gems[s++]]] -= 1;
		}
		else {
			jew_vec[jew_map[gems[e++]]] += 1;
		}
		
	}
	return{ minn[0] + 1, minn[0] + minn[1] };
}
/*
정확성  테스트
테스트 1 〉	통과 (0.01ms, 3.77MB)
테스트 2 〉	통과 (0.03ms, 3.79MB)
테스트 3 〉	통과 (0.07ms, 3.77MB)
테스트 4 〉	통과 (0.62ms, 3.91MB)
테스트 5 〉	통과 (0.04ms, 3.82MB)
테스트 6 〉	통과 (0.15ms, 3.83MB)
테스트 7 〉	통과 (0.27ms, 3.89MB)
테스트 8 〉	통과 (0.32ms, 3.88MB)
테스트 9 〉	통과 (0.28ms, 3.82MB)
테스트 10 〉	통과 (0.75ms, 3.93MB)
테스트 11 〉	통과 (0.89ms, 3.98MB)
테스트 12 〉	통과 (0.44ms, 3.91MB)
테스트 13 〉	통과 (0.55ms, 3.92MB)
테스트 14 〉	통과 (1.68ms, 3.92MB)
테스트 15 〉	통과 (1.11ms, 3.97MB)
효율성  테스트
테스트 1 〉	통과 (1.68ms, 3.87MB)
테스트 2 〉	통과 (9.18ms, 4.22MB)
테스트 3 〉	통과 (4.71ms, 4.53MB)
테스트 4 〉	통과 (43.04ms, 5.79MB)
테스트 5 〉	통과 (15.67ms, 5.01MB)
테스트 6 〉	통과 (7.20ms, 5.27MB)
테스트 7 〉	통과 (21.12ms, 5.91MB)
테스트 8 〉	통과 (23.50ms, 6.22MB)
테스트 9 〉	통과 (13.43ms, 6.51MB)
테스트 10 〉	통과 (23.00ms, 6.83MB)
테스트 11 〉	통과 (60.08ms, 7.53MB)
테스트 12 〉	통과 (211.68ms, 9.59MB)
테스트 13 〉	통과 (288.93ms, 10.2MB)
테스트 14 〉	통과 (72.95ms, 9.94MB)
테스트 15 〉	통과 (153.82ms, 10.7MB)
*/