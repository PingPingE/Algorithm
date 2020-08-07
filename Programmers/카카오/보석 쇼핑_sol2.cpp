/*
[카카오 인턴] 보석 쇼핑
문제 설명
[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]

개발자 출신으로 세계 최고의 갑부가 된 어피치는 스트레스를 받을 때면 이를 풀기 위해 오프라인 매장에 쇼핑을 하러 가곤 합니다.
어피치는 쇼핑을 할 때면 매장 진열대의 특정 범위의 물건들을 모두 싹쓸이 구매하는 습관이 있습니다.
어느 날 스트레스를 풀기 위해 보석 매장에 쇼핑을 하러 간 어피치는 이전처럼 진열대의 특정 범위의 보석을 모두 구매하되 특별히 아래 목적을 달성하고 싶었습니다.
진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매

예를 들어 아래 진열대는 4종류의 보석(RUBY, DIA, EMERALD, SAPPHIRE) 8개가 진열된 예시입니다.

진열대 번호	1	2	3	4	5	6	7	8
보석 이름	DIA	RUBY	RUBY	DIA	DIA	EMERALD	SAPPHIRE	DIA
진열대의 3번부터 7번까지 5개의 보석을 구매하면 모든 종류의 보석을 적어도 하나 이상씩 포함하게 됩니다.

진열대의 3, 4, 6, 7번의 보석만 구매하는 것은 중간에 특정 구간(5번)이 빠지게 되므로 어피치의 쇼핑 습관에 맞지 않습니다.

진열대 번호 순서대로 보석들의 이름이 저장된 배열 gems가 매개변수로 주어집니다. 이때 모든 보석을 하나 이상 포함하는 가장 짧은 구간을 찾아서 return 하도록 solution 함수를 완성해주세요.
가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아서 return 하도록 하며, 만약 가장 짧은 구간이 여러 개라면 시작 진열대 번호가 가장 작은 구간을 return 합니다.

[제한사항]
gems 배열의 크기는 1 이상 100,000 이하입니다.
gems 배열의 각 원소는 진열대에 나열된 보석을 나타냅니다.
gems 배열에는 1번 진열대부터 진열대 번호 순서대로 보석이름이 차례대로 저장되어 있습니다.
gems 배열의 각 원소는 길이가 1 이상 10 이하인 알파벳 대문자로만 구성된 문자열입니다.
*/

#include<iostream>
#include<string>
#include<vector>
#include<map>
using namespace std;
bool check(vector<int> m)
{
    for(auto i:m)
    {
        if(i == 0)
            return false;
    }
    return true;
}
vector<int> solution(vector<string> gems) {
	vector<int> answer ;
    answer.push_back(1);
    answer.push_back(gems.size());
    map<string, int> hash; 
    int cnt =0;
	for (auto i:gems)
		hash[i]=0;
    
    for(auto &i:hash)//string -> int로 맵핑
        i.second = cnt++;
    
    vector<int> gems_cnt(hash.size(), 0);
    int s=0,e=0;
    
    while(s<gems.size())  
    {
        if(check(gems_cnt))
        {
            if(e-s-1< answer[1]-answer[0])
                answer = {s+1, e};
            gems_cnt[hash[gems[s]]] -=1;
            s++;
        }
        else
        {
            if(e>=gems.size())
                break;
            gems_cnt[hash[gems[e]]] += 1;
            e++;
        }
    }
	return answer;
};

/*
정확성  테스트
테스트 1 〉	통과 (0.01ms, 3.75MB)
테스트 2 〉	통과 (0.03ms, 3.79MB)
테스트 3 〉	통과 (0.10ms, 3.84MB)
테스트 4 〉	통과 (0.31ms, 3.84MB)
테스트 5 〉	통과 (0.08ms, 3.78MB)
테스트 6 〉	통과 (0.01ms, 3.85MB)
테스트 7 〉	통과 (0.01ms, 3.75MB)
테스트 8 〉	통과 (0.31ms, 3.82MB)
테스트 9 〉	통과 (0.36ms, 3.83MB)
테스트 10 〉	통과 (0.48ms, 3.85MB)
테스트 11 〉	통과 (0.83ms, 3.96MB)
테스트 12 〉	통과 (0.55ms, 3.88MB)
테스트 13 〉	통과 (0.77ms, 4MB)
테스트 14 〉	통과 (1.33ms, 3.95MB)
테스트 15 〉	통과 (1.48ms, 3.93MB)
효율성  테스트
테스트 1 〉	통과 (2.43ms, 3.9MB)
테스트 2 〉	통과 (8.89ms, 4.27MB)
테스트 3 〉	통과 (6.86ms, 4.38MB)
테스트 4 〉	통과 (25.72ms, 5.38MB)
테스트 5 〉	통과 (23.38ms, 4.93MB)
테스트 6 〉	통과 (10.65ms, 5.34MB)
테스트 7 〉	통과 (34.15ms, 5.85MB)
테스트 8 〉	통과 (35.15ms, 6.08MB)
테스트 9 〉	통과 (19.78ms, 6.34MB)
테스트 10 〉	통과 (36.00ms, 6.81MB)
테스트 11 〉	통과 (102.01ms, 7.62MB)
테스트 12 〉	통과 (190.15ms, 9.08MB)
테스트 13 〉	통과 (301.09ms, 9.7MB)
테스트 14 〉	통과 (130.80ms, 9.52MB)
테스트 15 〉	통과 (288.30ms, 10.4MB)
*/
//sol1(cpp)이 더 효율성이 좋다.