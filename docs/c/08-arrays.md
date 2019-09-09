## Arrays :
Arrays are used to store same kind of data in matrix form.

## Syntax of array :
```c
	datatype variable_name[No_of_Matrix][No_of_Rows][No_of_columns];
		or
	datatype variable_name[No_of_Matrix][No_of_Rows][No_of_columns] = {value1, value2, value3};
```

#### Example :
```c
int main() {
	// 1-D Array
	int marks[100] = {1, 2, 3, 4, 5};

	int length = sizeof(marks) / sizeof(marks[0]);

	// printing elements of array.
	for(int i=0; i<length; i++){
		printf("%d\t",marks[i]);
	}

	return 0;
}
```

## Few important points about arrays :
1. Indexing of array starts with zero.

- Pointer arithmetic is base for indexing of array (discussed in later section).

- Arrays follow same naming schemes as variables name.

## Types of arrays :
1. One Dimensional Array

2. Two Dimensional Array

3. Three Dimensional Array

## One Dimensional Arrays :
One dimensional arrays are used to store multiple columns of data in a single row.
* The address of elements inside array is in sequential form.
* By default they have few things fixed :
* No_of_Matrix = 1, No_of_Rows = 1
* 1-D Array : int age[10];

#### Syntax of 1-D array:
You could ignore No_of_Matrix and No_of_Rows part, because they are default.

```c
int main() {

	datatype variable_name[No_of_columns];

	or

	datatype variable_name[No_of_columns] = {values};

	return 0;
}
```


#### Example of 1-D array :
```c
	int main(int argc, char const *argv[])
	{
		char name[10] = {'J','a','y','a','n','t','\0'};

		printf("first letter : %c\n",name[0]);
		printf("second letter : %c\n",name[1]);
		printf("third letter : %c\n",name[1]);
		printf("fourth letter : %c\n",name[1]);

		// printing via loop
		for(int i=0; i< 10; i++){
			printf("%d | %d\n", i, name[i]);
		}

		return 0;
	}
```

#### Memory Representation in case of 1-D :
```sh
	name
	{
		[][][][][][][][]		[][][][][][][][]	........
		   1 byte				   1 byte
	}
```

1. Here name is main container representing array.

2. There are sub containers inside name array, 1 byte each representing char datatype.

## Two Dimensional Arrays :
Two dimensional arrays are used to store multiple rows and columns of data in a single matrix.
* The address of elements inside array is in sequential form.
* By default they have few things fixed :
* No_of_Matrix = 1,
* 2-D Array : int ages[10][10];

#### Syntax of 2-D array:

```c
	datatype variable_name[No_of_Rows][No_of_columns];
	or
	datatype variable_name[No_of_Rows][No_of_columns] = {values};
```


#### Example of 2-D array :
```c
	int main(int argc, char const *argv[])
	{
		char matrix1[2][2] = {{1, 2},{4, 5}};

		// printing via loop
		for(int i=0; i< 2; i++){
			for (int j = 0; j < 2; j++) {
				printf("%d | %d = | %d |\n", i, j, matrix1[i][j]);
			}
		}

		return 0;
	}
```

#### Memory Representation in case of 2-D :
![matrix](/images/matrix.png)

## Multi Dimensional Arrays :
Multi dimensional arrays are used to store multiple matrix of data in a sequential order.
* Also known as 3 Dimensional Arrays
* The address of matrices is in sequential form.
* 3-D Array : int ages[2][10][10];

#### Syntax of 3-D array:

```c
	datatype variable_name[No_of_Matrix][No_of_Rows][No_of_columns];
	or
	datatype variable_name[No_of_Matrix][No_of_Rows][No_of_columns] = {values};
```

#### Example of 3-D array:
```c
int main() {
	int data[2][3][3] = {
		{
			{1,2,3},
			{4,5,6},
			{7,8,9}
		},
		{
			{10,11,12},
			{13,14,15},
			{16,17,18}
		}
	};

	printf("Matrix |   Row  | Column =  Value\n");

	//access data using loop.
	for(int matrix=0; matrix < 2; ++matrix){
		for(int row=0; row < 3; ++row){
			for(int col=0; col < 3; ++col){
				printf("%6d | %6d | %6d = %6d\n",
							matrix, row, col,
							data[matrix][row][col]);
			}
		}
	}
	return 0;
}

```

#### Memory Representation in case of 3-D:
![3d-array](/images/3d-array.png)
