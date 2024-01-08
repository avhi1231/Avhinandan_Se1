/*. Write a C++ program to create a class called Triangle that has private
member variables for the lengths of its three sides. Implement member
functions to determine if the triangle is equilateral, isosceles, or scalene.*/
#include<iostream>
using namespace std;
class Triangle{
	private:
		float s1,s2,s3;
		
		public:
			check()
			{
		cout<<"\nEnter Side 1 : ";
		cin>>s1;
		cout<<"\nEnter Side 2 : ";
		cin>>s2;
		cout<<"\nEnter Side 3 : ";
		cin>>s3;
			//for equilateral triangle
			if (s1 == s2 && s2 == s3)
        	cout << "Equilateral Triangle";
 
 		   //for isosceles triangle
    		else if (s1 == s2 || s2 == s3 || s3 == s1)
        	cout << "Isosceles Triangle";
 
    		// for scalene triangle
    		else
        	cout << "Scalene Triangle";
			}
};
int main()
{
	Triangle obj;
	obj.check();
}
