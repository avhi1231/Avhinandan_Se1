#include <iostream>
using namespace std;
class Employee { 
  private: 
    string name; 
    int employeeId; 
    double salary; 

  public:
    // Constructor 
    Employee(const string & empName, int empId, double empSalary): name(empName), employeeId(empId), salary(empSalary) {}

    // Member function 
    calculateSalary(double pr) 
	{
      if (pr >= 0.0 && pr <= 1.4) 
	  { 
        salary *= pr; 
      } 
	  else
	   {
        cout << "Invalid performance rating. Salary remains unchanged.";
      }
    }

    
    setSalary(double empSalary) 
	{
      salary = empSalary; 
    }

   string getName() const 
	{
      return name; 
    }
    getEmployeeId() const 
	{
      return employeeId; 
    }
    getSalary() const 
	{
      return salary; 
    }
};

int main() {
  string empName;
  int empId; 
  double empSalary; 

  cout << "Input employee name: "; 
  cin >> empName;

  cout << "Input employee ID: "; 
  cin >> empId; 

  cout << "Input employee salary: "; 
  cin >> empSalary; 

  Employee employee(empName, empId, empSalary); 

  cout << "Initial salary: " << employee.getSalary();

  double pr;
  cout << "Input performance rating (0.0-1.2): ";
  cin >> pr; 

  employee.calculateSalary(pr); 

  // Display updated salary
  cout << "\nUpdated salary: " << employee.getSalary(); 

  return 0;
}
