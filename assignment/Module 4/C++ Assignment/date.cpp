/*Write a C++ program to implement a class called Date that has private
member variables for day, month, and year. Include member functions to
set and get these variables, as well as to validate if the date is valid.*/
#include <iostream> 
using namespace std;
class Date { 
  private: 
    int day,month,year;
  public:
    // Constructor
    Date(int d, int m, int y): day(d), month(m), year(y) {}

    // Member function
    setDate(int d, int m, int y)
	 {
      day = d; 
      month = m; 
      year = y; 
    }
    getDay() const 
	{
      return day; 
    }
    getMonth() const 
	{
      return month; 
    }
    getYear() const 
	{
      return year;
    }
    isValidDate() const 
	{
      // Check valid month
      if (month < 1 || month > 12)
        return false;

      // Check valid day
      if (day < 1 || day > 31)
        return false;

      // Check for specific month-day combinations that are invalid
      if ((month == 4 || month == 6 || month == 9 || month == 11) && day > 30)
        return false;

      if (month == 2) {
        // Check for leap year
        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
          if (day > 29)
            return false;
        } else {
          if (day > 28)
            return false;
        }
      }

      // Date is valid
      return true;
    }
};

int main() 
{
  // Create a date object
  Date date(0, 0, 0); 
  int day, month, year; 
  cout << "Enter day: "; 
  cin >> day; 
  cout << "Enter month: ";
  cin >> month; 
  cout << "Enter year: "; 
  cin >> year;

  date.setDate(day, month, year); // Set Date

  // Get date
  cout << "Date: " << date.getDay() << "/" << date.getMonth() << "/" << date.getYear();

  // Validate the date
  if (date.isValidDate())
    cout << "\nThe date is valid.";
  else
    cout << "\nThe date is invalid.";

  return 0;
}
