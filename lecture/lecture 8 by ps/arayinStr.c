#include<stdio.h>
struct my{
	int a[5];
	int i;
};
main()
{
	
	struct my r;
	for(r.i=0;r.i<5;r.i++)
	{
	printf("Enter Number : ");
	scanf("%d",&r.a[r.i]);
	}
	for(r.i=0;r.i<5;r.i++)
	{
	printf("\nNumber is : %d  ",r.a[r.i]);
}
}
