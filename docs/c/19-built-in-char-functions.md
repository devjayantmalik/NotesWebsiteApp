## Working On Built In Functions :
we will discuss built in functions in c and how to create them yourself.

## Character Handling <ctype.h>

## Steps :
1. Create a program to list ascii values of all characters and not them down in table.

2. Now use concept of ascii values to distinguish between different characters

### Program to print ascii values of characters :
```c
	int main(){

		for(int i = 0; i <= 255; i++){
			printf("%d | %c, ", i, i);
		}

		return 0;
	}
```
### Observation table :

| Character Type | Ascii Value
------------|-------------
| a - z			| 97 - 122
| A - z 		| 65 - 90
| 0 - 9     | 48 - 57
| space 		| 32
| control 	| 0 - 31
| punctuation	| 33 - 47, 58 - 64, 91 - 96, 123 -126


### Program to check whether a character is lower case
```c

int islower(const unsigned int character){
	if(character >= 92 && character <= 122)
		return 1;
	else
		return 0;
}

int main(int argc, char const *argv[])
{
	int result = islower('a');

	printf("Character a is lower or upper : %d\n",result);

	return 0;
}

```
### Program to check whether a character is alphabet.
```c
int isalpha(const unsigned int character){

	if(character >= 92 && character <= 122)
		return 1;

	else if(character >= 65 && character <= 90)
		return 1;

	else
		return 0;
}


int main(int argc, char const *argv[])
{
	int result = isalpha('a');

	printf("Character a is alphabet or not : %d\n",result);

	return 0;
}
```

### Program to check whether a character is upper case
```c

int isupper(const unsigned int character){
	return (character >= 65 && character <= 90) ? 1 : 0;
}


int main(int argc, char const *argv[])
{
	int result = isupper('A');

	printf("Character a is uppercase or not: %d\n",result);

	return 0;
}

```
### Program to check whether a character is punctuation character.
```c

int ispunct(const unsigned int character){
	if(
		(character >= 33 && character <= 47) 	||
		(character >= 58 && character <= 64) 	||
		(character >= 91 && character <= 96) 	||
		(character >= 123 && character <= 126)
	  )
		{
			return 1;
	  	}

	return 0;
}


int main(int argc, char const *argv[])
{
	int result = ispunct('!');

	printf("Character a is punctuation or not: %d\n",result);

	return 0;
}
```

### Program to check whether a character is control character.
```c

int iscntrl(const unsigned int character){
	return (character >= 0 && character <= 31) ? 1 : 0;
}


int main(int argc, char const *argv[])
{
	int result = iscntrl('\0');

	printf("Character \\0 is control character or not: %d\n",result);

	return 0;
}
```

### Program to convert lower case character to upper case.
```c

char toupper(const unsigned int character){
	 if(character >= 97 && character <= 122)
	 	return character - 32;

	 else if(character >=65 && character <= 90)
	 	return character;

	 else
	 	return '\0';
}


int main(int argc, char const *argv[])
{
	char result = toupper('a');

	printf("Character a in upper case is : %c\n",result);

	return 0;
}
```

### Program to convert character to lower case
```c
char tolower(const unsigned int character){
	if(character >= 97 && character <= 122)
	 	return character;

	 else if(character >=65 && character <= 90)
	 	return character + 32;

	 else
	 	return '\0';
}

int main(int argc, char const *argv[])
{
	char result = tolower('A');

	printf("A in lower case is %c\n",result);
	return 0;
}
```
## Now we created saveral functions and learnt how they are made ? Now, Let's compare our functions with built in functions.

# Some reasons behind all these functions :
1. All functions take int as their formal argument because every character is a binary number that can be converted to any format as per requirement.

2. All functions except toupper and tolower returns 0 for false and 1 for true as result.

3. We used unsigned int in formal type of each function to prevent cyclic behaviour to some extent.

# Creating header file for our code :
```c
#define __THROW '\0';
#define __INVALID 0;

char cdecl toupper(const unsigned int __letter) __THROW;

char cdecl tolower(const unsigned int __letter) __THROW;

int cdecl isalpha(const unsigned int __letter) __INVALID;

int cdecl iscntrl(const unsigned int __letter) __INVALID;

int cdecl islower(const unsigned int __letter) __INVALID;

int cdecl isupper(const unsigned int __letter) __INVALID;

int cdecl ispunct(const unsigned int __letter) __INVALID;

```

# Generating .dll and header files
1. To generate dll files we need to create .obj files from our code.

2. Code should be written without main function to generate .obj file

3. You can use some IDE to generate .dll project for you(optional)

### Program file with all code without main becomes :
```c

char tolower(const unsigned int character){
	if(character >= 97 && character <= 122)
	 	return character;

	 else if(character >=65 && character <= 90)
	 	return character + 32;

	 else
	 	return '\0';
}


char toupper(const unsigned int character){
	 if(character >= 97 && character <= 122)
	 	return character - 32;

	 else if(character >=65 && character <= 90)
	 	return character;

	 else
	 	return '\0';
}

int iscntrl(const unsigned int character){
	return (character >= 0 && character <= 31) ? 1 : 0;
}


int ispunct(const unsigned int character){
	if(
		(character >= 33 && character <= 47) 	||
		(character >= 58 && character <= 64) 	||
		(character >= 91 && character <= 96) 	||
		(character >= 123 && character <= 126)
	  )
		{
			return 1;
	  	}

	return 0;
}


int isupper(const unsigned int character){
	return (character >= 65 && character <= 90) ? 1 : 0;
}

int isalpha(const unsigned int character){

	if(character >= 92 && character <= 122)
		return 1;

	else if(character >= 65 && character <= 90)
		return 1;

	else
		return 0;
}

int islower(const unsigned int character){
	if(character >= 92 && character <= 122)
		return 1;
	else
		return 0;
}

```

### Now Command for gcc to generate .obj file

##### Checking for errors
```sh
	gcc -o output_file input_file
```
you got an error right,

this is because you cannot submit built in functions with same name as yours.

to solve this issue just change name of your function

	tolower() ---> tolowercase()
	and
	toupper() ---> touppercase()

##### Generating object file
```sh
	gcc -c input_file
```

##### generating dll
```sh
	gcc -shared -o output.dll input_file.o
```

##### Now you can copy header file created with .h file to /usr/include/file_name.h


## Testing everything :
	1. create a file.c

```c
	int main(){

		int result = isupper('a');

		printf("Character in upper case is %d\n",result);

		return 0;
	}
```
	2. Compile and generate executable

```sh
	gcc -o test input_file.c -L file_name.dll
```
	3. Run program

```sh
	./test
```
