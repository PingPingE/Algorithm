#include<iostream>
#include<vector>
using namespace std;
vector<long long> prime;
void get_prime(long long);
//12164kb	28ms
int main()
{
	cin.tie(0);
	ios::sync_with_stdio(0);
	//최대 400만까지 이므로 int -> long long
	long long N;
	cin >> N;
	get_prime(N);
	long long index_from=0, index_to = 0;
	long long res = 0;
	long long tmp_sum = 0;
	//투 포인터
	while(index_from <= index_to)
	{
		if (tmp_sum <= N)
		{
			if (index_to < prime.size())
			{
				tmp_sum += prime[index_to];
				index_to++;
			}
			else
				break;
		}
			
		else
		{
			tmp_sum -= prime[index_from];
			index_from++;
		}
		if (tmp_sum == N)
			res++;
	}
	cout << res;
	return 0;
}
void get_prime(long long n)//에라토스테네스의 체
{
	bool *check = new bool[n + 2]{ 0, };
	
	for (long long i = 2; i <= n; i++)
	{
		if (check[i])
			continue;
		prime.push_back(i);
		for (long long j = i*i; j <= n; j += i)
			check[j] = 1;
	}
	delete check;
}