#include<iostream>
using namespace std;
int main()
{
	int n1,n2,n3;
	cout<<"Enter Number 1 : ";
	cin>>n1;
	cout<<"Enter Number 2 : ";
	cin>>n2;
	cout<<"Enter Number 3 :";
	cin>>n3;
	
	if(n1>n2)
	{
	if(n1>n3)
	{
		cout<<"Number 1 is Greatest ";
	}
	else
	{
		cout<<"Number 3 is Greatest ";
	}
}
else
{
	if(n2>n3)
	{
		cout<<"Number 2 is Greatest ";
	}
	else
	{
		cout<<"Number 3 is Greatest ";
	}
}
}
