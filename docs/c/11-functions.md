## Functions in C :
- functions are containers that help reduce duplicacy of code

- make code reusable at different positions in our program.

- Keeps program modular and seperates logic of program in seperate blocks.

## Types of Functions :
1. User defined functions.

2. Built in functions.

> Note : In reality in c programming only user defined functions exist but for writing in exams if you are in india, then write both types.

## User Defined Functions :
These functions are defined by developer itself.

example :
```c
	int max(int a, int b){
		return (a>b) ? a : b;
	}
```

## Built in Functions :
These are the functions defined by creator of c and are used by developers.

example :

```c
	int main() {
		//built in function
		printf("i am built in function of c");
		return 0;
	}
```

## Function Invokation :
Steps to call a function in our program is called function invocation.

example:

```c
	int main(){
		max(1, 3); // invoked max function
		return 0;
	}
```

## Nested Function :
1. Nesting of functions is possible in c.

2. Nested functions are functions declared/invoked within other function functions.

## Rules for Functions :
1. Variable name rules are same for function naming rules.

- Function Arguments are optional.

- Function return type could be void.

- By default a function in c returns int as datatype.

- return keyword is used to send response back from function.

## Syntax of Function :
```c
	return_type function_name( arguments )
	{
		// body of function.
	}
```

## Examples of Function :

```c
	//function returning void.
	void print_letters (char c)
	{
		for( int i = 0; i <= 10; i++)
		{
		     printf("%c\n",c);
		}
	}
```
```c
	// function return int as return type.

	int max( int a, int b )
	{
		return (a>b) ? a : b ;
	}
```
```c
	// function with no arguments
	void drawcircle()
	{
		printf("I am drawing circle\n");
		circle(100,100,30);
	}
```

## Function Arguments :
1. Actual Arguments

2. Formal Arguments

## Formal Arguments :
These are the declarations within user defined functions.

example :
```c
	int max( int a, int b ) // formal arguments.
	{
		return ( a > b ) ? a : b ;
	}
```

## Actual Arguments :
These are values passed during invocation of function.

example :
```c
	int main(){
		max( 2, 4 ); // actual arguments.
		return 0;
	}
```

## Expression Evaluation in Function Invocation:
Expressions passed in functions are always evaluated form right to left.

example :
```c
	int sum( int a, int b)
	{
		return a + b ;
	}

	int main()
	{
		int result = sum ( printf("abc"); , printf("def") );

		printf("\tResult is %d ", result );

		return 0;
	}
```
> #### Output will be  : defabc		 Result is 6

## Expression evaluation in Function Definition :
- In case of function declaration expression evaluation does not exist.

- In case of function definition values are assigned/declared from left to right.

example :
```c
	int multiply(int a, int b)
	{
		return a * b ;
	}
```

## Some practice for functions :
#### Find Output of program :
```c
	int max ( int a , int b )
	{
	    return ( a > b ) ? a : b ;
	}

	int main()
	{
		int number = 10;
		int result = max ( ++a , ++a ); // result = ?
		return 0;
	}
```

#### Find Max of four numbers :
```c
	int max ( int a, int b )
	{
		return ( a > b ) ? a : b ;
	}

	int main()
	{
		int first = 10;
		int second = 12;
		int third = 20;
		int fourth = 22;

		// code for max.
		int result = max( max(first, second) , max(third, fourth) ) ;
		printf(" Maximum value is %d \n", result ) ;
		return 0;
	}
```

#### Program to print letters in increasing order.
```c
	void pattern(char c, int times)
	{
		for(int i = 0; i <= times; i++){
			for(int j =0; j <= i; j++){
			   printf("%c",c);
			}
		   printf("\n");
		}
	}

	int main()
	{
		pattern('$', 5);
		pattern('Û', 7);
		return 0;
	}

```
