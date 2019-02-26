#include <iostream>
#include "LinkedList.h"
void main()
{
	LinkedList li;
	li.insert(3);
	li.insert(5);
	li.insert(2);
	li.display();
	li.remove(5);
	li.remove(2);
	li.display();
}