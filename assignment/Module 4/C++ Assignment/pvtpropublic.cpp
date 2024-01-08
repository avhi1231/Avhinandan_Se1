//Write a C++ Program to show access to Private Public and Protected using Inheritance
#include<iostream>
using namespace std;
class Myclass{
	private:
		string xyz;
		public:
		demo()
		{
			cout<<"\nEnter String : ";
			cin>>xyz;
			cout<<"--String in Pvt. "<<xyz;
			}	
	protected:
		int a=10,b=5;
		public:
		myfun()
		{
			cout<<"\nA : "<<a;
			cout<<"\nB : "<<b;
		}
		add()
		{
			cout<<"\nAddition : "<<a+b;
		}
};
class Child : public Myclass{
	public:
		sub()
		{
			cout<<"\nSubtraction: "<<a-b;
		}
};
int main()
{
	Child obj;
	obj.demo();
	obj.myfun();
	obj.add();
	obj.sub();
}
