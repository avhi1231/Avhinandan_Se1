#include<iostream>
using namespace std;
class A{
	private:
		int a,b;
	
		public:
		show()
		{
			cout<<"Enter 1st Number :";
			cin>>a;
			cout<<"Enter 2nd Number :";
			cin>>b;
		}
		friend max(A t);
	
};
	max(A t)
		{
			if(t.a>t.b)
			{
				cout<<"\n1st Number is Greastest ";
			}
			else
			{
				cout<<"\n2nd Number is Greastest";
			}
		}
int main()
{
	A obj;
	obj.show();
	max(obj);
	
}
