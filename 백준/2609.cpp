#include<iostream>
using namespace std;
int G(int, int);
int main()
{
	int n1, n2;
	cin >> n1 >> n2;
	int g = G(n1, n2);
	cout << g << "\n" << (n1*n2) / g;
	return 0;
}
int G(int a, int b)
{
	if (a%b == 0)
		return b;
	return G(b, a%b);
}
