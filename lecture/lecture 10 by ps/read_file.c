#include<stdio.h>
main()
{
	FILE *fp;
	fp = fopen("Test.txt","r");
	char a[100];
	fgets(a,100,fp);
	printf("%s",a);
	fclose(fp);
}
