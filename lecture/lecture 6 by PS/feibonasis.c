#include<stdio.h>
myfun(num)
{
	
	int n1=0,n2=1,n3,i;
	printf("\n%d %d",n1,n2);  // for 0 and 1 print
	for(i=3;i<=num;i++)   //loop started from 3 bcz 0 and 1 is already printed
	{
	n3=n1+n2;    
 	printf(" %d",n3);    
  	n1=n2;    
  	n2=n3;
	}
	
}
main()
{
	int x;
	printf("Enter Number: ");
	scanf("%d",&x);
	myfun(x);
}
