#pragma once
void heap(int a[],int size)
{
	int child = 2;
	int parent = 1; //1���� ����
	int temp = 0;
	int cnt = 1;
	while (child < size)
	{
		if (cnt <= 2) {
			if (a[parent] < a[child])
			{
				temp = a[child];
				a[child] = a[parent];
				a[parent] = temp;
				child++;
				cnt++;
			}
		}
		else
		{
			parent = child;
			child = ++child;
			cnt = 1;
		}

	}

}