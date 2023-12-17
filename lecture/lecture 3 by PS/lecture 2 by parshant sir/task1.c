#include<stdio.h>
main()
{
	
int n1,n2,n3;
printf("Enter number 1 : ");
scanf("%d",&n1);
printf("\nEnter number 2 : ");
scanf("%d",&n2);
printf("\nEnter number 3 : ");
scanf("%d",&n3);
if(n1>n2)
{
	if(n1>n3)
	{
		printf("Number 1 is Greatest ");
	}
	else
	{
		printf("Number 3 is Greatest ");
	}
}
else
{
	if(n2>n3)
	{
		printf("Number 2 is Greatest ");
	}
	else
	{
		printf("Number 3 is Greatest ");
	}
}
}
