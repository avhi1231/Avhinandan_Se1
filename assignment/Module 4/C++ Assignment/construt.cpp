//Write a program of Addition, Subtraction, Division, Multiplication using constructor.
#include<iostream>
using namespace std;
class Sample{
	public:
		float n1,n2;
		Sample()
		{
			cout<<"\nEnter First Number : ";
			cin>>n1;
			cout<<"\nEnter Second Number : ";
			cin>>n2;
			cout<<"\nAddition : "<<n1+n2;
			cout<<"\nSubtraction : "<<n1-n2;
			cout<<"\nDivision : "<<n1/n2;
			cout<<"\nMultiplication : "<<n1*n2;
		}
};
int main()
{
	Sample obj;
}
