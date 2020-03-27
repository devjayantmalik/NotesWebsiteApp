# Lesson - 04

* While
* Break
* Continue
* Do while
* Exception handling

## Write a program to print only odd numbers using while loop

```cpp
#include <iostream>

int main(int argc, char const *argv[])
{
	// create a variable to use in loop
	int i = 0;

	// printing the values
	while(i < 10){
		if(i % 2 == 0){
			i+= 1;
			continue;
		}

		std::cout << i << ", ";

		// increment the i
		i = i + 1;
	}

	return 0;
}

```


## Write a program to draw pine tree on the screen.

```cpp
// Sample Output: 
/*
    #
   ###
  #####
 #######
#########
    #
*/

#include <iostream>

int main(int argc, char const *argv[])
{
	// store height, spaces and hashes
	int height = 0;
	int spaces = 0;
	int hashes = 1;
	int tailSpaces = 0;

	// ask user height of tree
	std::cout << "Enter height of tree: ";
	std::cin >> height;

	// set the spaces and hashes
	spaces = height - 1;

	// just to put last space in center
	tailSpaces = spaces;

	// draw the tree
	while(height > 0){

		// draw the spaces
		// 4, 3, 2, 1, 0
		for(int i=0; i < spaces; ++i){
			std::cout << " ";
		}

		// decrement the spaces by 1
		spaces--;


		// draw the hashes
		// 1, 3, 5, 7, 9
		for(int i=0; i < hashes; ++i){
			std::cout << "#";
		}

		// increment the hashes by 2
		hashes += 2;

		// print a new line
		std::cout << "\n";

		// decrement the height
		height--;
	}

	// draw the tail of the tree
	for(int i=0; i<tailSpaces; ++i){
		std::cout << " ";
	}

	// draw the hash after spaces
	std::cout << "#" << std::endl;

	return 0;
}
```

## Write a program to divide two numbers and handle the division by zero exception.

```cpp
#include <iostream>

int main(int argc, char const *argv[])
{
	// declare two numbers
	double num1 = 0.0;
	double num2 = 1.0;

	// handle the zero division exception
	try{
		// ask user for input
		std::cout << "Enter First number: ";
		std::cin >> num1;

		std::cout << "Enter second number: ";
		std::cin >> num2;

		// check if num2 is zero
		if(num2 == 0) throw "Division by 0 is not possible.";

		// divide the numbers
		double result = num1 / num2;

		// print the result
		std::cout << "Result: " << num1 / num2 << std::endl;

	}catch(const char *ex){
		std::cout << "Error: " << ex << std::endl;
	}

	return 0;
}
```

## Write a program to demonstrate that after an error is thrown the remaining code inside try block is not executed. Throw an runtime error. Also catch all other exceptions.

```cpp
#include <iostream>

int main(int argc, char const *argv[])
{
	try{
		std::cout << "Throwing exception" << std::endl;
		throw std::runtime_error("Error Occured.");

		// the below statements will not execute
		std::cout << "The statement inside try." << std::endl;

	}catch(std::exception &exp){
		std::cout << "Handled Exception: " << exp.what() << std::endl;
	}
	catch(...){
		/// ... ellipsis will catch all exceptions.

		std::cout << "Default Exception:" << std::endl;
	}

	return 0;
}
```

## Write a program to demonstrate do while loop and also generate random number using ctime module. 

* Create a secret number guessing game.

> ctime module will provide you with seconds passed till now since **January 1, 1970**

```cpp
#include <iostream>
#include <ctime>

int main(int argc, char const *argv[])
{
	// create a seed
	srand(time(NULL));

	// create a secret num
	int secretNum = std::rand() % 10;

	// create a guess variable
	int guess = 0;

	do{
		// ask the user to enter a number
		std::cout << "Guess a number between 0 to 10: ";
		std::cin >> guess;

	}while(guess != secretNum);

	return 0;
}
```

## Create a number guessing game using only while loop.

```cpp
#include <iostream>
#include <ctime>

int main(int argc, char const *argv[])
{
	// seed the time to random function
	srand(time(NULL));

	// generate the random number.
	int random = std::rand() % 10;

	// store the guess
	int guess = 0;

	while(1){
		// ask the user for a input
		std::cout << "Guess a number: ";
		std::cin >> guess;

		// check if the guess is correct
		if(guess == random) break;
	}
	
	std::cout << "Hey, you guessed it right!" << std::endl;

	return 0;
}
```

## Create a user login screen prompting user for username and password. Invalid password will make the user try again.

```cpp
#include <iostream>

std::string USER_NAME = "root";
std::string PASSWORD = "root";

int main(int argc, char const *argv[])
{
	// store the username and password
	std::string username = "";
	std::string password = "";

	// ask the user for username and password
	do{
		

		// ask for username
		std::cout << "Enter your username: ";
		getline(std::cin, username);

		// ask for password
		std::cout << "Enter password: ";
		getline(std::cin, password);

		if(username == USER_NAME && password != PASSWORD){
			// clear the screen
			std::system("cls || clear");

			// tell the user for incorrect password
			std::cout << "=====================" << std::endl;
			std::cout << "   Invalid Password  " << std::endl;
			std::cout << "=====================" << std::endl;
		}
		

	}while((username != USER_NAME) || (password != PASSWORD));

	// clear the screen
	std::system("cls || clear");

	// print the auth success message.
	std::cout << "Authentication successful." << std::endl;

	return 0;
}
```

