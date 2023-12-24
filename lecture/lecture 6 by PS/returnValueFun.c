#include<stdio.h>
myfun(n,n1)
{
	printf("Number 1: %d",n);
	printf("\nNumber 2: %d",n1);
	return n-n1;
}
main()
{
	int sub = myfun(20,10);
	printf("\nSubtraction = %d",sub);
}
