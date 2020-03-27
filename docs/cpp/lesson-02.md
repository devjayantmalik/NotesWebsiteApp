# Lesson - 02

* Operators
* Conditionals
* Vectors
* Arrays
* Vectors
* StringStream
* Loops (while, for)

## Write a program to detect if a birth date is important or not?

* 1 years - 18 years is Important
* 21 years is important
* 50 years is important
* greater than 65 is important

```cpp
#include <iostream>

int main(int argc, const char **argv){
	// store the age
	int age = 0;

	// ask user for his age
	std::cout << "Enter your age: ";
	std::cin >> age;

	// store an important message.
	const std::string message = "Birthday is important.";

	// check for his age
	if(age >= 1 && age <=18){
		std::cout << message << std::endl;
	}
	else if((age == 21) || (age == 50)){
		std::cout << message << std::endl;
	}
	else if(age > 65){
		std::cout << message << std::endl;
	}
	else{
		std::cout << "Birthday is not important." << std::endl;
	}

	return 0;
}
``` 

## Write a program that determine a grade or class a student would goto based on the conditions.

* Age = 5 : Go to kindergarten.
* Age 6 - 17 : Go to grade 1 - 12
* Age > 17 : Go to college

```cpp
#include<iostream>

int main(int argc, const char **argv){
	// store the age
	int age = 0;

	// ask user for his age.
	std::cout << "Enter your age: ";
	std::cin >> age;

	// check for his age
	if(age < 5)
		std::cout << "Too young for school." << std::endl;
	else if(age == 5)
		std::cout << "Go to kindergarten." << std::endl;
	else if(age >= 6 && age <= 17)
		std::cout << "Go to grade " << age - 5 << std::endl;
	else
		std::cout << "Go to college." << std::endl;

	return 0;
}
```

## Create an array with default value initialized to 1 for all elements.

```cpp
#include <iostream>

int main(int argc, const char ** argv){
	// declare an array
	int nums[10] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};

	// incorrect: results in {1, 0, 0, 0, 0, 0...}
	// int nums[10] = {1};

	// calculate length of array
	int len = sizeof(nums) / sizeof(nums[0]);

	// print the array
	for(int i=0; i<len; ++i){
		std::cout << "Nums : " << i << " = " << nums[i] << std::endl;
	}

	return 0;
}
```

## Create an array that automatically infers its size.
```cpp
#include <iostream>

int main(int argc, const char ** argv){

	// declare an array
	int nums[] = {10, 20, 30, 40, 50, 60};

	// calculate its length
	int len = sizeof(nums) / sizeof(nums[0]);

	// print elements of an array
	for(int i=0; i<len; ++i){
		std::cout << "Nums: " << i << " = " << nums[i] << std::endl;
	}

	return 0;
}
```

## Create an array and perform following operations on it.

* Update its elements value
* Calculate its length using \*(dereference) operator and sizeof function
* Create a multidimensional array
* Access elements of multidimensional array

```cpp
#include <iostream>

int main(int argc, const char **argv){
	// create an array
	int nums[] = {10, 20, 30, 40, 50};

	// update element value of array
	nums[0] = 600;

	// calculate its length and print on screen
	int len = sizeof(nums) / sizeof(*nums);
	std::cout << "Length of nums array is : " << len << std::endl;
	
	// create a multidimensional array
	// read as 2 matrix of 2 rows and 3 columns each.
	int data[2][2][3] = {
		{
			{10, 20, 30},
			{40, 50, 60}
		},
		{
			{70, 80, 90},
			{100, 110, 120}
		}
	};

	// access elements of multidimensional array
	for(int matrix=0; matrix < 2; ++matrix){
		// to seperate multiple matrixes
		std::cout << "================" << std::endl;

		for(int row=0; row < 2; ++row){
			for(int col=0; col < 3; ++col){
				std::cout << data[matrix][row][col] << " ";
			}
			// to print like a matrix
			std::cout << '\n';
		}
		// to seperate multiple matrixes
		std::cout << "================" << std::endl;
	}

	return 0;
}
```

## Create a vector to hold 2 elements and perform following operations

* Update value of elements
* Push an element at the end of vector to prove it is resizable
* Calculate size of a vector using method.
* Print the last index of vector using [len - 1] notation.

```cpp
#include <iostream>
#include <vector>

int main(int argc, const char ** argv){

	// create a vector
	std::vector<int> nums(2);

	// update a vector
	nums[0] = 10;
	nums[1] = 20;

	// access elements of a vector
	std::cout << nums[0] << std::endl;

	// add extra element to a vector
	nums.push_back(30);

	// access size of a vector
	int len = nums.size()

	// print last index of a vector
	std::cout << "Last Index: " << nums[len -1 ] << std::endl;

	return 0;
}
```

## Create a string and convert it into a vector

```cpp
#include <iostream>
#include <string>
#include <sstream>

int main(int argc, const char ** argv){

	// create a string
	std::string sentence = "This is a collection of random words.";

	// create a vector to hold words
	std::vector<std::string> words;

	// create a string stream
	std::stringstream stream(sentence);

	// create a seperator
	char seperator = ' ';

	// create a variable to store a word temporary
	std::string tempWord = "";

	while(getline(stream, tempWord, seperator)){
		words.push_back(tempWord);
	}

	// print the vector elements
	for(int i=0; i < words.size; ++i){
		std::cout << words[i] << std::endl;
	}

	return 0;
}
```

## Create a simple calculator to solve the calculation entered by user.

Sample Output:

* Enter calculation (ex. 20 + 3) : 40 + 4
* 40.0 + 4.0 = 44.0
* Program should support +, -, /, *
* Any unsupported operator should display an error.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

int main(int argc, const char ** argv){
	// store the user input
	std::string calculation = "0 + 0";

	// store the converted numbers in vector
	std::vector<std::string> splittedWords;

	// ask user for calculation
	std::cout << "Enter calculation (ex. 2 + 4) : ";
	std::getline(std::cin, calculation);

	// create a string stream to allow us to manipulate strings
	std::stringstream calcStream(calculation);

	std::string word = "";
	// split the numbers out of calculation
	while(getline(calcStream, word, ' ')){
		splittedWords.push_back(word);
	}

	// check the operand and store the result
	double result = 0;

	// convert the string into double numbers.
	double num1 = std::stod(splittedWords[0]);
	double num2 = std::stod(splittedWords[2]);

	std::string operand = splittedWords[1];

		if(operand == "+")
			result = num1 + num2;
		else if(operand == "-")
			result = num1 - num2;
		else if(operand == "*")
			result =  num1 * num2;
		else if(operand == "/")
			result = num1 / num2;
		else{
			// print the error and exit the program.
			std::cout << "Please enter only +, -, *, /" << std::endl;
			return 0;
		}

	// print the result
	std::cout << num1 << " " << operand << " " << num2 << " = " << result;

	return 0;
}
```



