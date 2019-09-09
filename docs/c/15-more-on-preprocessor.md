## Conditional Preprocessor :
These are used to perform inclusion of file based on some condition.

## keywords related to conditional preprocessor :
| Sr. | keyword | Full Form | Usage
------|--------|------------|-------
| 1 | #ifdef | if defined | used to check whether a macro is declared previously.
| 2 | #ifndef | if not defined | used to check whether a macro is not declared previously.
| 3 | #undef | undefine | used to undefine a previous defined macro.
| 4 | #endif | end if | used to terminate #ifdef statement.
| 5 | #elif | else if | used to declare second #ifdef (if first condition check fails).

## Syntax of Conditionals and examples :
### #ifdef
```c
	#ifdef macro_name
		macro_body
	#endif
```
```c
	#define SUM +

	#ifdef SUM
		#include<stdio.h>
	#endif

	int main(int argc, char const *argv[])
	{
		int result = 10 SUM 20;

		printf("10 + 20 = %d \n", result);

		return 0;
	}

```

### #undef
Used to undefine existing macro

```c
	#undef macro_name
```

```c
	#define SUM +

	#ifdef SUM
		#undef SUM
		#define SUM -
	#endif

	int main(int argc, char const *argv[])
	{
		// program will perform subtraction in place of addition.
		int result =  10 SUM 20;
		printf("10 + 20 = %d\n", result);

		return 0;
	}
```

### #ifndef
```c
	#ifndef macro_name
```
```c
	#ifndef SUM
	  #define SUM +
	#endif

	int main(int argc, char const *argv[])
	{
		int result = 10 SUM 20;

		printf("10 + 20 = %d\n", result);

		return 0;
	}
```

### #elif
```c
	#elif condition
		elif_body
```
```c
	#include<stdio.h>
	#define NUMBER 12

	#if NUMBER > 2
		#define SQUARE(x) x * x		
	#elif NUMBER == 2
		#define SQUARE(x) 2 * x
	#else
		#define SQUARE(x) x
	#endif

	int main(int argc, char const *argv[])
	{
		int result = SQUARE(2);
		printf("Square of 2 is %d\n",result);

		return 0;
	}

```

## Examples of Preprocessor Directives :
```c
	#define CUBE(x) x * x * x

	#ifndef CUBE
		#define CUBE(x) x * x * x
	#endif

	int main(int argc, char const *argv[])
	{
		int result = CUBE(2);
		printf("Cobe of 3 is %d\n", result);

		return 0;
	}

```

## Program to find max of 6 numbers using macro :
```c
#include<stdio.h>
#define MAX(a, b) (a) > (b) ? (a) : (b)

// Note in above case we used round brackets around a and b
// to prevent incorrect substitutuion.

int main(int argc, char const *argv[])
{
	int result = MAX(
			MAX(MAX(1, 2), MAX(4, 4)),
			 MAX(MAX(5, 6), MAX(7, 8))
			 );

	printf("result : %d\n",result);
	return 0;
}
```

# Pragma preprocessor (IDE Specific) :

```c
	#pragma startup Before
	#pragma exit After

	void Before(){
		printf("I am before main....\n");
	}

	int main(int argc, char const *argv[])
	{
		printf("inside main....\n");
		return 0;
	}

	void After(){
		printf("After main...\n");
	}

```
