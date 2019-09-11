## Static Queue
Queue is a collection of data items, and has **Front** and **Rear** ends.

![Queue Image](images/)

Queue follows the condition:
* Data Items can be inserted from **Rear** End.
* Data Items can be deleted from **Front** End.

Now, if Queue is implemented using **array**, then it is known as *Static Queue*

## Where is Queue Formed?
If you decide to simulate the queue, using **array** or some other variable, *without* **dynamic memory allocation**, then it is formed in **STACK**.

![Queue in STACK](images/)

The implementation of **Queue** is similar to **Stack** with just few changes. You will see this difference in a while.

## Algorithm of Queue
In order to implement the **Queue**, using array. We need to follow the below steps:

* Create an Array with **NULL** value initialized
* Now, restrict the item insertion from **Rear** end and
* Item Deletion from **Front** end.

After this quick overview, you can easily implement the **Queue**, and create functions for this restriction task.

## Operations on Queue

There are several operations performed on Queue, some of them are:

* Insertion of an item
* Deletion of an item
* Traversal of Queue
* Searching an item
* Updating an item

Every operation on queue will be implemented with the help of a separate function. There are maximum of 3 arguments required to implement the above cases:

Variables Requirement

1. **queue** is a variable containing location of array with null values
2. **length** is a variable with length of array
3. **item** is the data item to be inserted.

We will see write code for each of these operations.

### Insertion in Queue

To insert an item in a queue, we need to create the function, with few required arguments as:

```c
int insert(int *queue, int length, int item);
```

In the above prototype of the **insert** function, the arguments are:

1. **queue** is a variable containing location of array with null values
2. **length** is a variable with length of array
3. **item** is the data item to be inserted.

Algorithm to **insert** an item in queue will be:

1. Iterate the **queue** from i=0; to i<length; with increment of 1.
2. If queue[i] != NULL then continue
3. Else set queue[i] = item; and return item
4. [ End of for loop in step 2]
5. Return -1 and exit

Implementation of above algorithm in code.
```c
#include <stdio.h>

int insert(int *queue, int length, int item){
  for(int i=0; i<length; ++i){
    if(queue[i] != NULL)
      continue;

    // if ith index of queue is null
    // then insert an item
    queue[i] = item;
    return item;
  }

  // in case queue is full
  return -1;
}
```

### Deletion from Queue

The function prototype for *deletion* will be:

```c
void delete(int *queue, int length);
```

In the above prototype of the **delete** function, the arguments are:

1. **queue** is a variable containing location of array with null values
2. **length** is a variable with length of array

Algorithm to **delete** an item from queue will be:

1. Iterate the **queue** from i=0; to i<length; with increment of 1.
2. If queue[i] != NULL then set queue[i] = NULL and break the loop
3. [ End of for loop in step 2]
4. Exit

Implementation of above algorithm in code.
```c
void delete(int *queue, int length){
  for(int i=0; i<length; ++i){
    if(queue[i] != NULL){
      queue[i] = NULL;
      break;
    }
  }
}
```


### Traversal in a Queue
Traversal is a process, of iteration in queue from first element to last element.

The function prototype for *traversal* will be:

```c
void traversal(int *queue, int length);
```

In the above prototype of the **traversal** function, the arguments are:

1. **queue** is a variable containing location of array with null values
2. **length** is a variable with length of array

Algorithm to **traverse** an item from queue will be:

1. Iterate the **queue** from i=0; to i<length; with increment of 1.
2. If queue[i] == NULL then continue
3. Else print 'index of item and item in queue'
4. [ End of for loop in step 2]
5. Exit

Implementation of above algorithm in code.
```c
void traversal(int *queue, int length){
  for(int i=0; i<length; ++i){
    if(queue[i] == NULL)
      continue;

    // if ith index of queue is not null
    printf("Index: %d holds Item: %d\n", i, queue[i]);
  }
}
```

### Searching in a Queue

The function prototype for *searching* will be:

```c
int search(int *queue, int length, int item);
```

In the above prototype of the **traversal** function, the arguments are:

1. **queue** is a variable containing location of array with null values
2. **length** is a variable with length of array
3. **item** is an integer value to be searched.

Algorithm to **search** an item from queue will be:

1. Iterate the **queue** from i=0; to i<length; with increment of 1.
2. If queue[i] == item then return i;
3. [ End of for loop in step 2]
4. Return -1 and Exit

Implementation of above algorithm in code.
```c
int search(int *queue, int length, int item){
  for(int i=0; i<length; ++i){
    if(queue[i] == item)
      return i;
  }

  // if item is not found
  return -1;
}
```


### Updating in Queue

To update an item in a queue, we need to create the function, with few required arguments as:

```c
int update(int *queue, int length, int oldValue, int newValue);
```

In the above prototype of the **insert** function, the arguments are:

1. **queue** is a variable containing location of array with null values
2. **length** is a variable with length of array
3. **oldValue** is the data item to be updated.
4. **newValue** is the data item to update oldValue.

Algorithm to **update** an item in queue will be:

1. Iterate the **queue** from i=0; to i<length; with increment of 1.
2. If queue[i] == NULL then continue
3. Else if queue[i] = oldValue then set queue[i]  = newValue and return newValue
4. [ End of for loop in step 2]
5. Return -1 and exit

Implementation of above algorithm in code.
```c
#include <stdio.h>

int update(int *queue, int length, int oldValue, int newValue){
  for(int i=0; i<length; ++i){
    if(queue[i] == NULL)
      continue;

    if(queue[i] == oldValue){
      queue[i] = newValue;
      return newValue;  
    }
  }

  // in case item is not found
  return -1;
}
```

## Complete Algorithm of Queue:
```c
#include <stdio.h>


// ==========================
//    Insert Function
// ==========================

int insert(int *queue, int length, int item){
  for(int i=0; i<length; ++i){
    if(queue[i] != NULL)
      continue;

    // if ith index of queue is null
    // then insert an item
    queue[i] = item;
    return item;
  }

  // in case queue is full
  return -1;
}


// ==========================
//    Delete Function
// ==========================

void delete(int *queue, int length){
  for(int i=0; i<length; ++i){
    if(queue[i] != NULL){
      queue[i] = NULL;
      break;
    }
  }
}


// ==========================
//    Seperator Function
// ==========================

void seperator(char *message){
  printf("====================================\n");
  printf("====================================\n");
  printf("\t %s\n", message);
  printf("====================================\n");
  printf("====================================\n");
}


// ==========================
//    Traversal Function
// ==========================

void traversal(int *queue, int length){
  for(int i=0; i<length; ++i){
    if(queue[i] == NULL)
      continue;

    // if ith index of queue is not null
    printf("Index: %d holds Item: %d\n", i, queue[i]);
  }

  // just some message to seperate output
  seperator("Traversal Successful");
}


// ==========================
//    Search Function
// ==========================

int search(int *queue, int length, int item){
  for(int i=0; i<length; ++i){
    if(queue[i] == item)
      return i;
  }

  // if item is not found
  return -1;
}


// ==========================
//    Update Function
// ==========================

int update(int *queue, int length, int oldValue, int newValue){
  for(int i=0; i<length; ++i){
    if(queue[i] == NULL)
      continue;

    if(queue[i] == oldValue){
      queue[i] = newValue;
      return newValue;
    }
  }

  // in case item is not found
  return -1;
}


// ==========================
//    Main Function
// ==========================
int main(int argc, char const *argv[]) {
  // create a queue
  int queue[100] = {NULL};
  int length = sizeof(queue) / sizeof(queue[0]);

  // insert item in queue
  insert(&queue, length, 10);
  insert(&queue, length, 20);
  insert(&queue, length, 30);
  insert(&queue, length, 40);
  insert(&queue, length, 50);

  // traverse the queue
  traversal(&queue, length);

  // delete an item
  delete(&queue, length);
  delete(&queue, length);

  // traverse the queue
  traversal(&queue, length);

  // search an item
  int position = search(&queue, length, 40);
  printf("40 is present at location: %d\n", position);

  // update an item
  update(&queue, length, 30, 500);
  update(&queue, length, 40, 600);

  // traverse the queue
  traversal(&queue, length);

  return 0;
}
```

## Queue V/s Stack
