#include<iostream>
#include<set>
using namespace std;
//44356kb	1136ms
int main()
{

	int M, N;
	cin >> M >> N;
	set<int> s;
	for (int j = 2; j <= N; j++)
	{
		if (s.find(j) != s.end())
			continue;
		if (j >= M && j <= N)
			printf("%d\n", j);
		for (int k = j * 2; k <= N; k += j)
			s.insert(k);

	}
	return 0;
}