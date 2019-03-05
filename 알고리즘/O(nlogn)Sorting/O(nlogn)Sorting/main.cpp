#include "mergeSort.h"
#include "heap.h"
#include "Quick.h"

void main()
{
	int a1[10] = { 3,18,2,31,0,12,56,78,25,67 };
	int a2[8] = { 4,1,7,9,24,41,2,8 };
	int a3[5] = { 65,23,33,12,84 };

	//Quick(a1, 0, 9);
	//for (int i = 0; i < 10; i++)
	//	cout << a1[i] << " ";
	//cout << endl;
	//
	//Quick(a2, 0, 7);	
	//for (int i = 0; i < 8; i++)
	//	cout << a2[i] << " ";
	//cout << endl;

	mergeSort(a1, 0, 9);
	for (int i = 0; i < 10; i++)
		cout << a1[i] << " ";
	cout << endl;

	mergeSort(a3, 0, 4);
	for (int i = 0; i < 5; i++)
		cout << a3[i] << " ";
	cout << endl;

	//heap(a3, 5);
	//for (int i = 0; i < 5; i++)
	//	cout << a3[i] << " ";
	//cout << endl;
	//heap(a1, 10);
	//for (int i = 0; i < 10; i++)
	//	cout << a1[i] << " ";
	//cout << endl;

	//heap(a2, 8);
	//for (int i = 0; i < 8; i++)
	//	cout << a2[i] << " ";
	//cout << endl;
}