#include<stdio.h>
myfun()
{
	int a,b;
	printf("Enter Number : ");
	scanf("%d",&a);
	printf("Enter Number : ");
	scanf("%d",&b);
	return a*b;
}
main()
{
	int c = myfun();
	printf("Multiplication is %d ",c);
}
