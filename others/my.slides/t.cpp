
// Paycheck-V1.0
// AJ Avecilla
// Janurary 2, 2019
// CIS-54 C/C++ Programing
// Inputs: Hours, Payrate
// Outputs: Paycheck


#include <stdio.h>
#include <iostream>
#include <iomanip>
using namespace std;

int main(int argc, const char * argv[])
{
    // Variables
    double hours = 0 ;
    double wage = 0 ;
    double stdHours = 0 ;
    double overtimeHours = 0 ;
    double regularPay = 0 ;
    double overtimePay = 0 ;
    double grossPay = 0 ;
    double regPay = 0 ;
    
    // change the withholding tax rate from 17% to a new value between 5% and 25%.
    const double TAX_RATE = .20;    //tax rate
    double taxes;
    double netPay;
    
    //Hour Input & Wage Input
    std::cout << "Enter the Hours Worked: "; // Prompt
    std::cin >> hours;
    std::cout << "Enter The Pay Rate: "; // Prompt
    std::cin >> wage;
    
    // Hours Worked
    if (hours <= 40)
        { 
        stdHours = hours ;
        overtimeHours = 0.0 ;
        }    
    else 
        {
        stdHours = hours ; // xxx logic error here
        overtimeHours = hours - 40 ;
        }

    
    // Pay
        regularPay = stdHours * wage ;
        overtimePay = overtimeHours * wage * 1.5 ;
        grossPay = regularPay + overtimePay ;
 
    
    //Taxes_rate
    taxes = grossPay * TAX_RATE;
    netPay = grossPay - taxes;
    
    
    //OUTPUT the gross pay w/ two digits past the decimal
    std::cout << std::setiosflags(std::ios::fixed);
    std::cout << std::setiosflags(std::ios::showpoint);
    std::cout << "Your gross pay is: $" << std::setprecision(2) << 
grossPay << std::endl;

    //OUTPUT the taxes w/ two digits past the decimal
    std::cout << std::setiosflags(std::ios::fixed);
    std::cout << std::setiosflags(std::ios::showpoint);
    std::cout << "Your taxes are: $" << std::setprecision(2) << taxes << 
std::endl;

    //OUTPUT the net pay w/ two digits past the decimal
    std::cout << std::setiosflags(std::ios::fixed);
    std::cout << std::setiosflags(std::ios::showpoint);
    std::cout << "Your net pay is: $" << std::setprecision(2) << netPay << 
std::endl;

    return 0;
}
    
    

