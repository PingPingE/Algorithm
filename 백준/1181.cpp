/*
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
- 길이가 짧은 것부터
- 길이가 같으면 사전 순으로
* 1≤N≤20,000
*/
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<algorithm>
#include<map>
#include<set>
#include<string>
using namespace std;
int main()//4764kb, 736ms
{
	int N;
	string st;
	cin >> N;
	map<int, set<string>> m;//중복제거를 위해 set<string>으로 선언
	getline(cin, st);
	for (int i = 0; i < N; i++)
	{
		getline(cin,st);
		m[st.size()].insert(st);
	}

	for (auto const&k : m)//map의 value를 돌면서(key는 오름차순) 
	{
		for (std::set<string>::iterator it = k.second.begin(); it != k.second.end(); it++)
			cout << *it<<endl;//오름차순으로 string 출력
	}
	return 0;
}


//다른 사람 풀이: 4224kb, 56ms
/*
#include<iostream>
#include<algorithm>
using namespace std;

pair<int, string> words[20001];//길이와 문자열을 받을 pair 배열 선언

int main() {
	int n;
	cin >> n;
	for (int i = 0; i<n; i++) {
		cin >> words[i].second;
		words[i].first = words[i].second.size();
	}
	sort(words, words + n);//정렬
	for (int i = 0; i<n; i++)//모든 배열을 돌면서
		if (words[i] != words[i - 1])//중복 확인 후 
			cout << words[i].second << '\n';//출력
}
*/