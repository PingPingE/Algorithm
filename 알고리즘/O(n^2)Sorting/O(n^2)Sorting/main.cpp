
#include "insertion.h"
#include "Selection.h"
#include "bubble.h"

void main()
{
	int arr[10] = { 12, 3, 6, 23, 8, 13, 3, 7, 45, 21 };
	int arr2[5] = { 32,12,5,2,7 };
	int arr3[7] = { 2,1,0,43,5,7,21 };
	//Insertion(arr ,10);
	// Insertion(arr2, 5);
	//Insertion(arr3, 7);
	//Bubble(arr, 10);
	//Bubble(arr2, 5);
	//Bubble(arr3, 7);
	Selection(arr, 10);
	Selection(arr2, 5);
	Selection(arr3, 7);
	system("pause");
}