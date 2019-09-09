## Preprocessor Directives :
Preprocessor directives are special kind of c statements, that are processed during compilation of c program.

## Types of Preprocessor directives :
1. File inclusion preprocessor

2. Macro preprocessor

3. Conditional preprocessor

## Preprocessor :
1. preprocessor tells compiler about some special kind of action to execute.

2. preprocessor directives are started with # symbol.

## File inclusion preprocessor :
1. File inclusion preprocessor directives are used to include some other c file in our program code file.

- File inclusions are included using #include keyword.

- File inclusion preprocessor can be included in any scope (global or local).

- code from other file is copied in your main program file during compilation.

## Syntax of file inclusion preprocessor :
```c
	#include<filename>	or
	#include "filename"
```

## Difference in double and single quotes inclusions:
1. "" are searches file in current directory and then searches in include directory (if not found in current path).

- <> searches file in include directory.

## Rules of file preprocessor :
1. Single inclusion per line is allowed only.

- No two files can be included in single line.(others are discarded in any.)

- Semicolons are not used with file preprocessor.

- Absolute path can be used to include preprocessor. (/home/jayant/file.c)

- Short path is not allowed. (~/temp/file.c)

## Why to use preprocessor :
preprocessor are used to include instructions written in some other file into our main program file.

## Errors in Preprocessors :
### Program 1 :
```c
	//----------------------temp.c file----------------

	printf("Hello from program.c");

	//----------------------program.c------------------
	#include "temp.c" // not allowed because only declarative statements are allowed in global scope.

	int main(){
		printf("in beginning of main...\n");

		#include<temp.c>	// error because file not present in
						 // include directory.

		#include "temp.c" // replaced by printf("Hello from program.c");
						// during compilation.

		return 0;
	}
```

### Program 2 :
```c
	//--------------------temp.c---------------------
		int sum(const int *const num1, const int * const num2){
			return *num1 + *num2;
		}


	//-------------------program.c------------------
	#include "temp.c"

		int main(){
			int num1 = 10, num2 = 20;

			int result = sum(&num1, &num2);

			printf("Result is %d\n",result);

			return 0;
		}

```

## Conclusions from File inclusion preprocessor:
1. keep scope of code in mind of temp.c file because code from temp.c file will be substituted in program.c file.

2. use "" or <> syntax as per directory, which stores your .c file.

## What happens during compilation :
1. temp.c ------>  compiler -----> .obj file

2. program.c ----> compiler -----> .exe file / .out file

## What dennis ritche did :
1. He wrote saveral .c files that contained his c code.

- He injected .obj file to .lib or .dll file.

- When compiler linker does its action during compilation time, then he checks .lib or .dll file..

- Now we uses printf function that is injected somewhere in .lib file.

## Difference between dll and lib file :
- Dll files load limited contents of code to memory as required by program.

- lib file loads all code to memory whether it is required or not.

## How to inject file to .lib or .dll file using turboc++ ?
1. Navigate to BIN directory.

- using tslib.exe inject .obj file to .lib file

- command : tslib ../lib/CS.lib + sample.obj

# Header Files in C :
Now, We injected our .obj file to .lib file then, question arises how will user know what are functions defined in .lib file.

Header files are simple text files with .h extension used to define function prototypes and macro definition.

Header files are used to tell developer about which functions are declared in .lib file.

Header files do not contain any program logic. it only contains function prototype which tells us few things :
	1. Name of function
	2. Return value of function
	3. Inputs required by function.

## Creating function prototype in a header file (sample code):
```c
	int cdecl sum(const int *num1, const int *num2);
```

## Some terms in header file :
1. cdecl ---> specifies that function was purely written in c language syntax. (c declarative)

# Macro Preprocessor :
Macro preprocessor is used to define a custom name for any operator or statement.

it reduces duplicate code.

it helps to call multiple statements of c using a single macro name.

There is no stack formation in case of macro, these are c statements that are replaced in code during compilation with their values.

## Syntax to declare macro :
```c
	#define macro_name value_or_statements
```

## Example of macro :
```c
	#define PI 3.14
	#define NAME printf("Hello"); printf("Jayant");
```

## Types of MACROS :
1. Simple Macro without Argument.
		it do not have any arguments as functions have.
2. Argument Macro
		it has arguments that are replaced by values.

## Example of Simple Macro :
```c
	#define PI 3.14

	#define Age 20
```

## Syntax of Argument Macro :
```c
	#define sum(x,y) x+y

	#define multiply(a,b) a*b
```

>## Note : In case of argument macro there is no formation of stack.

## Example of Macro :

### Program 1 :
```c
	#define PI 3.14

	int main(){
		int pi_square = PI * PI;	//int pi_square = 3.14 * 3.14;
		printf("value of PI is %f\n",pi_square);

		return 0;
	}
```

### Program 2 :
```c
	#define AND &&

	int main(){
		int age = 10;

		if( (age > 5) AND (age < 19))
			printf("Congrats you won a laptop.\n");

		else
			printf("You won a titanic ship.\n");


		return 0;
	}
```

### Program 3 :
```c
	#define sum(a,b) a+b

	int main(){
		long double first, second;

		printf("Enter first number:\t");
		scanf("%Le",&first);	// 10

		printf("Enter second number:\t");
		scanf("%Le",&second);	// 20

		long double result = sum(first,second); // int result = 10 + 20 ;

		printf("Result is %Lf\n",result); //result = 30

		return 0;
	}
```
