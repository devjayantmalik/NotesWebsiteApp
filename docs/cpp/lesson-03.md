# Lesson - 03

* Vectors
* Loops
* Functions
* Pointers
* Arrays

## Create a vector and populate its values from 0 to 9 without using loops (Use c++ 2017 version and std::iota function in numeric library).

```cpp
#include <iostream>
#include <numeric>
#include <vector>


int main(int argc, char const *argv[])
{
	std::vector<int> nums(10);

	// populate value of vector
	std::iota(nums.begin(), nums.end(), 0);

	// another syntax
	// std::iota(std::begin(nums), std::end(nums), 0);

	// print elements of the array
	for(int i=0; i < nums.size(); ++i){
		std::cout << nums[i] << std::endl;
	}

	return 0;
}

```

## Create a vector and output its elements using shorter syntax of for loop

```cpp
#include <iostream>
#include <vector>
#include <numeric>

int main(int argc, char const *argv[])
{
	// create a vector
	std::vector<int> nums(10);

	// fill the vector with values
	std::iota(nums.begin(), nums.end(), 0);

	// print the vector values
	for(auto value: nums) 
		std::cout << value << std::endl;

	return 0;
}
```

## Create a vector and populate its values from 1 to 10. Now print the even values of inside the vector.

```cpp
#include <iostream>
#include <vector>
#include <numeric>

int main(int argc, char const *argv[])
{
	// create a vector
	std::vector<int> nums(10);

	// fill the values
	std::iota(nums.begin(), nums.end(), 1);

	// print the even values
	for(auto val: nums){
		if(val % 2 == 0) 
			std::cout << val << std::endl;
	}

	return 0;
}
```

## Create a function to add two numbers. Declare the function below main and its prototype above main.

```cpp
#include <iostream>

double addNumbers(double num1, double num2);

int main(int argc, char const *argv[])
{
	// declare two values
	int num1 = 10;
	int num2 = 20;

	// add the numbers
	double sum = addNumbers(num1, num2);

	// print the sum
	std::cout << num1 << " + " << num2 << " = " << sum << std::endl;

	return 0;
}


// ======================
// User defined functions
// ======================

double addNumbers(double num1, double num2){
	return num1 + num2;
}
```

## Write a program to prove that the global variables are accessible inside everywhere inside a file but local variables are accessible only inside the parent scope.

```cpp
#include <iostream>
#include <string>

// Global Variables
std::string REGISTRATION_CODE = "ABCD-EFGH-IJKL-MNOP";

int main(int argc, char const *argv[])
{
	// ask user for licence key
	std::string licence= "";

	std::cout << "Enter licence key: ";
	std::cin >> licence;

	// also note the global variable usage.
	// check for valid key
	if(licence == REGISTRATION_CODE){
		std::cout << "Product activated successfully..." << std::endl;
	}else{
		std::cout << "Activation failed..." << std::endl;
	}

	return 0;
}
```

```cpp
#include <iostream>

void validateKey(void);

int main(int argc, char const *argv[])
{
	// declare a secret_key
	int secret_key = 2020;

	// calling validate key function
	// the function will try to access
	// secret_key created by main.
	validateKey();

	return 0;
}

void validateKey(void){
	// the line will cause error because 
	// secret_key does not exist in this scope
	if(secret_key == 2020)
		std::cout << "Valid secret key." << std::endl;
	else:
		std::cout << "Invalid secret key." << std::endl;
}
```

## Create a variable age and change its value from other function using pointer.

```cpp
#include <iostream>

void changeAge(int *age){
	*age = 20;
}

int main(int argc, char const *argv[])
{
	// create age variable
	int age = 10;

	// print original value
	std::cout << "Original age: " << age << std::endl;	

	// change its value
	changeAge(&age); // address of age

	// print changed value
	std::cout << "Changed age: " << age << std::endl;
	return 0;
}

```

## Write a program to store address of some variable and print pointer contents on screen.

```cpp
#include <iostream>

int main(int argc, char const *argv[])
{
	// create a pointer
	int * years = NULL;

	// create a variable
	int num = 10;

	// assign the address of num to years
	years = &num;

	// print the contents of pointer
	std::cout << "Num address: " << years << std::endl;

	// change the value of num using pointer
	*years = 20;

	// print the value of num using pointer
	std::cout << "Years: " << *years << std::endl;

	return 0;
}
```

## Create a pointer to an array and print the values of the array using pointer. Also use pointer increment and decrement.

```cpp
#include <iostream>
#include <numeric>

int main(int argc, char const *argv[])
{
	// create an array
	int nums[10];

	// length of array
	int len = sizeof(nums) / sizeof(nums[0]);

	// fill the array
	std::iota(std::begin(nums), std::end(nums), 1);

	// array traversal using pointer
	int * ptr = nums;

	// print the first value
	std::cout << "Ist: " << *ptr << " Address: " << ptr << std::endl;

	// increment the pointer
	ptr++;

	// print the second value
	std::cout << "2nd: " << *ptr << " Address: " << ptr << std::endl;

	// decrement the pointer
	ptr--;

	// print the first value
	std::cout << "Ist: " << *ptr << " Address: " << ptr << std::endl;

	return 0;
}
```

## Write a function that receives pointer to an array and size of array. The function should double every value in the array.

```cpp
#include <iostream>

// function prototypes
void doubleArray(int * arr, int size);

int main(int argc, char const *argv[])
{
	// create an array
	int nums[10] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};

	// find length of the array
	int len = sizeof(nums) / sizeof(nums[0]);

	// double the values
	doubleArray(nums, len);

	// print the numbers
	for(auto num: nums) std::cout << num << std::endl;


	return 0;
}

// ==================
//	User defined functions.
// ==================

void doubleArray(int *arr, int size){
	for(int i=0; i<size; ++i){
		*arr = (*arr) * 2;
		arr++;

		// another way
		// arr[i] = arr[i] * 2
	}
}
```

## Create a range function of python using c++. The function should return a vector.

```cpp
#include <iostream>
#include <vector>

std::vector<int> range(int start, int end, int step);

int main(int argc, char const *argv[])
{
	// generate a list of values
	std::vector<int> values = range(1, 100, 1);

	// print the values
	for(auto val: values) std::cout << val << std::endl;
	
	return 0;
}

std::vector<int> range(int start, int end, int step){
	// create a vector
	std::vector<int> nums;

	// fill the vector with values
	for(int i=start; i < end; i += step){
		nums.push_back(i);
	}

	return nums;
}

```

## Write a program that uses range function made in previous example to calculate compound interest.

```cpp
#include <iostream>
#include <vector>

std::vector<int> range(int start, int end, int step);

int main(int argc, char const *argv[])
{
	// store the investment and interest and amount
	double investment = 0;
	double interest = 0;

	// ask user for investment
	std::cout << "How much to invest: ";
	std::cin >> investment;

	// ask user for interest
	std::cout << "Interest rate (in percent): ";
	std::cin >> interest;

	// divide the interest by 100 because of percent.
	interest = interest / 100;


	// Calculate the amount after 10 years
	for(auto i: range(0, 10, 1)){
		investment = investment + (investment * interest);
	}

	// print the final amount
	std::cout << "Amount after 10 years : " << investment << std::endl;

	return 0;
}

// ======================
// User defined functions
// ======================

std::vector<int> range(int start, int end, int step){
	// create a vector
	std::vector<int> result;

	// using while loop
	while(start < end){
		result.push_back(start);
		start += step;
	}
	
	// return the result
	return result;
}

```

