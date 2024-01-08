#include<iostream>
using namespace std;
class Rectangle{
	private:
		float l,w;
		public:
			area()
			{
				float ar,peri;
				cout<<"\nEnter Length of Rectangle: ";
				cin>>l;
				cout<<"Enter Width Of Rectangle: ";
				cin>>w;
				ar=l*w;
				peri = 2*(l+w);
				cout<<"\nArea of Rectangle : "<<ar;
				cout<<"\nPerimeter Of Rectangle : "<<peri; 
			}
};
int main()
{
	Rectangle obj;
	obj.area();
}
