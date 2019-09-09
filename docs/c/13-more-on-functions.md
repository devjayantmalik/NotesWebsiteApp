## Stack Concept :
1. STACK is a part in RAM reserved by OS to keep account of program.

- OS manages program execution with the help of STACK.

- OS stores program execution in STACK.

- Top most stack section is always executed first.

- Once a function execution finishes STACK memory is cleaned for that specific function (removal is called as pop)

## Concept of STACK with function calls :
Best way to understand the concept is to see it in action.

#### Example :
```c
	int max(int a, int b){
		return (a >b) ? a : b;
	}

	int main(){
		int firstNumber  = 0;
		int SecondNumber = 0;

		printf("Enter First Number: ");
		scanf("%d",&firstNumber);

		printf("Enter Second Number: ");
		scanf("%d",&secondNumber);

		int result = max(firstNumber, secondNumber);

		printf("Maximum of %d and %d is : %d\n",firstNumber,secondNumber,result);

		return 0;
	}
```

#### Steps of Execution are :
1. Main function is loaded in STACK.

- Local variables are created in STACK.

- Value is assigned to local variables.

- Value of address from where program left execution is stored in register.

- For printf seperate STACK section is created, because it is a function.

- Now printf execution completed, so STACK memory for printf is popped.

- Again program continues execution from main function.

- scanf is a function so, seperate STACK section is created for it.

- scanf execution completes with some value assigned to variable, so STACK memory is popped again.

- Steps 4 to 9 repeats again for second number input.

- Program Execution leaving address is again stored in STACK or register.(but for now say stack)

- Now max function is created in STACK, with two variables a and b.

- Values from main function are copied in max function.

- Program calculates result based on condition.

- Value is returned to main function and STACK is popped.

- and so on...... the process continues till end of program.

>### Note : Only USER-DEFINED functions are shown in images.
>#	//Add image here.

## Why is main function declared with int return type?
- Every program has to return some value back to Operating System

- This information is stored in a variable, named errorlevel (in case of windows only)

- View info of this variable using : echo %errorlevel% (on windows)
#### The above case can also be detected by using debugger because improper termination of program creates a dump file.

## Call by Reference functions :
The functions that takes pointer as formal argument and address as actual argument are called as call by reference functions.

```c
	int sum(const int * first, const int * second){
		return first + second;
	}

	int main(int argc, char const *argv[])
	{
		int num1 = 10 , num2 = 20;

		int result = sum(&num1, &num2);
		printf("%d + %d = %d\n", num1, num2, result);

		return 0;
	}

```

## Notable points about call by reference :
1. There is formation of one variable as pointer in stack.

- Size of pointer depends on bits of compiler .

- (16bit - 1 byte), (32bit - 4 bytes), (64bit - 8 bytes).
- In case of passing arrays to functions this method saves lot of memory space and processor computing power.

### Sample 1 :
```c
	void print(char name[], int salary){
		printf("Your name is %s and monthly pay is %d", name, salary);
	}

	int main(int argc, char const *argv[])
	{
		char name[20] = "Jayant Malik";
		print(name, 20000);

		return 0;
	}

	// Memory Usage by print : 20 bytes for name + 4 bytes for int(64 bit compiler).
```
### Sample 2 :
```c
	void print(const char *name, int salary){
		printf("Your name is %s and monthly pay is %d", name, salary);
	}

	int main(int argc, char const *argv[])
	{
		print("Jayant Malik", 20000);
		return 0;
	}
	//memory usage by print : 8 bytes for name + 4 bytes for int.

```

## Call by Value Functions :
Functions that takes original datatype as actual argument and direct values as actual argument.

```c
	int sum(int first, int second){
		return first + second;
	}

	int main(int argc, char const *argv[])
	{
		int result = sum(10, 20);
		printf("10 + 20 = %d\n", result);

		return 0;
	}

```

## Notable points about Call by value functions :

1. Actual value of variable is copied in stack.

- Not access to change value of variable in local scope of parent calling function.

- In case of array extra memory usage takes place.

## Nested function declaration :
when a function is declared inside function then it is called as nested function declaration.

```c
	int main(int argc, char const *argv[])
	{
		int sum(int a, int b){
			return a + b;
		}

		int result = sum(10, 20);
		printf("10 + 20 = %d\n",result);

		return 0;
	}


```

## Recursive function :
when same function again from same calling function then it is called recursion.

Output of recursion is determined using stack.

```c
	void temp(int number){
		number--;

		if(number > 0){
			temp(num);
		}
	}
	int main(int argc, char const *argv[])
	{
		temp(3);
		return 0;
	}

```
