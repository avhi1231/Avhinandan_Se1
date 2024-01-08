#include<iostream>
using namespace std;
class Multi{
	public:
		int num,sq,cu;
		sqar()
		{
			cout<<"\nEnter the Value To find Multipliaction & Cube Value:";
			cin>>num;
			sq=num*num;
			cout<<"\n Multiplication Values =  "<<sq;
		}
		cube()
		{
			cu=num*num*num;
			cout<<"\n Cube Values =  "<<cu;
		}
};
int main()
{
	Multi obj;
	obj.sqar();
	obj.cube();
}
