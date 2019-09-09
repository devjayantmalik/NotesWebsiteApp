## Definition
Special kind of symbols that are part of ASCII characters and have specific meaning in programming language are called as operators.

> +, -, /, * are examples of  operators.

## Types of operators based on inputs:
  1. Unary Operators
  - Binary Operators
  - Terniary Operator

## Unary Operators
The operators that takes single input are called as unary operators.

Example :
> ! not operator.

```c
int main() {
  int status = 1;

  if(!status){ // converts status value to zero.
    // body will not execute in this case.
  }
}

```

## Binary Operators
The operators that takes two inputs are called as binary operators.

Example:
> result = 20 + 30;

> '+' plus operator takes two input.

> '-' minus operator takes two input.

```c
int main() {
  int age = 10; // assignment operator.
  int sum = age + 10; // plus operator
  float salary = 10 * 90; // multiplication operator
  double length = 200 / 10; // divide operator.

  /* Some short operators*/
  length += 2; // equivalent to length = length + 2;
  length++; // equivalent to length = length + 1;
  age--;
  sum -= 2;
  salary *= 0.20f;
  salary /= 2;
  return 0;
}
```
## Terniary Operator
The operator that takes three inputs are called as terniary operators.
> They are mainly used in place of if else.

Syntax :
> (expression_returning_zero_or_one) ? true_case : false_case;

Example :
> int result = (10 > 20) ? 1 : 0;

> ?: is a terniary operator

```c
int fact() {
  // code to find factorial.
}

int main() {
  int number = 0;

  printf("Enter a number to calculate factorial:\t");
  scanf("%d",&number);

  int result = (number != 0) ? fact(number) : 1;

  printf("%d factorial is %d:\n", number, result);

  return 0;
}
```

## Post-fix and prefix unary operators :
### Post-fix unary :
These operators are mainly placed after a variable.

> number++;

In case of post-fix, there is formation of temporary memory location and in this temporary location the original value of operator is stored.

#### Working of post-fix :
```c
  int main() {
    int marks = 65;
    printf("postfix : %d\n",marks++); // result is 65.

    return 0;
  }
```

1. Create a temporary memory location to store original value present in variable.
2. Increments the original value.
3. Returns value stored at temporary memory location created in step 1.

## Prefix unary operator :
These operators are placed before a variable.
> ++number;

In case of prefix unary operator, original variable is incremented or decremented, there is no formation of temporary memory.

#### Working of prefix :
```c
int main(){
  int number = 100;
  printf("prefix: %d\n",++number); // result is 101

  return 0;
}
```
1. Increment the original value.
2. Returns the incremented value.

## Types of operators :
  1. Arithmetic Operators.
  2. Relational Operators.
  3. Logical operators
  4. Bitwise Operators.

## Arithmetic Operators :
The operators used to perform simple
mathematical arithmetic.
> '+', '-', '*', '/', '%'

```c
int main() {
  int number1 = 0;
  int number2 = 0;

  printf("Enter first number :\t");
  scanf("%d",&number1);

  printf("Enter first number :\t");
  scanf("%d",&number2);

  int addition = number1 + number2;
  int subtraction = number1 + number2;
  long int multiplication = number 1 * number2;
  float division = number1 / number2;
  int remainder = number1 % number2;

  printf("Addition : %d\n", addition);
  printf("Subtraction : %d\n", subtraction);
  printf("Multiplication : %ld\n", multiplication);
  printf("Division : %f\n", division);
  printf("Remainder : %d\n", remainder);

  return 0;
}
```

## Relational Operators :
The operators that used to check relations between two values.

> '>', '<', '>=', '<=', '==', '!='

```c
int main() {
  int num1 = 10;
  int num2 = 20;

  printf("Greater than : %d\n", num1 > num2);
  printf("Less than : %d\n", num1 < num2);
  printf("Greater or Equal : %d\n", num1 >= num2);
  printf("Less or Equal : %d\n", num1 <= num2);
  printf("Equals to : %d\n", num1 == num2);
  printf("Not Equals : %d\n", num1 != num2);

  return 0;
}
```

## Logical Operators :
These operators are used to check for logical conditions, such as : and or.

> '&&' and operator
> '||' or operator

```c
int main() {
  int age = 0;

  printf("Enter your age:\t");
  scanf("%d",&age);

  if(age > 18 && age < 50){
    printf("You are eligible for voting.\n");
  }

  if(age < 18 || age > 50){
    printf("You are not eligible for voting.\n");
  }

  return 0;
}
```

### Evaluation of logical operators :
The logical operators are evaluated based on physics gate table.

#### Logical And :
| Condition 1 | Condition 2 | Result |
| :---------- | :---------- | :----- |
|      1      |      1      |    1   |
|      1      |      0      |    0   |
|      0      |      1      |    0   |
|      0      |      0      |    0   |

#### Logical Or :
| Condition 1 | Condition 2 | Result |
| :---------- | :---------- | :----- |
|      1      |      1      |    1   |
|      1      |      0      |    1   |
|      0      |      1      |    1   |
|      0      |      0      |    0   |

## Bitwise Operators :
* These operators works only on binaries, that is zero and one, of their operands.
* The value on which operator operates is called as operand.

> '>>' left binary shift operator.
> '<<' right binary shift operator.
> '|' bitwise or operator.
> '&' bitwise and operator.
> '^' bitwise exclusive or
> '~' bitwise exclusive not.

Example :
```c
int main() {
  printf("%d\n", 3 << 5);

  return 0;
}
```

### Bitwise OR
Denoted by a '|' (pipe) symbol.

#### Working of Bitwise OR :
* takes two number as input.
* Converts both numbers to binary.
* Compares each digit of binary,
* if any of digit is found to be 1 result is 1.

#### Table of output :
| First Input | Second Input | Output
| :---------- | :----------- | :-------
|      0      |      0       |    0
|      0      |      1       |    0
|      1      |      0       |    1
|      1      |      1       |    1

#### Example of Bitwise OR :
```c

// bitwise or
void or() {
	int result = 1 | 5;
	/*
	* 128 64 32 16 8 4 2 1

	*  0  0  0  0  0 0 0 1 Equals 1.
	*  0  0  0  0  0 1 0 1 Equals 5
	* =============================
	*  0  0  0  0  0 1 0 1 Equals 5
	*/
	printf("1 | 5 = %d\n", result);

	result = 15 | 8;
	/*
	*  128 64 32 16 8 4 2 1

	*   0   0 0  0  1 1 1 1 Equals 15
	*   0   0 0  0  1 0 0 0 Equals 8
	* ===============================
	*   0   0 0  0  1 1 1 1 Equals 15
	*/
	printf("15 | 8 = %d\n", result);
}

int main(){
  or();
  return 0;
}
```

### Bitwise And
Denoted by a '&' (and / address of) symbol.

#### Working of Bitwise And :
* takes two number as input.
* Converts both numbers to binary.
* Compares each digit of binary,
* if any of digit is found to be 0 result is 0.

#### Table of output :
| First Input | Second Input | Output
| :---------- | :----------- | :-------
|      0      |      0       |    0
|      0      |      1       |    0
|      1      |      0       |    0
|      1      |      1       |    1

#### Example of Bitwise And :
```c
// Bitwise and
void and() {

	int result = 2 & 5;
	/*
	* 128 64 32 16 8 4 2 1  Places.

	*  0   0  0  0 0 0 1 0  Equals 2
	*  0   0  0  0 0 1 0 1  Equals 5
    * ==============================
	*  0   0  0  0 0 0 0 0 Equals zero.
	*/
	printf("2 & 5 is %d\n", result);

	result = 1 & 5;
	/*
	* 128 64 32 16 8 4 2 1 Places

	*  0   0  0  0 0 0 0 1  Equals 1
	*  0   0  0  0 0 1 0 1  Equals 5
	* ===============================
	*  0   0  0  0 0 0 0 1  Equals 1
	*/

	printf("1 & 5 Equals : %d\n", result);

}

int main() {
  and();
  return 0;
}

```

### Bitwise XOR
Denoted by a '^' (power) symbol.

#### Working of Bitwise XOR :
* takes two number as input.
* Converts both numbers to binary.
* Compares each digit of binary,
* if both digit of first and second numbers are different,
* result is 1 else 0

#### Table of output :
| First Input | Second Input | Output
| :---------- | :----------- | :-------
|      0      |      0       |    0
|      0      |      1       |    1
|      1      |      0       |    1
|      1      |      1       |    0

#### Example of Bitwise xor :
```c
// Bitwise exclusive or
void xor() {
	/*
	* xor gives 1 only where,
	* first binary is different,
	* from second binary at same place.
	*/
	int result = 2 ^ 5;
	/*
	* 128 64 32 16 8 4 2 1 Places

	*  0   0 0  0  0 0 1 0 Equals 2
	*  0   0 0  0  0 1 0 1 Equals 5
	* ================================
	*  0   0 0  0  0 1 1 1 Equals 7
	*/
	printf("2 ^ 5 = %d\n", result);

	result = 13 ^ 16;
	/*
	* 128 64 32 16 8 4 2 1 Places

	*  0   0  0  0 1 1 0 1 Equals 13
	*  0   0  0  1 0 0 0 0 Equals 16
	* =================================
	*  0   0  0  1 1 1 0 1 Equals 29
	*/
	printf("13 ^ 16 = %d\n", result);
}

int main() {
  xor();
  return 0;
}
```

### Bitwise NOT
Denoted by a '~' (tilde) symbol.

#### Working of Bitwise NOT :
* takes one number as input.
* Converts the number to binary.
* Reverses the bits of the number
* Again, bits are reversed except sign bit.
* Now, one is added to the number.

#### Example of Bitwise NOT :
```c
// bitwise not
void not() {
	int result = ~5;
	/*
	* 128 64 32 16 8 4 2 1 Places

	*  0  0  0   0 0 1 0 1 Equals 5
	*  ============================
	*  1  1  1   1 1 0 1 0 Equals 250 // bits reversed
	*  1  0  0   0 0 1 0 1 Equals -5  // again reversed except sign bit
	*  1  0  0   0 0 1 1 1 Equals -6  // 1 is added to number.
	*/
	printf("~5 = %d\n", result);

	result = ~14;
	/*
	* 128 64 32 16 8 4 2 1 Places

	*  0  0  0  0  1 1 1 0 Equals 14
	*  1  1  1  1  0 0 0 1 Equals 241
	*  1  0  0  0  1 1 1 0 Equals -14
	*  1  0  0  0  1 1 1 1 Equals -15
	*/
	printf("~14 = %d\n", result);
}

int main() {
  not();
  return 0;
}
```

### Bitwise left shift
* Denoted by a '>>' (left stream operator) operator.
* Works only on positive values.
* left side denotes the number
* right side denotes the no. of bits to shift.

#### Working of Bitwise left shift :
* takes two numbers as input.
* Converts the number to binary.
* Shifts the numbers binary towards left,
* by number of bits provided as second input.

#### Example of left shift :
```c
void leftshift() {
	unsigned int result = 4 << 1;
	/*
	* 128 64 32 16 8 4 2 1 Places

	*  0   0 0   0 0 1 0 0 Equals 4
	*  ==============================
	*  0   0 0   0 1 0 0 0 Equals 8
	*/
	printf("4 << 1 = %d\n", result);

	result = 15 << 4;
	/*
	* 128 64 32 16 8 4 2 1 Places

	*  0   0  0  0 1 1 1 1 Equals 15
	* ============================
	*  1   1  1  1 0 0 0 0 Equals 240
	*/
	printf("15 << 4 = %d\n", result);

}

int main() {
  leftshift();
  return 0;
}
```

### Bitwise right shift :
* Denoted by a '<<' (less than less than) operator.
* Works only on positive values.
* left side denotes the no. of bits to shift.
* right side denotes the number

#### Working of Bitwise right shift :
> takes two numbers as input.
> Converts the number to binary.
> Shifts the numbers binary towards right,
> by number of bits provided as first input.

#### Example of right shift :
```c

void rightshift() {
	int result = 4 >> 1;
	/*
	* 128 64 32 16 8 4 2 1

	*  0   0 0   0 0 1 0 0 Equals 4
	*  ==============================
	*  0   0 0   0 0 0 1 0 Equals 2
	*/
	printf("4 >> 1 = %d\n", result);

	result = 15 >> 4;
	/*
	* 128 64 32 16 8 4 2 1

	*  0   0  0  0 1 1 1 1 Equals 15
	* ============================
	*  0   0  0  0 0 0 0 0 Equals 0
	*/
	printf("15 >> 4 = %d\n", result);

}

int main() {
  rightshift();
  return 0;
}
```
