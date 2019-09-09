## Variables :
Variables are place holders in RAM, which provides us ability to store data.

## Rules for Variables :
* Variable Names could contain letters, digits and underscore character.
* Variable name should start with a letter or underscore
* variable name should not contain spaces.
* Variable name length should be atleast one character.
* Variable name should not contain any special character except underscore.

> Note: In case of GCC compiler $ symbol is allowed.

## Types of Variables :
* Global Variable / Public Variables
* Local Variable / Private Variables

## Syntax of declaring variable :
```c
	datatype variable_name;
	datatype variable_name = value;
```

## Examples of variables :
```c
	int marks = 10;

	int age;	// age declared without any value.
	age =10;	// age assigned a value.
```

## Local Variables :
The variables which are present within a function are called as local variables.

## Examples of Local Variables :
```c
	int main() {
			//local scope variables
		int age = 10;
		char grade = 'A';
		float pi = 3.14f;

		return 0;
	}
```

## Examples of Global Variables :
```c
	float PI = 3.14;
	int main(){
		printf("Value of PI is %f",PI);
		return 0;
	}
```
## Scopes of Variables :
* Public Scope - means any part of program is able to use them.
* Private Scope - means only specific part of Program is able to use them.

## You Tell me...
* Which type of variable according to you has public scope?
*	Which type of variable according to you has private scope?

## Basic Conventions For Global Variables :
* Conventions are optional,
* They are rules followed by most of developers around the world.
* You may choose to implement them in your programs to keep seperate of concerns.

* Name your variable in UPPER CASE
* Declare your variables with pre allocated value.(to prevent garbage value)
* In case you do not know what value the variable will hold then, provide a suitable value to prevent garbage value.
* Keep length of characters in variable name to be minimum.
* Variable name should not exceed 50 characters.
* Variable name should be descriptive.

## Basic Conventions for Local Variables :
* Name you variable in CAMEL CASE.
* Declare your variable with default value to prevent allocation of garbage value.
* Variable name should be descriptive.

## On program execution :
* OS will create account of Program in STACK.
* OS will allocate some space in RAM.
* OS will generate address of allocation unit.
* OS will store address of variable in STACK.
* STACK Exists in RAM itself somewhere.

## Stack :
* Stack is a space in RAM created by OS to keep account of program and its variables.
* Stack helps OS keep record of RAM bits used by saveral programs during concurrent operations.
* Makes Multitasking possible.

## How Program Execution Works :

### $$$

#### Program *asks* ---> OS *allocate me some memory*
#### OS *Creates Account of Program* ---> OS *Allocates Space in RAM*
#### OS *Stores Address of Memory in STACK*
#### Program *Asks OS to store value in variable*
#### OS *fetches Address of variable from stack.*
#### OS *fetches data of variable stored at that address*
#### OS *provides program data in binary form*
#### Program *converts data as required*

### $$$

## Why were local variables developed ?
Let's see source code of some program to understand this,

```c
	int Multiply(int first, int second){
		return first * second;
	}
	int Sum(int a, int b){
		return a + b;
	}

	int main(){
		printf("a = %d and b = %d",a,b);
		return 0;
	}
```

In above situation,

* Our program has 3 functions.
* But None of Sum and Multiply functions are used in program.
* Our Sum() function has two local variables a and b.
* Our main function prints values of a and b on execution.

> We notice that, in our situation all three variables are local.

*	Let's Execute the program and see what happens :
>	Result : We got an error that a and b are not defined.

* It means a and b variables are not allocated any space in RAM by OS.
* So, Local variables prevent unnecessary space allocation in RAM. and this is the reason, why local variables were created.

## Why were global variables developed ?
Let's again see source code of some program to understand this,

```c
	float PI =3.14;

	float AreaOfCircle(float radius){
		return PI * (radius * radius);
	}

	int main(){
		printf("Value of PI is %f",PI);

		float area = AreaOfCircle(23.4f);

		printf("Area of Circle is %f",area);
	}
```

In above situation :
* We have a global variable PI.
* We have two functions that uses value of PI.
> In above situation we notice that PI is a global variable.

#### Conclusion :
So global variables to created to avoid duplicate variable declaration. This makes OS Fast and Efficient.

## Conclusions of why variables were created :

* Prevents duplicate code.
* Makes system faster.
* Prevents unnecessary usage of RAM.
* Reduces overall software size.
