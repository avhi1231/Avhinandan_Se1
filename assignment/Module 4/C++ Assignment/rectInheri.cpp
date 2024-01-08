//Write a C++ Program to find Area of Rectangle using inheritance
#include<iostream>
using namespace std;
class Rectangle{
	public:
		int l,w,area;
		input()
		{
			cout<<"\nEnter Length of Rectangle : ";
			cin>>l;
			cout<<"\nEnter Width of Rectangle : ";
			cin>>w;
		}
};
class Calculate : public Rectangle{
	public:
		proces()
		{
			area=l*w;
		}
		display()
		{
			cout<<"\nArea Of Rectangle : "<<area;
		}
};
int main()
{
	Calculate obj;
	obj.input();
	obj.proces();
	obj.display();
}
