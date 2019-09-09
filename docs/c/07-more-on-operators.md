## Some facts :
> printf() returns number of characters printed on screen.

> if() could have multiple expressions separated by commas

## Short Circuit behaviour of && :
The and operator will not evaluate other expressions if, any expression, that comes first, is evaluates to zero value.
> Inside if the expressions are evaluated from left to right.

```c
int main() {
  int num1 = 10;
  int num2 = 20;

  // simple usage of if
  if((num1 != 0) && (num2 != 0))
    printf("Number one and two are non-zero\n");

  // Verification of short behaviour
  // Output : We are inside body of if...
  if(printf("") && printf("Second")){
    printf("\nWe are inside body of if...\n");
  }

  return 0;
}
```

## Short circuit behaviour of || :
The or operator will not evaluate expressions futher, if any expression, that comes first, evaluates to non-zero value.

```c
int main() {
  int num1 = 10;
  int num2 = 20;

  // simple usage of if
  if((num1 != 0) || (num2 != 0))
    printf("Number one and two are non-zero\n");

  // Verification of short behaviour
  // Output : First
  if(printf("First") || printf("Second")){
    printf("\nWe are inside body of if...\n");
  }

  return 0;
}
```

## How operators are evaluated ?
The operators are evaluated based on precedence table.

If you find same operators in a expression then, rule of Associativity is applied.

Example :
> int age = 10 + 20 + 30 + 40;

## Rule of Precedence and Associativity
Rule of precedence, defines the order, in which OS evaluates operators in an expression.

There is a precedence table for this task.
> ANSI has changed precedence table in different versions of C language.

Example:
> int age = 10 + 20 - 30 * 40;

Rule of Associativity, defines the direction, in which OS evaluates expression with same operators.

Example:
> int age = 10 + 20 + 30 + 40;

| Precedence |     Operator   |      Description       | Associativity |
| :--------- | :------------  | :--------------------- | :------------
|    01      |     ++, --     | Postfix                | Left to Right |
|    01      |      ()        | Function Call          | Left to Right |
|    01      |      []        | Array Subscripting     | Left to Right |
|    01      |      .         | Direct Member Access   | Left to Right |
|    01      |      ->        | Indirect Member Access | Left to Right |
|    01      |  (type){list}  | Compound Literal       | Left to Right |

| Precedence |     Operator   |          Description        | Associativity |
| :--------- | :------------  | :-------------------------  | :------------
|    02      |     ++, --     | Postfix                     | Right to left |
|    02      |      +, -      | Unary plus minus            | Right to left |
|    02      |      !, ~      | Logical Not and bitwise not | Right to left |
|    02      |      (type)    | Unary plus minus            | Right to left |
|    02      |        *       | Unary plus minus            | Right to left |
|    02      |        &       | Unary plus minus            | Right to left |
|    02      |    sizeof      | Unary plus minus            | Right to left |
|    02      |   _Alignof     | Unary plus minus            | Right to left |

| Precedence |     Operator    |                Description             | Associativity |
| :--------- | :------------   | :------------------------------------- | :------------
|    03      |     *, /, %     | Multiplication, division, remainder    | Left to Right |

| Precedence |   Operator    |        Description          | Associativity |
| :--------- | :------------ | :---------------------------| :------------
|    04      |     +, -      | Addition and Subtraction    | Left to Right |

| Precedence |     Operator    |              Description            | Associativity |
| :--------- | :------------   | :---------------------------------- | :------------
|    05      |     <<, >>      | Bitwise left shift and right shift  | Left to Right |

| Precedence |     Operator    |               Description             | Associativity |
| :--------- | :------------   | :-----------------------------------  | :------------
|    06      |     <, <=       | less than and less than equals        | Left to Right |
|    06      |     >, >=       | greater than and greater than equals  | Left to Right |

| Precedence |     Operator   |       Description        | Associativity |
| :--------- | :------------  | :----------------------- | :------------
|    07      |     ==, !=     | Equals and not equals    | Left to Right |

| Precedence | Operator   | Description  | Associativity |
| :--------- | :--------  | :----------- | :------------
|    08      |      &     | Bitwise And  | Left to Right |

| Precedence | Operator   | Description  | Associativity |
| :--------- | :--------  | :----------- | :------------
|    09      |      ^     | Bitwise XOR  | Left to Right |

| Precedence | Operator   | Description  | Associativity |
| :--------- | :--------  | :----------- | :------------
|    10      |      |     | Bitwise OR   | Left to Right |

| Precedence | Operator   | Description  | Associativity |
| :--------- | :--------  | :----------- | :------------
|    11      |     &&     | Logical And  | Left to Right |

| Precedence | Operator   | Description  | Associativity |
| :--------- | :--------  | :----------- | :------------
|    12      |     ||     | Logical OR   | Left to Right |

| Precedence | Operator   | Description  | Associativity |
| :--------- | :--------  | :----------- | :------------
|    13      |     ?:     | Ternary     | Right to Left |

| Precedence | Operator   |                       Description                  | Associativity |
| :--------- | :--------  | :------------------------------------------------  | :------------
|    14      |      =     | Assignment                                         | Right to Left |
|    14      |  +=, -=    | Assignment by sum and difference                   | Right to Left |
|    14      | *=, /=, %= | Assignment by product quotient remainder           | Right to Left |
|    14      |  <<=, >>=  | Assignment by bitwise left shigt and right shift   | Right to Left |
|    14      | &=, ^=, |= | Assignment by bitwise AND XOR OR                   | Right to Left |

| Precedence | Operator   | Description  | Associativity |
| :--------- | :--------  | :----------- | :------------
|    15      |  ,         | Comma        | Left to Right |
