##	Pointers in C :
Pointers are special kind of variables which stores memory address of another variables.

## Syntax of Pointers :
```c
	datatype *variable_name;	or
	datatype *variable_name = value;
```

## Uses of Pointers :
- Manipulate data present at some specific memory address.
- Increases scope of variables.
- Provides multiple names to single variable.
- Provides a way to create arrays in C.
- Dennis Ritche created arrays with help of pointers.
- Pointers are used to manipulate constant variable value.


## Memory allocation in case of pointers :
Memory is allocated by Compiler.
| Compiler | Memory|
|----------|--------
| 16 - BIT | 2 BYTES |
| 32 - BIT | 4 BYTES |
| 64 - BIT | 8 BYTES |

Example :
```c
int main()
{
	char   * ptr1;
	int    * ptr2;
	float  * ptr3;
	double * ptr4;

	printf("char : %lu, int : %lu, float : %lu, double : %lu\n",
				sizeof(ptr1), sizeof(ptr2), sizeof(ptr3), sizeof(ptr4)
			);

	return 0;
}
```

## Examples of pointers :
```c
	int main(){
		int number = 10;
		int *ptr; // declaration

		ptr = &number; // initialization

		// getting address of variable
		printf("address of number %u\n",&number);

		// accessing value of pointer.
		printf("Value in pointer %u\n",ptr);

		return 0;
	}
```

## De-referencing Pointers :

- Dereferencing is process of getting value stored at some memory location with help of pointers. or

- Dereferencing is process of getting value of a variable by using memory address stored in pointer.

## Uses of Dereferencing :
- Dereferencing is Used to read or write data of memory location stored inside pointer.

- Example : int *number = 10; // changes value of number to 10.

## Examples of Dereferencing :
```c
	int main(){
		int marks = 10;
		int *ptr = &marks;

		printf("Marks are %d\n", *ptr); // *ptr is dereferencing pointer to marks.

		return 0;
	}
```
