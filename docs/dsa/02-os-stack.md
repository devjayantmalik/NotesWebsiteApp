## Intro to Stack:
Stack is a part of memory, created during the application runtime. It holds all the local variables and instances of functions in it.

Let's say we have a program, consisting of 3 functions as follows:
```c
#include <stdio.h>

// Function pi
float pi(){
  return 22/7;
}

// function calculate
float pi_times(int num){
  return pi() * num;
}

// main function
int main(int argc, char const *argv[]) {
  // calculating the pi squared.
  int squared = pi_times(2);
  printf("PI Squared: %.14f\n", squared);

  return 0;
}
```

#### Note:
  To visualize the above code working please visit [pythontutor.com/c.html](http://pythontutor.com/c.html)  
  Paste the code and press visualize execution button.
  After pressing visualize button you will see Forward button.
  Click forward button and see the stack in action.

Now, the Operating System needs to solve the functions. In order to solve the above program,

The Operating System:

* Allocates *RAM* for program
* Loads the program in *RAM*
* Solves *each* function one by one inside **STACK**
* Free the memory allocated for each function, whenever the function returns some value.
* Finally, free the memory reserved for whole program.

Let's understand different parts of RAM, allocated by OS.
We have already discussed in introduction section, that each program on loading in **RAM**, loads in 4 different sections. They are:

* Text
* Environment Variables
* Heap
* Stack

Now, in this lesson, we will study one of the memory section from above 4 sections, that is **STACK**

## Working of Stack
Stack is a data structure, that holds some data. The data could be of any type, such as int, float, char, pointer, structure, union etc.

The STACK follows some conditions, which differentiates it from other **data structures**, that is:

* Item in *STACK* can be **inserted** and **deleted** from **TOP** of STACK.

The above terminology ***"insertion and deletion from top"*** has given STACK a short form **LIFO** described as, **LAST IN FIRST OUT**

**LIFO** simply means, the data item inserted at last will be evaluated first.

## Example to Demonstrate the example:
Consider, the **STACK** as bunch of boxes, each able to store a number.

* Step 1:

```
Each Box represent a single part of STACK memory

Memory | Index
  []      0
  []      1
  []      2
  []      3
```

* Adding 1, 2, 3 in the STACK

```
Memory | Index
  [1]      0
  [2]      1
  [3]      2
  []       3
```

* Deleting an item from STACK

```
Memory | Index
  [1]      0
  [2]      1
  []       2
  []       3
```

* Adding 5 in the STACK

```
Memory | Index
  [1]      0
  [2]      1
  [5]      2
  []       3
```

Note:
  You will notice that,

  * **3 was deleted** from stack and **5 was inserted** in the same position **where 3 existed** a while ago(before deletion).
  * So, it makes sense that, if we print address of each of these numbers, **then address of 3** should be equal to **address of 5**


## Practical Demonstration of LIFO:

Let's write a program that demonstrates, that:
**a function on returning some value is deleted from stack**
and a new function called after it will occupy its position.

#### Note:
  Please Visit [pythontutor.com/c.html](http://pythontutor.com/c.html) to visualize the **STACK** formed during execution of program.

```c
#include <stdio.h>

int calculate_fib(int num){
  // printing address of num.
  printf("Address: %u || Number: %d\n", &num, num);

  // check for 1 and 0
  if(num <= 1)
    return 1;

  // else calculate the fib
  return calculate_fib(num - 1) + calculate_fib(num-2);
}

int main(int argc, char const *argv[]) {

  // calculating Fibonacci of 3
  int result = calculate_fib(3);

  printf("Fib 4: %d\n", result);
  return 0;
}
```

The output of the above program is:
```sh
Address: 1528622092 || Number: 3
Address: 1528622044 || Number: 2
Address: 1528621996 || Number: 1
Address: 1528621996 || Number: 0
Address: 1528622044 || Number: 1
Fib 3: 3
```

You could have noticed that:

* Line 3 and 4 have same address.
* Line 2 and 5 have same address.

To understand the above issue, draw the STACK with following rule:

* Insert the item from top and delete from top.

You will notice that result of **fib(1)** was deleted and then **fib(0)** was loaded in same memory address, so, the address were same.

---

## Implementation of STACK:
STACK can be implemented using 2 ways, i.e,

* STATIC IMPLEMENTATION - ARRAY IMPLEMENTATION
* DYNAMIC IMPLEMENTATION - LINKED LIST IMPLEMENTATION

DYNAMIC IMPLEMENTATION WILL BE COVERED IN FUTURE.

### STATIC Implementation:
Whenever actions of STACK are simulated using arrays, it is called static implementation.

To implement the stack as array:

* Create an array variable and restrict its insertion and deletion from one end.
* To restrict the insertion and deletion, we need to create 2 functions, **insert()** and **delete()** and allow them to insert and delete item in our array.

### Algorithm for static implementation

Variables Explanation:

```
1. Here, int *stack is a pointer variable which holds the address of stack array initialized with null values.
2. length is the integer variable holds max no of items that can be inserted in stack array.
3. item is the int variable that holds the data item to be inserted.
```

* Insert Function

```
int insert(int *stack, int length, int item){
  1. Process for loop from i=0 to i<length;
  2. If stack[i] != NULL then continue
  3. Else:
      set stack[i] = item;
      return item;
    [End of step 2 loop]
  4. print "stack is full"
  5. return -1;
}
```

* Delete Function

```
void delete(int *stack, int length){
  1. process for loop from i=length-1 to i>0
  2. if stack[i] is not NULL:
        set stack[i] = NULL
        break;
}
```

* Traverse Function

```
void traverse(int *stack, int length){
  1. process for loop from i=0 to i<length
  2. If stack[i] == NULL then continue
  3. Else print i and queue[i]
}
```

* Main Function

```
int main(){
  1. create an stack array with all elements initialized to null
  int stack[100] = {NULL}

  2. Calculate length of stack using formula:
  int length = sizeof(stack) / sizeof(stack[0])

  3. Insert elements in array
    insert(&stack, length, 10);
    insert(&stack, length, 20);
    insert(&stack, length, 30);

  4. Traverse the array
    traverse(&stack, length);

  5. Delete the element from array
    delete(&stack, length);

  6. Traverse the array
    traverse(&stack, length)

  return 0;
}
```

### Algorithm written in C

```c
#include <stdio.h>


// ++++++++++++++++++++++++++
//      Insert Function
// ++++++++++++++++++++++++++

int insert(int *stack, int length, int item){
  for(int i=0; i<length; ++i){
    if(stack[i] != NULL)
      continue;

    // if ith index of stack is not null
    stack[i] = item;
    return item;
  }

  // if stack is full
  return -1;
}


// ++++++++++++++++++++++++++
//      Delete Function
// ++++++++++++++++++++++++++

void delete(int *stack, int length){
  for(int i=length -1; i>0; --i){
    if(stack[i] != NULL){
      stack[i] = NULL;
      break;
    }
  }
}


// ++++++++++++++++++++++++++
//      Traverse Function
// ++++++++++++++++++++++++++

void traverse(int *stack, int length){
  for(int i=0; i<length; ++i){
    if(stack[i] == NULL)
      continue;

    // means ith index of stack contains some item.
    printf("Index: %d holds Item: %d\n", i, stack[i]);
  }

  // just to seperate content
  printf("================================\n");
  printf("================================\n");
  printf("\t Traversal Successful\n");
  printf("================================\n");
  printf("================================\n");
}


// ++++++++++++++++++++++++++
//      Main Function
// ++++++++++++++++++++++++++

int main(int argc, char const *argv[]) {
  // create stack and calculate its length
  int stack[100] = {NULL};
  int length = sizeof(stack)/ sizeof(stack[0]);

  // insert element in stack
  insert(&stack, length, 10);
  insert(&stack, length, 20);
  insert(&stack, length, 30);

  // traverse elements in stack
  traverse(&stack, length);

  // delete elements from stack
  delete(&stack, length);
  delete(&stack, length);

  // traverse elements from stack
  traverse(&stack, length);

  return 0;
}
```
