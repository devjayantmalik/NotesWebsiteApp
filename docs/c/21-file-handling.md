## File handling in C :
File handling is API of C used to interact with OS and buffer to read or write or work with files.

## Files :
-	Collection of related info is called as file. or
-	Collection of number of bytes when written on harddrive is called a file.

## File Operation :
We can execute four operations on any file :

1. Open
2. Read
3. Write
4. Close

## Why File handling ?
1. Hard Disk Contains all your files.

2. Files are managed by OS.

3. But OS cannot change contents of a file itself.

4. Some Program/Software is required to provide data to OS to write it to file.

5. Examples : Notepad for text files, VLC for audio video files...etc...

## What happens during program execution?
1. Program is Executed

- It gets some memory in RAM.

- Program creates BUFFER for file handling.

- Data is loaded in BUFFER

- Data is manipulated in BUFFER.

- OS flushes buffer and writes data to file.

- Program Terminates.

## Why we need buffer ?
Because speed of Hard Disk is slow than RAM.

## What will happen if Program interacts direct with files on HDD ?
1. Program Loads in RAM and executes from RAM.
- RAM has much much faster speed than Hard Disk.
- File is present in Hard Disk.

If program interacts with File present on Hard Disk or secondary storage, then Speed of Program execution will not match with file read or write.
	Hence,

	1. Program will require a large time to complete its execution.
	2. Will result in slow speed

## C File Handling :
	Program  ----> BUFFER ----> File_on_hard_disk

## Functions for file handling :

|Function Name |Description
|--------------|------------
| fputc() 	   | Writes single character in buffer
| fputs()	   | Writes string to buffer
| fopen() 	   | Opens buffer as per mode ({'a'}append, {'r'}read, {'w'}write)
| fclose()	   | Closes and flushes buffer
| fgetc()	   | Reads single character from buffer
| fgets()	   | Reads single string from buffer
| feof()	   | Checks if end of file is reached.
| fprintf()	   | Writes formatted data to buffer.
| fseek()	   | Changes current reading/writing position in file buffer.
| ftell()      | Returns current reading/writing position in file buffer.
| fwrite()	   | Writes structure data to file with datatype info in encrypted form
| fread()	   | Reads data from file stored in form of structures


## How C handles file details :
- To manage file details, C uses structure to store file info.
- FILE is structure name, declared in stdio.h
- fopen() returns pointer to FILE struct, this pointer is then later used for file manipulation.

```c
// sample code
#include<stdio.h>
int main(int argc, char const *argv[])
{
	FILE *document;

	document = fopen("/home/jayant/testing.txt","r");
	fclose();

	return 0;
}

```
### Note : Complete file content cannot be loaded to buffer at once, because BUFFER size allocated to application is limited.

## fopen
	1. It is a function of C.
	2. Used to create BUFFER in RAM.
	3. Loads content of file to buffer as per requirement.
	4. Returns NULL if unable to open.
Syntax :
```c
	int main(int argc, char const *argv[])
	{
		fopen(pointer_to_file_location, pointer_to_file_mode);
		// Visual picture :
		FILE * fopen(const char *loc, const char *mode);

		file modes :
		1. Read 	---->allows read only operations
		2. Write 	---->allows overwrite operations
		3. Append 	---->allows appending operations (adds text after end of file)

		return 0;
	}

```

## Example of fopen()
```c
#include<stdio.h>

int main(int argc, char const *argv[])
{
	FILE *document;

	document = fopen("/home/jayant/temp/file.c");
	if(document == NULL)
		return 0;
	// some operation on file.

	fclose(document);	//closes file buffer.
	return 0;
}
```

## fclose()
1. Function of C.
2. Closes File stream or buffer.
3. Flushes buffer.
4. Informs OS to release memory allocated for file by program.

Syntax :
```c
#include<stdio.h>
	int main(int argc, char const *argv[])
	{
		// open buffer using fopen()

		fclose(pointer_to_buffer);
		//Visual appearence
		fclose(const FILE *buffer);

		return 0;
	}
```

## Example of fclose() :
```c
#include<stdio.h>

int main(int argc, char const *argv[])
{
	FILE *document;

	document = fopen("/home/jayant/temp/file.c","w");
	if(document == NULL)
		return 0;

	// some action to ececute on file

	fclose(document);

	return 0;
}
```

## fputc()
1. Writes a single character at an instance to BUFFER.
2. Returns ascii value of charcter written.

Synatx :
```c
	int main(int argc, char const *argv[])
	{
		int fputc(letter_to_write, pointer_to_buffer);
		// Visual Appearence
		extern int fputc (int __c, FILE *__stream);

		return 0;
	}

```

## Example of fputc()
```c
#include<stdio.h>

int main(int argc, char const *argv[])
{
	FILE *doc;

	doc = fopen("/home/jayant/temp/file.c","a");
	if(document == NULL)
		return 0;

	char result = fputs('A', doc);
	printf("Returned : %c", result);

	fclose(doc);
	return 0;
}
```

```c
#include<stdio.h>

int main(int argc, char const *argv[])
{
	FILE *doc;

	doc = fopen("/home/jayant/temp/file.c","a");
	if(document == NULL)
		return 0;

	for(char ch = 'A'; ch <= 'Z'; ch++){
		fputc(ch, doc);
	}

	fclose(doc);
	return 0;
}
```

## fputs()
1. writes a string to buffer.
2. returns 1 on success and -1 on failure(when mode of file is read only).

syntax :
```c
	extern int fputs (const char *__restrict __s, FILE *__restrict __stream);
	// Visual look
	fputs(pointer_to_string, pointer_to_buffer);

```
## Example of fputs()
```c
#include<stdio.h>

int main(int argc, char const *argv[])
{
	FILE *doc;

	doc = fopen("/home/jayant/temp/file.c","w");
	if(document == NULL)
		return 0;

	int result = fputs("Jayant", doc);
	printf("%d\n",result);

	fclose(doc);
	return 0;
}
```

## You can use stdout as buffer to print on screen using fgets()

## fgetc()
1. used to read character from buffer.
2. Returns character fetched.

Syntax :
```c
	extern int fgetc (FILE *__stream);
	// Visual Appearence
	fgetc(pointer_to_buffer);
```

## Example of getc()
```c
	#include<stdio.h>
	int main(int argc, char const *argv[])
	{
		FILE *document;

		document = fopen("/home/jayant/temp/file.c","r");
		if(document == NULL)
		return 0;

		char result = fgetc(document);
		printf("Result is %c\n",result);

		fclose();
		return 0;
	}
```

```c
	#include<stdio.h>

	int main(int argc, char const *argv[])
	{
		FILE *document;

		document = fopen("/home/jayant/temp/file.c","r");
		if(document == NULL)
		return 0;

		//reads 10 charcater from file
		for(int i = 0; i < 11; i++){
			printf("%c", fgetc(document));
		}

		return 0;
	}
```

## fgets()
1. Used to read string from BUFFER

- Reads till newline character '\n'

- Returns pointer to destination string variable which is manipulated to store result.(same as first argument of fgets)

- Always terminates itself even if length provided in function is less than no of words read.

- Writes newline character in string if any and always places null character at the end.

Syntax:
```c
	extern char *fgets (char *__restrict __s, int __n, FILE *__restrict __stream);

	//Visual Appearence
	fgets(destination_string_to_write, length_of_string_to_read, pointer_to_buffer);

```

## feof()
- Known as file end of file.

- Checks whether there is end of file reached in buffer.

- Returns 0 on completion is not reached and non zero on completion.

Syntax :
```c
	extern int feof (FILE *__stream) __THROW __wur;
	//Visual Appereance
	feof(pointer_to_buffer);

```

## Examples of feof()
```c
	#include<stdio.h>
	int main(int argc, char const *argv[])
	{
		FILE *document;
		char *message;
		document = fopen("/home/jayant/temp/file.c","r");

		while(feof(document) == 0){ // !feof(document)
			fgets(message, , document);
		}
		fclose(document);
		return 0;
	}
```

## fprintf()
- Function to write formatted output to file
- Provide pointer_to_buffer to printf() function and you get fprintf() function.

Syntax :
```c
extern int fprintf (FILE *__restrict __stream,
		    const char *__restrict __format, ...);
// Visual Appereance :
	fprintf(pointer_to_buffer, same_as_printf_arguments);

```

## Example of fprintf() :
```c
	#include<stdio.h>
	int main(int argc, char const *argv[])
	{
		FILE *doc;
		int name[10] = "Jayant Malik";

		doc = fopen("/home/jayant/temp/file.c","a");
		fprintf(doc, "\nThis is a nice message for %s",name);

		fclose();
		return 0;
	}
```

## Examples :
### Write a program to create simple implementation of cat command in linux.
```c
	#include <stdio.h>

int main(int argc, char const *argv[])
{
	FILE *document;
	char message[100];

	document = fopen(argv[1], "r");

	if(document == NULL){
		printf("Error while processing request.\n");
		return 0;
	}

	while(!feof(document)){
		fgets(message, 95, document);
		printf("%s",message);
	}

	printf("\n");
	return 0;
}
```

### Write a program to create simple implementation of less command in linux.
```c
#include <stdio.h>

int main(int argc, char const *argv[])
{
	FILE *document;
	char message[100];

	document = fopen(argv[1], "r");

	if(document == NULL){
		printf("Error while processing request.\n");
		return 0;
	}

	while(!feof(document)){
		fgets(message, 95, document);
		printf("%s",message);
		getc(stdin);
		printf("\033[1A");
	}

	printf("\n");
	return 0;
}
```

## Handling data with dataype info :
C provides us fwrite() and fread() function to read and write data to file in binary form or encrypted form.

## fwrite()
- writes data stored in structure variable of program to file in encrypted form.

- preserves datatype info of data.

- do not store entire data in form of string.

Syntax :
```c
	extern size_t fwrite (const void *__restrict __ptr, size_t __size,
		      size_t __n, FILE *__restrict __s);
// Visual Appereance
	fwrite(address_of_structure, number_of_bytes, units_of_structures, pointer_to_file);
```

1. number_of_bytes can also be called as size_of_structure

2. units_of_structure is used in case, when we have array of type structure demonstrated in example.

## Examples of fwrite() :
```c
#include<stdio.h>

	struct Employee{
		char name[20];
		int age;
		double salary;
	};			
	typedef struct Employee Employee;

	void getClientData(Employee *client){
		printf("Enter employee name :\t");
		scanf("%s",&client->name);

		printf("Enter employee age :\t");
		scanf("%d",&client->age);

		printf("Enter employee salary :\t");
		scanf("%lf",&client->salary);
	}

	int main(int argc, char const *argv[])
	{
		FILE *document;

		document = fopen("/home/jayant/temp/client_info.data","a");
		if(document == NULL)
		return 0;

		Employee client;
		getClientData(&client);

		fwrite( (char *)&client, sizeof(Employee), 1, document);
		// Note here 1 us passed as third argument because
		//we have single unit of structure not array
		// if we had an array then we would have passed number of elements
		// as argument to fwrite()

		fclose(document);

		return 0;
	}
```

#### Data written in above case is not readable by any text editor.

```c
	// program to accept data of n employees.
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
	FILE *document;
	Employee client[NUMBER_OF_CLIENTS] = {"", 0, 0};
	int index = 0;

	document = fopen("/home/jayant/temp/client_info.txt","a");
	if(document == NULL)
		return 0;

	while(1){
		printf("Enter y to add record and q to quit..\t");
		char ch = getchar();

		if(ch == 'q')
			break;

		getClientData(&client[index]);
		index++;
	}

	fwrite((char *)&client, sizeof(Employee), NUMBER_OF_CLIENTS, document);
	// here NUMBER_OF_CLIENTS are passed as input to function
	// because client structure contains NUMBER_OF_CLIENTS units.

	printf("Record added successfully...");

	fclose(document);
	return 0;
}
```

##fread()

1. Used to read data from file.
2. Reads encrypted data with data type information.

Syntax :
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
	FILE *document;
	Employee client[NUMBER_OF_CLIENTS] = {"", 0, 0};
	int index = 0;

	document = fopen("/home/jayant/temp/client_info.txt","r");
	if(document == NULL)
		return 0;

	while(1){
		printf("Enter y to add record and q to quit..\t");
		char ch = getchar();

		if(ch == 'q')
			break;

		getClientData(&client[index]);
		index++;
	}

	fread((char *)&client, sizeof(Employee), NUMBER_OF_CLIENTS, document);

	for(int i = 0; i < NUMBER_OF_CLIENTS; i++){
		printf("Name : %s\nAge : %d\nSalary : %d\n",client[i].name, client[i].age, client[i].salary);
		printf("============================\n");
	}

	fclose(document);
	return 0;
}

```

## ftell()
1. Returns current read write position in file buffer.
2. After creation of buffer position is 0.
3. File always ends with a character EOF or End Of File.

Syntax :
```c
extern long int ftell (FILE *__stream) __wur;
// Visual Appearence :
ftell(pointer_to_file);
```

## Examples of ftell()
```c

#include<stdio.h>

int main(int argc, char const *argv[])
{
	FILE *document;
	document = fopen("/home/jayant/temp/file.c", "r");

	if(document == NULL)
		return 0;

	int position = ftell(document);
	printf("Position at start is %d\n", position);

	fgetc(document); // reads first character at 0 and changes position to 1.

	position = ftell(document);
	printf("Position after fgetc %d\n", position);

	fclose(document);
	return 0;
}
```

## fseek()
1. Used to change current read write position in file buffer.

2. Supports three mode : beginning position, current position, end position.

3. beginning --> 0, current --> 1, end --> 2

Syntax:
```c
extern int fseek (FILE *__stream, long int __off, int __whence);
// Visual Apperence :
fseek(pointer_to_file, number_of_bytes, position_to_start_from);
```

## Examples of fseek() :
```c

#include<stdio.h>

int main(int argc, char const *argv[])
{
	FILE *document;
	document = fopen("/home/jayant/temp/file.c", "r");

	if(document == NULL)
		return 0;

	int position = ftell(document);
	printf("Position at start is %d\n", position);

	fseek(document, 10, 0); // from beginning

	position = ftell(document);
	printf("Position after fgetc %d\n", position);

	fclose(document);
	return 0;
}
```
```c

#include<stdio.h>

int main(int argc, char const *argv[])
{
	FILE *document;
	document = fopen("/home/jayant/temp/file.c", "r");

	if(document == NULL)
		return 0;

	int position = ftell(document);
	printf("Position at start is %d\n", position);

	fseek(document, -3, 1); // from ending

	position = ftell(document);
	printf("Position after fgetc %d\n", position);

	fclose(document);
	return 0;
}

```

## Write a program in C to count number of letters in a file.
```c
#include<stdio.h>

int main(int argc, char const *argv[])
{
	FILE *src;
	src = fopen("/home/jayant/temp/file.c", "r");

	if(src == NULL)
		return 0;

	fseek(src, 0, 2);
	int letters_count = ftell(src);

	printf("Total letters in file are : %d\n",letters_count);
	fclose(src);
	return 0;
}

```
