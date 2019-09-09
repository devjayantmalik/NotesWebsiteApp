## Software Engineer :
* A person who has knowledge of programming is a software engineer.
* sometimes also called as software scientist.
* Software Scientist > Software Vendor > Software user > Software end user.
* Software Scientist (Software creator) : creates software or technology.
* Software Vendor: distribute technology on behalf of software creator.
* Software User: Uses technology to create bulk products
* Software End user: uses technology product created

## Technology:
Creation of some product or project is technology.
1. Tech Creator created a technology.( Thomas created technology to make bulbs)
2. Vendor distributed that technology.. (Let's say xyz)
3. User used that technology to create in bulk (Philips company workers)
4. End user used that product (We light our homes with bulb)

## History of C :
- Unix was first Developed by Ken Thompson in posix.
- The language was not able to fix all issues in linux.
- Now Ken Thompson needed a language to rewrite linux.
- Writing a new language will take a lot of time so,
- He took help of his junior Dennis R. Ritche.
- Ken Thompson told Dennis what he wanted to do with Language
- and Dennis wrote all functionalities what Ken wanted.
- Now Language was written and it was ready to used.
- Ken Thompson rewrote the entire OS in C.

- After 2 years he released Unix (Portable and multi-tasking)
- The Problem was that linux was 16 bit.
- So, it was slow.
- We needed some OS that works fast.
- Richard was 12 years old student who learnt C and was from New Zealand.
- He told people that OS could work on 32 bit.
- People did not believe him. He wrote one linux command in 32 bit and proved that it could be written in 32 bit.
- Richard gathered people who were familiar with C and asked each of them to write one command in 32 bit so, Linux become OS of community and was written in C.

## What is 16 bit?
- The one cycle of Processor to work is called tic.
- If any OS completes 16 bit of Work in one cycle then it is called 16 bit.

## Summary :
- Unix was created by Ken Thompson.
- Dennis Ritche created C language.
- Unix was 16 bit
- Linux was 32 bit written by community and started by Richard.

## Let's Discuss about C
* Inclusion of 'stdio.h' in not necessary.
* Follow ANSI Standard.
* Case sensitive language.
* Most of built in functions are in small case.

## Requirements to run C program on machine.
1. Text Editor
2. Compiler
3. API (Application Programming Interface)
4. Debugger
5. Manual

## Who will provide me all these things?
Tech Creator or Tech Vendor.

## Software could be categorised in two parts :
* Software Projects
* Software Products

## Software Projects:
* Software Projects are made for specific purpose and are available to specific person even after completion of software by developer.
* Example - Metro Ticketing System.
* It could be only by metro employees. You can take tickets but cannot use software to issue tickets.

## Software Products:
*	Software Products are, those software which are made for general purpose, and are available to a wide range of persons.
*	Example- Microsoft Word, Paint, Tally, VLC, AllPlayer, etc...
*	These software could be used by anyone for their own purposes.

|	Before Completion|After Completion|  Called As
|---------|-----------|-----------
|Project 	|Project 		|Project
|Project  |Product 		|Product

## C Program
```c
		#include<stdio.h>

		int main() {
			printf("Hello World\n");
			return 0;
		}
	```

## C Program Explanation:
Header files Contain pre-built functions prototypes and macros for us.

* These are included using a reserved keyword #include<Filename.h>
*	main is entry point of our C program. Every program should have a main function.
*	In our case main returns an integer value.
*	return is a reserved keyword in C to return a value back from function.
*	printf is a function used to print some output to screen.
*	Statement Terminator ';' or semicolon is used to terminate c Statement.
