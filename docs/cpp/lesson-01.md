# Basic Introduction and First Program

## Write a program that displays hello world on the screen.

```cpp
#include <iostream>

int main(int argc, const char ** argv){

	// displays hello world
	std::cout << "Hello World" << std::endl;

	return 0;
}
```

## Write a program to display all the arguments passed to the program from command line using for loop

```cpp
#include <iostream>

int main(int argc, const char ** argv){
	// argc : count no of arguments
	// argv : pointer to list of arguments

	for(int i=0; i<argc; ++i){
		// prints the argument
		std::cout << argv[i] << std::endl;
	}
}
```

## Write a program to demonstrate how to import a function only instead of whole namespace with the help of using statement.

```cpp
#include <iostream>

// using cout and endl inside
// standard namespace.
using std::cout;
using std::endl;

int main(int argc, const char ** argv){
	cout << "Hello, this is Really cool..." << endl;

	return 0;
}
```

## Write a program to print multiplication table of 3 using for loop.

```cpp
#include <iostream>

int main(int argc, const char **argv){

	int num = 3;
	for(int i=1; i<=10; ++i){
		std::cout << num << " x " << i << " = " << num * i << std::endl;
	}

	return 0;
}
```

## Create two gloabl and two local variables

```cpp
#include <iostream>

// GLOBAL VARIABLES
int PI = 3.1417;
int SCORE = 0;

int main(int argc, const char **argv){

	// local variables
	for(int i=0; i<10; ++i){
		// the output will always be 10.
		int num = 10;

		// print the output
		std::cout << num << std::endl;

		// increment the number
		num++;
	}

	return 0;
}
```

## Declare all the datatypes: char, double, bool, float, int, auto, signed, unsigned, short, long

```cpp
#include <iostream>

int main(int argc, const char **argv){

	// without decimal types
	char grade = 'A';
	int num1 = 1020;
	signed int num2 = -1020;
	unsigned int num3 = 1010;
	long long int num4 = 10102120120;
	short int age = 20;
	bool isPasswordValid = false;

	// with decimal types
	float num5 = 23.23;
	double num6 = 453452342.23;
	long double num7 = 23232.23;

	// auto type inference
	auto num = 20;

	// string type
	std::string name = "Jayant Malik";

	return 0;
}
```

## Write a program to find min and max limits of datatypes created above. Also find its size.

```cpp
#include <iostream>
#include <limits>

int main(int argc, const char **argv){

	// finding size of all datatypes
	std::cout << "=============Size==============" << std::endl;
	std::cout << "Int :" << sizeof(int) << std::endl;
	std::cout << "Float: " << sizeof(float) << std::endl;
	std::cout << "Double: " << sizeof(double) << std::endl;
	std::cout << "Char: " << sizeof(char) << std::endl;
	std::cout << "Bool: " << sizeof(bool) << std::endl;
	std::cout << "Short: " << sizeof(short) << std::endl;
	std::cout << "Long: " << sizeof(long) << std::endl;
	std::cout << "Long Long Int: " << sizeof(long long int) << std::endl;
	std::cout << "Long Double: " << sizeof(long double) << std::endl;
	std::cout << "Signed Int: " << sizeof(signed int) << std::endl;
	std::cout << "Unsigned Int: " << sizeof(unsigned int) << std::endl;

	std::cout << "************************************\n";
	std::cout << "************************************\n";

	// max of types
	std::cout << "===============Max=============" << std::endl;
	std::cout << "Int :" << std::numeric_limits<int>::max() << std::endl;
	std::cout << "Float: " << std::numeric_limits<float>::max() << std::endl;
	std::cout << "Double: " << std::numeric_limits<double>::max() << std::endl;
	std::cout << "Char: " << std::numeric_limits<char>::max() << std::endl;
	std::cout << "Bool: " << std::numeric_limits<bool>::max() << std::endl;
	std::cout << "Short: " << std::numeric_limits<short>::max() << std::endl;
	std::cout << "Long: " << std::numeric_limits<long>::max() << std::endl;
	std::cout << "Long Long Int: " << std::numeric_limits<long long int>::max() << std::endl;
	std::cout << "Long Double: " << std::numeric_limits<long double>::max() << std::endl;
	std::cout << "Signed Int: " << std::numeric_limits<signed int>::max() << std::endl;
	std::cout << "Unsigned Int: " << std::numeric_limits<unsigned int>::max() << std::endl;

	std::cout << "************************************\n";
	std::cout << "************************************\n";


	// min of types
	std::cout << "===============Min=============" << std::endl;
	std::cout << "Int :" << std::numeric_limits<int>::min() << std::endl;
	std::cout << "Float: " << std::numeric_limits<float>::min() << std::endl;
	std::cout << "Double: " << std::numeric_limits<double>::min() << std::endl;
	std::cout << "Char: " << std::numeric_limits<char>::min() << std::endl;
	std::cout << "Bool: " << std::numeric_limits<bool>::min() << std::endl;
	std::cout << "Short: " << std::numeric_limits<short>::min() << std::endl;
	std::cout << "Long: " << std::numeric_limits<long>::min() << std::endl;
	std::cout << "Long Long Int: " << std::numeric_limits<long long int>::min() << std::endl;
	std::cout << "Long Double: " << std::numeric_limits<long double>::min() << std::endl;
	std::cout << "Signed Int: " << std::numeric_limits<signed int>::min() << std::endl;
	std::cout << "Unsigned Int: " << std::numeric_limits<unsigned int>::min() << std::endl;

	std::cout << "************************************\n";
	std::cout << "************************************\n";

	return 0;
}
```

## Write a program to demonstrate that floats have precision of 16 digits while double have much greater precision.

```cpp
#include <iostream>

int main(int argc, char const *argv[])
{
	float num1 = 0.111111111111111111;
	float num2 = 0.111111111111111111;

	// display the sum
	printf("Sum : %.20f\n", num1 + num2);

	return 0;
}
```

> Note: 32 bit compiler has 8 digits precision and 64 bit compiler has 16 digits precision.

## Ask user to enter two numbers and display their sum.

```cpp
#include <iostream>

int main(int argc, char const *argv[])
{
	// store the numbers
	std::string num1 = "0";
	std::string num2 = "0";

	// ask user for num1
	std::cout << "Enter first number: ";
	getline(std::cin, num1);

	// ask user for num2
	std::cout << "Enter second number: ";
	getline(std::cin, num2);

	// convert the numbers to int and add
	// std::stoi --- string to integer
	// std::stod -- string to double
	int sum = std::stoi(num1) + std::stoi(num2);

	// print the sum
	std::cout << num1 << " + " << num1 << " = " << sum << std::endl;

	return 0;
}

```

## Write a program to convert miles to kms

> km = miles \* 1.60934

```cpp
#include <iostream>

int main(int argc, const char **argv){
	// store the miles
	std::string miles = "0";

	// ask user for miles
	std::cout << "Enter miles: ";
	getline(std::cin, miles);

	// convert miles in kms
	double kms = std::stod(miles) * 1.60934;
	// print the kms
	std::cout << miles << " miles equals " << kms << " kms\n";

	return 0;
}
```

## Write a program to swap two numbers.

```cpp
#include <iostream>

int main(int argc, const char ** argv){
	// store two numbers
	int num1 = 10;
	int num2 = 20;

	// swap the number
	int temp = num1;
	num1 = num2;
	num2 = temp;

	// print the numbers
	std::cout << "Num 1 : " << num1 << std::endl;
	std::cout << "Num 2 : " << num2 << std::endl;

	return 0;
}
```

## Write a program to calculate area and perimeter of a rectangle.

```cpp
#include <iostream>

int main(int argc, const char ** argv){
	// create two numbers.
	int length = 20;
	int breadth = 10;

	// print length of rectangle
	std::cout << "Length of rectangle: " << length << std::endl;
	std::cout << "Breadth of rectangle: " << breadth << std::endl;

	// perimeter of rectangle.
	std::cout << "Perimeter of rectangle: " << 2 * (length + breadth) << std::endl;

	// area of rectangle
	std::cout << "Area of rectangle: " << length * breadth << std::endl;

	return 0;
}
```

## Write a program to calculate total and average of n numbers.

```cpp
#include <iostream>
#include <vector>

int main(int argc, const char ** argv){
	// store the total and average
	std::vector<int> nums;

	while(1){
		int num = 0;

		// ask user to enter a number
		std::cout << "Enter -1 to exit or Enter a number: ";
		std::cin >> num;

		if(num == -1){
			break;
		}

		// add the no to vector
		nums.push_back(num);
	}

	// find length of nums
	int len = sizeof(nums) / sizeof(*nums);

	// find the sum
	int total = 0;
	for(int i=0; i < len; ++i){
		total += nums[i];
	}

	// print the sum and average
	std::cout << "Sum of nums are: " << total << std::endl;
	std::cout << "Average of nums are: " << total / len << std::endl;

	return 0;
}
```

## Write a program to check whether a number is positive or negative

```cpp
#include <iostream>

int main(int argc, const char ** argv){
	// ask user to enter a number.
	int num = 0;

	std::cout << "Enter a number: ";
	std::cin >> num;

	// check if a number is negative
	if(num < 0)
		std::cout << "Number is negative." << std::endl;
	else if(num == 0)
		std::cout << "Number is zero or an invalid entry." << std::endl;
	else
		std::cout << "Number is positive." << std::endl;

	return 0;
}
```

## Write a program to swap two variables without using third variable

```cpp
#include <iostream>

int main(int argc, char **argv){
	// ask user for a number
	int num1 = 0;
	int num2 = 0;

	std::cout << "Enter first number: ";
	std::cin >> num1;

	std::cout << "Enter second number: ";
	std::cin >> num2;

	// swapping the variables
	num2 = num1 + num2;
	num1 = num2 - num1;
	num2 = num2 - num1;

	std::cout << "Number 1 : " << num1 << std::endl;
	std::cout << "Number 2 : " << num2 << std::endl;

	return 0;
}
```
