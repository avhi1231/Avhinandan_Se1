#include<iostream>
using namespace std;
class Myclass{
	public:
		int a=5,b=7;
		fun()
		{
			
			a=a*b;
			b=a/b;
			a=a/b;
			cout<<"Swap Value \n A: "<<a;
			cout<<"\nB :"<<b;
		}
};
int main()
{
	Myclass obj;
	obj.fun();
}
