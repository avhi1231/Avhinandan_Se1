#include<stdio.h>
main()
{
	char a[30]="Abhinandan";
	char b[30]="Jay";
	char c[30]="Tops";
	int result = strcmp(a,b);
	int result1 = strcmp(b,c);
	printf("\n%d",result);	
	printf("\n%d",result1);	
}
