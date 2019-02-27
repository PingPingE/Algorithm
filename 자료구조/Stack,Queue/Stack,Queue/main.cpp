#include "Queue.h"
#include "Stack.h"

void main()
{
	Stack st;
	st.push(1);
	st.push(3);
	st.display();
	st.push(6);
	st.push(7);
	st.pop();
	st.display();
	
	Queue q;
	q.enqueue(3);
	q.enqueue(5);
	q.dequeue();
	q.display();
	q.enqueue(7);
	q.enqueue(10);
	q.dequeue();
	q.display();
}