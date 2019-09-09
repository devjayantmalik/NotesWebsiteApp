## Structures in C :
structures are user defined datatype used for storing entities of data. Entity is any real world physical thing.

## Why we need structures ?
1. In order to store data in a single unit form.

- To create our own user defined datatype.

- To create memory location for different datatype in sequential order.

- To store details of some object.

- Example : storing id name and age of a student.

## Where structure could be useful ?
1. Let's say we need to store student name and age, then c program for it could be like this without structure :

```c
	int main(){
		char name[20];
		int age;

		printf("Enter student name :\t");
		scanf("%s",name);
		// remember array name itself holds memory address of base location or address of zero index element.

		printf("Enter student age :\t");
		scanf("%d",&age);

		printf("%s has age of %d",name,age);

		return 0;
	}

```
2. In order to keep details of student in such manner, c does not guarantee us that name and age variable will be in sequential order.

## Real Life usage of Structures :
	1. In order to create a metro ticketing system, developers needed a tool to store data about issuer, client, price, from, to, and so many other details. So, they used structures to implement the same.

	2. facebook uses structures to store data of person, posts, comments....

	3. Telecom company uses structures to store data...

## How does a structure looks :
```c
	struct Rect{
		double breadth;
		double length;
	}

	typedef struct Rect Rect;

	int main(){
		Rect x;

		x.length = 100;
		x.breadth = 200;

		printf("Rect has length %ld and breadth %ld\n", x.length, x.breadth );
		return 0;
	}


```

## Syntax of Structure Definition :
```c
	struct structure_name{
		datatype value1;
		datatype value2;
		datatype value3;
	};

	// Example
	struct Rectangle{
		double length;
		double breadth;
	};

```

## Syntax of Structure with variables inside code :
```c
	int main(){
		struct structure_name variable_name;

		//Example
		struct Rectangle rect1;

		return 0;
	}

```

## Accessing Elements of Structure :
```c
	int main(){
		struct Rectangle rect1;

		printf("Length = %ld\n",rect1.length);
		printf("Breadth = %d\n",rect1.breadth);

		return 0;
	}

```
## Rules for structures :
1. Naming of structure is same as variable name.

- Structure definition starts with struct reserved keyword of c.

- Structure definition ends with a semicolon.

- Structure could contain different datatypes.

- Structures are accessed using direct member accessor operator (.) or period.

- Structures are could also be accessed using indirect member accesor operator ( -> )

- Variables inside body of structure are allocated sequential poitions.

- Function declaration is not allowed inside structures.

- Structures are used to create variables of own defined type with a specific syntax (struct struct_name variable_name );

- Variables in body of structure cannot be assigned direct values.

- By default all elements of structure gets garbage value.

- Structure name is mapped to first element in struct.

## Example of struct
```c
	struct Rect{
		double length;
		double breadth;
	};

	int main(){

		struct Rect rect1;

		// garbage value proof.
		printf("Length : %ld and Breadth : %ld\n",rect1.length, rect1.breadth);

		// set custom values to rect1

		rect1.length = 100;
		rect1.breadth = 200;

		printf("Length : %ld and Breadth : %ld\n",rect1.length, rect1.breadth);

		return 0;
	}


```
## Direct Member accessor operator / Direct Component selector operator:
1. period or dot is called as direct member accessor operator.

- It is a binary operators means, requires two inputs :

- first input : variable_name

- second input : property name or struct member name.

## Memory Formation of Structure :
	example :
```c
	struct Sample{
		char grade;
		char blood_group;
	};
```

	Memory:				[][][][][][][][]	[][][][][][][][][]
	Variable				grade				blood_group		
	Address 				520620				520621
	Size					 1 byte					1 byte

#### Total size of structure depends on datatypes used inside body of struct.

## Preventing use of struct every time we create a variable :
```c
	struct Rect{
		double length;
		double bredth;
	};

	typedef struct Rect Rect;

	int main(int argc, char const *argv[])
	{
		Rect rect1;

		rect1.length  = 10;
		rect2.breadth = 20;

		printf("length : %ld, breadth : %ld\n",rect1.length, rect2.length);

		return 0;
	}

```
## Another syntax of using typedef :
```c
	//direct use of typedef to create struct.

	typedef struct{
		double length;
		double breadth;
	} Rect;

	int main(){
		Rect rect1;
		// some related code.
		return 0;
	}

```

## Using Functions to Print Elements of structure :
```c
	struct Rect{
		int length;
		int breadth;
	};

	typedef struct Rect Rect;

	void display(Rect rect){
		printf("length : %d, breadth : %d\n", rect.length, rect.breadth);
	}

	int main(int argc, char const *argv[])
	{
		Rect rect1;
		Rect rect2 = {100, 200};

		rect1.length = 20;
		rect1.breadth = 30;

		// code consumes high memory due to clone formation in stack.

		display(rect1);
		display(rect2);

		return 0;
	}


```

## Advantages of use with pointers :
1. Less memory space is required by application.

- Cloning of struct datatype is prevented.

- Variables in local scope could be manipulated.

- Reduces number of operations in STACK formation.


## Pointers with struct :
```c
	typedef struct{
		int length;
		int breadth;
	} Rect;

	int main(int argc, char const *argv[])
	{
		Rect rect1;
		Rect *ptr;

		ptr = &rect1;

		ptr->length = 100;
		ptr->breadth = 200;

		printf("Length : %d and Breadth : %d\n",rect1.length, rect1.breadth);

		return 0;
	}

```
## Indirect Member Access Operator/ Indirect Component Selector Operator ( -> ):

1. It is a binary operator, hence takes two inputs

- first : address of variable
- second : member of struct.

## Difference in size of pointers and struct :
```c

	typedef struct{
		int length;
		int breadth;
	} Rect;

	int main(int argc, char const *argv[])
	{
		Rect rect1;
		Rect *ptr;

		printf("Size of rect1 is %lu bytes\n", sizeof(rect1));
		printf("Size of ptr is %lu bytes\n", sizeof(ptr));

		return 0;
	}
```

## Passing pointers to functions

```c
	typedef struct{
		int length;
		int breadth;
	} Rect;

	void print_data(Rect * ptr){
		printf("length : %d, breadth : %d\n",(*ptr).length, ptr -> breadth);
	}

	int main(int argc, char const *argv[])
	{
		Rect rect1 = {10, 20};

		print_data(&rect1);

		return 0;
	}

```

## program to get data from user and store in variable :
```c
	typedef struct{
		int length;
		int breadth;
	} Rect;

	void get_data(Rect *rect){
		printf("Enter length :\t");
		scanf("%d",&rect->length);

		printf("Enter breadth:\t");
		scanf("%d",&rect->breadth);
	}

	void print_data(Rect *rect){
		printf("length : %d, breadth : %d\n",(*rect).length, rect->breadth);
	}

	int main(int argc, char const *argv[])
	{
		Rect rect1;
		Rect rect2;

		get_data(&rect1);
		get_data(&rect2);

		print_data(&rect1);
		print_data(&rect2);

		return 0;
	}

```

## Return data from user defined function :
```c

	// write a program in c to compare two rectangles.
	struct Rect{
		int length;
		int breadth;
	};

	typedef struct Rect Rect;

	Rect * compare(Rect const *rect1, Rect const *rect2){
		int area1 = rect1->length * rect1->breadth;
		int area2 = rect2->length * rect2->breadth;

		return (area1 > area2) ? rect1 : rect2;
	}

	int main(int argc, char const *argv[])
	{
		Rect rect1 = {100, 200};
		Rect rect2 = {200, 400};

		Rect const * result = compare(&rect1, &rect2);

		printf("length : %d, breadth : %d\n",result->length, result->breadth);

		return 0;
	}
```

## Write a program in c to add two rectangles :
```c
	struct Rect{
		int length;
		int breadth;
	};

	typedef struct Rect Rect;

	Rect add_rectangle(const Rect *rect1, Rect const *rect2){
		Rect temp;

		temp.length =  rect1 -> length + rect2 -> length;
		temp.breadth = rect1 -> breadth + rect2 -> breadth;

		return temp;
	}

	int main(int argc, char const *argv[])
	{
		Rect rect1 = {10, 20};
		Rect rect2 = {50, 60};

		Rect resultant = add_rectangle(&rect1, &rect2);

		printf("Resultant Rectangle, length : %d and breadth : %d\n",
			resultant.length, resultant.breadth);

		return 0;
	}
```

## Write a program in c to store data of 10 employees.
```c
#include<stdio_ext.h>
#define NUMBER_OF_CLIENTS 10
// could create seperate header file for this info.

	struct Employee{
		char name[20];
		int age;
		int salary;
	};			
	typedef struct Employee Employee;

void getClientData(Employee *client){
	printf("Enter employee name :\t");
	scanf("%s",&client->name);
	__fpurge(stdin);

	printf("Enter employee age :\t");
	scanf("%d",&client->age);
	__fpurge(stdin);

	printf("Enter employee salary :\t");
	scanf("%d",&client->salary);
	__fpurge(stdin);
}

int main(int argc, char const *argv[])
{
	Employee client[NUMBER_OF_CLIENTS] = {"", 0, 0};
	int index = 0;

	while(1){
		printf("Enter y to add record and q to quit..\t");
		char ch = getchar();

		if(ch == 'q')
			break;

		getClientData(&client[index]);
		index++;
	}

	for(int i = 0; i <2; i++){
		printf("%s, %d, %d\n",client[i].name, client[i].age, client[i].salary);
	}

	return 0;
}
```
