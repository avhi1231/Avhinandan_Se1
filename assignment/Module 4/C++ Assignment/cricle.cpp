#include<iostream>
using namespace std;
class Cricle{
	private:
	float radius;
	public:
	area()
	{
		float ar,crnf;
		cout<<"\nEnter the Radius of Cricle: ";
		cin>>radius;
		ar = 3.14*radius*radius;
		crnf = 2*3.14*radius;
		cout << "\narea :  " <<ar;
		cout << "\ncircumference : " <<crnf;
	}	
	
};
int main()
{
 	Cricle obj;
 	obj.area();
}
