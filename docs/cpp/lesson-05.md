# Lesson - 05

-   Math Functions
-   Strings

## Create a string using char datatype and an array. Also use null character. Also find its length.

```cpp
#include <iostream>

int main(int argc, char const *argv[])
{
	// create a string
	char name[] = {'J', 'A', 'Y', 'A', 'N', 'T', '\0'};

	// print the name string
	std::cout << name << std::endl;

	// find size of string
	std::cout << sizeof(name) << std::endl;

	// the above statement can also be written as:
	int len =  sizeof(name) / sizeof(name[0]);

	// the len and size will be equal because
	// the char has size of 1 byte.

	return 0;
}
```

## Create a string and perform some common operations on the string.

```cpp
#include <iostream>

int main(int argc, char const *argv[]){
	// create a string
	std::string words = "These are the words. I'll be late";

	// print the letter at some index
	std::cout << "First Letter: " << words.at(0) << std::endl;
	std::cout << "Second Letter: " << words[1] << std::endl;

	// find the letter at the front and back of string
	std::cout << "Front: " << words.front() << std::endl;
	std::cout << "Back: " << words.back() << std::endl;

	// find length of the string
	std::cout << "Length: " << words.length() << std::endl;

	// copy one string to another string
	std::string words2(words);

	// print all characters of string using for loop
	for(auto letter: words) std::cout << letter;

	// just to print a new line
	std::cout << std::endl;

	// copy everything after 4th character
	std::string words3(words, 4);

	// copy everything after 4th to 8th character
	std::string words4(words, 4, 8);

	// print the copied string
	std::cout << "Words 3: " << words3 << std::endl;
	std::cout << "Words 4: " << words4 << std::endl;

	// create a string with 5 'a' letters inside it
	std::string words5(5, 'a');

	// print the generated string.
	std::cout << "Words 5: " << words5 << std::endl;

	// append a string
	std::cout << "Append String: " << words5.append(" Hello") << std::endl;

	// append a part of the string
	std::cout << "Part of String appended: " << words5.append(words5, 4, 5) << std::endl;

	// delete from a string
	words5.erase(4, 9);
	std::cout << "Words 5: " << words5 << std::endl;

	// find some word inside string
	int index = words.find("late");

	std::cout << "Late found at index: " << index << std::endl;

	// create a substring
	std::string words6 = words.substr(21, words.length() -1);
	std::cout << "Substring is: " << words6 << std::endl;

	return 0;
}


```

## Find the ascii code of the characters of english alphabets

```cpp
#include <iostream>

int main(int argc, char const *argv[])
{
	// declare a character
	char a = 'a';
	char z = 'z';

	// print its ascii code
	std::cout << "a: " << int(a) << " b: " << int(z) << std::endl;
	std::cout << "A: " << int('A') << " Z: " << int('Z') << std::endl;

	return 0;
}
```

## Ask the user to enter a uppercase string. Hide its meaning by converting the string to its ascii code. and convert it back to its original meaning

```cpp
#include <iostream>

int main(int argc, char const *argv[])
{
	// store the string
	std::string original = "";
	std::string hidden = "";

	// ask user for message
	std::cout << "Enter message to hide in UPPERCASE: ";
	getline(std::cin, original);

	// convert the letters to ascii code and add it to string
	for(char letter: original)
	{
		int code = int(letter);
		hidden = hidden + std::to_string(code);
	}

	// display the hidden words
	std::cout << "Secret: " << hidden << std::endl;

	original = "";
	for(int i=0; i<hidden.length(); i += 2){
		std::string code = "";
		code += hidden[i];
		code += hidden[i+1];

		// convert it back to int
		int characterCode = std::stoi(code);

		// convert the int to character
		char decoded = characterCode;

		// add it to original string
		original += decoded;
	}

	// print the original string
	std::cout << "Decoded: " << original << std::endl;

	return 0;
}

```

## Ask the user to enter a string in either upper or lower case. Hide its meaning by converting the string to its ascii code. and convert it back to its original meaning

```cpp
#include <iostream>

int main(int argc, char const *argv[])
{
	// store the string
	std::string original = "";
	std::string hidden = "";

	// ask user for message
	std::cout << "Enter message to hide: ";
	getline(std::cin, original);

	// convert the letters to ascii code and add it to string
	for(char letter: original)
	{
		// subtract any number to make it 2 digits number
		// we will add it during decode process.
		int code = int(letter) - 24;
		hidden = hidden + std::to_string(code);
	}

	// display the hidden words
	std::cout << "Secret: " << hidden << std::endl;

	original = "";
	for(int i=0; i<hidden.length(); i += 2){
		std::string code = "";
		code += hidden[i];
		code += hidden[i+1];

		// convert it back to int
		int characterCode = std::stoi(code) + 24;

		// convert the int to character
		char decoded = characterCode;

		// add it to original string
		original += decoded;
	}

	// print the original string
	std::cout << "Decoded: " << original << std::endl;


	return 0;
}

```

## Create a program to demonstrate various mathematical operation using c plus plus

```cpp
#include <iostream>
#include <cmath>

int main(int argc, char const **argv){
	// find absolute value: remove negative sign.
	std::cout << "abs(-10): " << std::abs(-10) << std::endl;

	// find the max of two values
	std::cout << "max(10, 20): " << std::max(10, 20) << std::endl;

	// find min of two values
	std::cout << "min(10, 20): " << std::min(10, 20) << std::endl;

	// find max of floating point numbers
	std::cout << "fmax(19.2, 23.2): " << std::fmax(19.2, 23.2) << std::endl;

	// find exponential of a number raised to power e
	std::cout << "exp(1): " << std::exp(1) << std::endl;

	// find exponential of a number raised to power 2
	std::cout << "exp2(2): " << std::exp(2) << std::endl;

	// find log of a number
	std::cout << "log(20.2): " << std::log(20.2) << std::endl;

	// find log10 of a number
	std::cout << "log10(20.23): " << std::log10(20.23) << std::endl;

	// find log2 of a number
	std::cout << "log2(202): " << std::log2(202) << std::endl;

	// find the power of a number
	std::cout << "pow(2, 3): " << std::pow(2, 3) << std::endl;

	// find sqrt of a number
	std::cout << "sqrt(100): " << std::sqrt(100) << std::endl;

	// find cube root of a number
	std::cout << "cbrt(100): " << std::cbrt(100) << std::endl;

	// find hypoteneus of a triangle
	std::cout << "hypot(2, 3): " << std::hypot(2, 3) << std::endl;

	// round a number to its top
	std::cout << "ceil(2.3): " << std::ceil(2.3) << std::endl;

	// round a number to its bottom
	std::cout << "floor(3.4): " << std::floor(3.4) << std::endl;

	// round a number
	std::cout << "round(8.45): " << std::round(8.45) << std::endl;

	return 0;
}
```
