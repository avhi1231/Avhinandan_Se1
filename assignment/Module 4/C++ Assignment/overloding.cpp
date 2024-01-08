/*Write a program to Mathematic operation like Addition, Subtraction,
Multiplication, Division Of two number using different parameters and
Function Overloading*/
#include<iostream>
using namespace std;
class A{
	public:
		
		fun(int a,int b)
		{
			cout<<"\nNumber 1 : "<<a;
			cout<<"\nNumber 2: "<<b;
			cout<<"\nAdd : "<<a+b;
		}
		fun(float n1, float n2)
		{
			cout<<"\nNumber 1 : "<<n1;
			cout<<"\nNumber 2: "<<n2;
			cout<<"\nSubtract : "<<n1-n2;
		}
		fun(int a1,int b1, int c1)
		{
			cout<<"\nNumber A: "<<a1;
			cout<<"\nNumber B: "<<b1;
			cout<<"\nNumber C: "<<c1;
			cout<<"\nMultiplication : "<<a1*b1*c1;
		}
		fun(double x, double y)
		{
			cout<<"\nNumber 1 : "<<x;
			cout<<"\nNumber 2: "<<y;
			cout<<"\nDivision : "<<x/y;
		}
};

int main()
{

	A obj;
	obj.fun(5,6);
	obj.fun(4,3);
	obj.fun(2,4,5);
	obj.fun(15,4);
}
