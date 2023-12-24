#include<stdio.h>
struct my{
	int a;
	int b;
};
main()
{
	struct my r;
	printf("Enter Number : ");
	scanf("%d",&r.a);
	printf("Enter Number : ");
	scanf("%d",&r.b);
	printf("A : %d",r.a+r.b);
//	printf("\nB : %d",r.b);
}
