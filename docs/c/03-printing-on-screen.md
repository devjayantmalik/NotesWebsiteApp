## Comments :
Comments are used to document our code, they help other programmers what our code is all about.

* Comments are not translated by compiler, they are deleted at time of compilation from output file.
* Source file will still contain comments, note that they are deleted from .exe or .out file

#### Single Line Comments :
Single line comments are started using double forward slashes and they are automatically terminated at end of line, means for termination you do not use any operator.

Syntax :
```c
int main() {
	// This is a single line comment.
	return 0;
}
```

#### Multi-line Comments :
Multi-line comments are used to document code that spans multiple lines.

* Nesting is not allowed in multi-line comments, that a comment cannot contain another comment within it, this happens only in case of multi-line comment.
* They starts with a forward slash and an asterisk symbol.
* They end using asterisk symbol followed by a forward slash.

Syntax :
```c
int main() {
	/* Hello
		This is a multiline comment.
	*/

	// Most commonly used as :
	/*
	* First line
	* Second line
	*/

	return 0;
}
```

## Why do we need to plan a c program?
-	We program in C because we want computer to do some task for us.

##	How do we program in C?
In order to program in c we have following instructions :

- Input Instructions (scanf)
- Output Instructions (printf)
- Conditional Instructions (while, if, for, loops)
- Declarative Instructions (variables, pointers)

##	Input Instructions :
- These instructions are required to take input from keyboard within our program.

## Output instructions :
- These instructions are required to print output to standard output device, that is monitor.

##	Conditional Instructions :
- These instructions are used to write repetition code and code that evaluates on conditions.

##	Declarative Instructions :
-	These instructions are used to reserve some memory in OS for our input.

> Note : One tab equals 8 spaces.

## Structure of C program :
```c
		header files
		global variables

		main function declaration
			{
				body of program.
			}
```

##	Example of C program :
```c
		#include<stdio.h> //header file

		int main() { 	//main function declaration

			printf("Hello World"); 	//print output on screen
			return 0;		//returns value back from function.

		}
```

## Addition in printf :

- More than one string passed passed to printf without commas will combine together to form a single string.

```c
		int main() {
			printf("Hello" "Jayant" "Malik");
			return 0;
		}
```

## Escape Sequences in printf :
-	Escape sequences are used to shift cursor position at specific location.

```c
		//escape sequences are used with backslash followed by specific letters.

		int main() {
			printf("Hello Jayant 1\n"); // prints a new line at end of text.
			printf("Hello Jayant 2\r"); // carriage return
			printf("Hello Jayant 3\b"); // backspace
			printf("Hello Jayant 4\t"); // tab
			return 0;
		}
```
> Note : Use manual of ANSI C for more escape sequence characters.

## Example of new line :
```c
		int main() {
			int a=0;  // local variable
			while(a<=10) {	// while loop
				a++;	// a = a+1
				printf("This is line no : %d\n", a);
			}
		}
```

## Example of carriage return
```c
		int main() {
			int x = 0;
			// in borland compiler use delay(milli_second) function
			// to understand it better or use a higher value of x in loop.
			while(x<=100){
				x++;
				printf("%d\r",x);
			}

			return 0;
		}
```

##	Example of Backspace Escape Sequence Character :
```c
		int main() {
			printf("Hello\b\b\b"); // shift cursor three position back.
			printf("AB");
			return 0;
		}
```

## Let's See Borland Compiler Specific Code
```c
		int main() {
			textcolor(10);	// sets text color
			textbackground(4)	// sets textbackground color\
			cprintf("Hello in Color");	// only works in borland
			delay(2000); //sets delay in milliseconds
			gotoxy(30,13); // changes cursor position (col, row)
		}
```

##	Let's Clear the Screen
-	clrscr is a function used to clear the screen  in DOS only.
- Think it as compiler specific code.

```c
		int main() {
			printf("India is great.");
			clrscr();
		}
```
