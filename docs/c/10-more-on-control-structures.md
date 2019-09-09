## Loop Control Structures :
Loop control structures are used to perform repetitive tasks.
> Example : to print table for any user provided number.

> Loops can be infinite, make sure to end loop at some point.

## Types of Loop Control Structures :
1. while
- do...while
- for

## while control structure :
while control structure is used to execute repetitive tasks, till the condition provided evaluates to non-zero

#### Syntax :
```c
int main() {

  while(expressions_that_evaluates_to_zero_or_non_zero){
    // statements to execute.
  }

  return 0;
}
```

#### Example :
```c
int main() {
  int number = 10;
  int index = 1;

  // loop to print table of any number.
  while(number <= 10){
    printf("%d x %d = %d\n", number, index, number * index);
    index++;
  }

  return 0;
}
```

```c
int main() {
  while(1, 2, 0){
      printf("Try to predict the output!\n");
  }

  return 0;
}
```

## do...while control structure :
do while control structure is used when we need to execute some task prior to checking condition and till the condition is met.

#### Syntax :
```c
int main() {

  do{
    // statements to execute.
  }while(expression_that_results_zero_or_non_zero_value);

  return 0;
}
```

#### Example :
```c
int main() {
  int user_choice = 0;

  do{

    printf("Choose a random number :\t");
    scanf("%d",&user_choice);

  }while(user_choice != rand() % 100);

  // rand() % 100 generates a random number between 0 and 100;

  return 0;
}
```

## for Control Structure :
for control structure is allows us to define initiation and final condition along with operation in same line.

> In older versions of C, initialization of variable is allowed only at top,
but in ANSI C17, variable can be declared at time of usage.

#### Syntax :
```c
int main() {

  for(initialization_expression; termination_expression; operation_expression){
    // statements to execute.
  }

  return 0;
}
```

#### Example :
```c
int main() {

  // prints counting from 0 to 99.
  for(int i=0; i<100; i++){
    printf("%d\t",i);
  }

  return 0;
}
```

> All three initiation, termination and operation section of for are optional.

#### for without initialization section :
```c
int main() {
  int i=0;

  for(; i<100; i++){
    printf("%d\t",i);
  }

  return 0;
}
```

#### for without termination section :
```c
int main() {

  for(int number = 0; ; number++){
    printf("%d\t", number);

    if(number >=99)
      break;
  }

  return 0;
}
```

#### for without operation section :
```c
int main() {

  for(int i=0; i<100; ){
    printf("%d\t",i);
    i++;
  }

  return 0;
}
```

#### for without any section :
```c
int main() {
  int i = 0;

  for(;;){
    if(i < 100)
      printf("%d\t",i++);
  }

  return 0;
}
```

#### Multiple expressions in for :
```c
int main() {
  int i=0;

  for(printf("initialization\n"), i = 0; printf("Condition Check\n"), i<5; printf("Operation\n"), i++){
    printf("Inside body of if\n");
  }

  return 0;
}
```

> The above program verifies that we could have multiple expressions in if.

> the expressions are evaluated from left to right due to associativity of comma.

#### Working of for :
1. initialization Occurs
- Termination Condition is Checked
- Body is executed
- Operation section is executed, means value is incremented or decremented.

```c
int main() {
  int i=0;

  for(printf("initialization\n"), i = 0; printf("Condition Check\n"), i<5; printf("Operation\n"), i++){
    printf("Inside body of if\n");
  }

  return 0;
}
```
