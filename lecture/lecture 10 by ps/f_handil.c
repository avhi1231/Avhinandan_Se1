#include<stdio.h>
main()
{
	FILE *fp;
	fp = fopen("Test.txt","w");
	fprintf(fp,"This is your Firs File");
	fclose(fp);
}
