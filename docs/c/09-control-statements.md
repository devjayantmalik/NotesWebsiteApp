## Control Statements
The statements that are used to control flow of execution of program are called as control statements.

## Types of Control Statements :
1. Selection Control Structures
2. Loop Control Structures

## Selection Control Structures :
The control structures that allows us to execute actions based on a condition, provided by us, are called as selection control structures.

Or, When the selected statements are executed based on some condition then selection control structures are used.

## Types of Selection Control Structures :
1. if....else
- switch...case
- '?:' (terniary)

## if else selection control structure :
if else control structure is used, when we need to execute some tasks, based on the expression, that results zero or non-zero value.

#### Syntax of if :
```c
int main() {

  // syntax :
  if(expression_resulting_zero_or_non_zero){
    // Note : Every non- zero number is treated as 1.
    // multiple expressions are allowed, seperated with commas.
  }

  // usage :
  if(0){
    // statements inside body of if, will not execute.
  }

  // usage :
  if(1){
    // statements inside body of if, will execute.
  }

  return 0;
}
```

#### Examples of if :
```c
int main() {
  int login_status = 0;

  // only if.
  if(login_status != 1){
    printf("You are not allowed to access this system.\n");
  }  

  return 0;
}
```

```c
int main() {
  int login_status = 0;

  //if with else
  if(login_status != 1){
    printf("You are not allowed to access this system.\n");
  }
  else {
    printf("Access granted..\n");
  }

  return 0;
}
```

```c
int main() {
  int login_status = 0;

  //if without else
  if(login_status != 1){
    printf("You are not allowed to access this system.\n");
  }

  if(login_status == 1)
  {
    printf("Access granted..\n");
  }

  return 0;
}
```

```c
int main() {
  int login_status = 0;

  //if with else
  if(login_status == 0){
    printf("You are not allowed to access this system.\n");
  }
  else if(login_status == 1){
    printf("Access granted..\n");
  }
  else{
    printf("We have secured our system, from this hack.\n");
    printf("Your identity have been reported to security agency.\n");
  }

  return 0;
}
```

#### Notable Points about if...else in above example:
1. else is a reserved keyword that is optional to use with if.
- else is used to connect another if with previous if.

#### Multiple Expressions with if :
We could use multiple expressions with if :
> Body of if is always evaluated as per the last value.

```c
int main() {
  if(0, 1, 0){
    printf("I will not get printed.\n");
  }

  if(1, 0, 1){
    printf("I will get printed.\n");
  }

  return 0;
}
```

> Expression is always evaluated from left to right because, rule of Associativity of comma is left to right.

```c
int main() {

  if(printf("First\n"), printf("Second\n"), printf("Third\n")){
    printf("Let's have a look in depth.\n");
  }

  return 0;
}
```

#### Nested if
When if statements is used inside body of another if, it is called nested if.

```c
int main() {
  if(1) {

    if(1){ // this is nested if
      printf("I am present inside body of if.\n");
    }

  }
}
```

## Switch Case Control Structure :
switch case control structure is used, when we have possible combinations, prior to writing our c program.

> Example : Cities of students, studying in a school.

Syntax :
```c
int main() {

  switch(expression_with_some_value) {
    case value : statements_to_execute; break;
    case value : statements_to_execute; break;
    default:
      statements_to_execute
  }

  return 0;
}
```

Example :
```c
int main() {

  switch(1){
    case 1: printf("Value is 1\n"); break;
    case 2: printf("Value is 2\n"); break;
    default :
      printf("Value does not match any above case.\n");
  }

  return 0;
}
```

#### Explanation of each part in  switch case :
```c
int main() {
  int x = 10;

  switch(x){
    case 1: printf("Hello");
  }

  // here x, is the value that will be used to match with every case.
  // os tries to match value of x with 1 and if both of them are found to be same, then printf("Hello"); will be executed.

  return 0;
}
```

```c
int main() {
    int roll_no = 2;

    switch(roll_no){
      case 2 : printf("Student Name: Arnav\n"); break;
      // In above case break keyword is used to exit execution of switch case.
      // Means other cases after matching case will not be evaluated.
    }

  return 0;
}
```

```c
int main() {
  int record_no = 10;

  switch(record_no){
    case 1: printf("Name: Rahul, Salary : 1000\n"); break;
    case 2: printf("Name: Amit, Salary : 1000\n"); break;
    case 3: printf("Name: Suraj, Salary : 1000\n"); break;
    default :
      printf("Sorry, record not found.\n");
  }

  return 0;
}
```

> break is used to exit out of switch body.

> statements associated with default are executed only if, any of the above cases do not match.

## Ternary Control Structure :
Ternary control structure is used, in place of if..else, In fact, it is short form of if..else.
It is ternary operator.

```c
int main() {
  int marks = 10;

  int interview_eligibility = (marks > 60) ? 1 : 0;

  if(interview_eligibility)
    printf("Please visit administrator block at 6, for interview.\n");
  else
    printf("You are not eligible for interview.\n");

  return 0;
}
```
