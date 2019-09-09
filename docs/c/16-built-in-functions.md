## Built in Functions
C provides us some built in functions to help us, write c programs quickly and easily.

## Where do these functions exists ?
1. These functions exists in library files provided by c.
2. Header files contain information about function prototype.

## String related Functions
String related functions are used to manipulate strings, calculate length and perform different operations on string.

```c
#include<string.h>
int main() {
  char name[50] = "Jayant Malik";

  // length of string.
  // navigates till null character and returns the count.
  printf("Length : %d\n", strlen(name));

  // compare two strings
  // navigates till last index and returns difference of,
  // ascii values of characters present,
  // at index.
  printf("Is Has equals has : %d\n", strcmp("Has", "has"));
  printf("Is Has equals java : %d\n", strcmp("Has", "java"));

  // compare n characters of string.
  printf("Is Jayant compares with Jayant Malik : %d\n", strncmp("Jayant", "Jayant Malik", 6))

  // copy one string to another string.
  // this function overwrites the string.
  strcpy("Snake Lion", name);
  printf("Name after copy : %s\n", name);

  // Concatenation of string
  // this function appends name after string.
  strcat(name, "Snake Lion");
  printf("Name after concatenation : %s\n", name);

  return 0;
}
```

## Numbers Related Functions :
```c
#include<math.h>
int main() {
  int number = 20;

  // math related functions
  printf("Sin %d : %f\n", number, sin(number));
  printf("Cos %d : %f\n", number, cos(number));
  printf("Tan %d : %f\n", number, tan(number));
  printf("Cosec %d : %f\n", number, 1 / sin(number));
  printf("Sec %d : %f\n", number, 1 / cos(number));
  printf("Cot %d : %f\n", number, 1 / tan(number));

  // Modulus of floating point numbers.
  // on linux use : gcc filename -lm
  // to link libm library that contains
  // math decimal point related functions.
  printf("20.5 % 3.6 = %f\n", fmod(20.5, 3.6));

  return 0;
}
```

## Quick prototype of string related functions :
```c
    char *strcpy (char *dest, char *src);
    //Copy src string into dest string.

    char *strncpy(char *string1, char *string2, int n);
    //Copy first n characters of string2 to stringl .

    int strcmp(char *string1, char *string2);
    //Compare string1 and string2 to determine alphabetic order.

    int strncmp(char *string1, char *string2, int n);
    //Compare first n characters of two strings.

    int strlen(char *string);
    //Determine the length of a string.

    char *strcat(char *dest, const char *src);
    //Concatenate string src to the string dest.

    char *strncat(char *dest, const char *src, int n);
    //Concatenate n chracters from string src to the string dest.

    char *strchr(char *string, int c);
    //Find first occurrence of character c in string.

    char *strrchr(char *string, int c);
    //Find last occurrence of character c in string.

    char *strstr(char *string2, char string*1);
    //Find first occurrence of string string1 in string2.

    char *strtok(char *s, const char *delim) ;
    //Parse the string s into tokens using delim as delimiter.

```

## Quick prototype of memory related functions :
```c

    void *calloc(int num elems, int elem_size);
    //Allocate an array and initialise all elements to zero .

    void free(void *mem address);
    //Free a block of memory.

    void *malloc(int num bytes);
    //Allocate a block of memory.

    void *realloc(void *mem address, int newsize);
    //Reallocate (adjust size) a block of memory.

```

## Quick prototype of buffer related functions :
```c

    void* memcpy(void* s, const void* ct, int n);
    //Copies n characters from ct to s and returns s. s may be corrupted if objects overlap.

    int memcmp(const void* cs, const void* ct, int n);
    //Compares at most (the first) n characters of cs and ct, returning negative value if cs<ct, zero if cs==ct, positive value if cs>ct.

    void* memchr(const void* cs, int c, int n);
    //Returns pointer to first occurrence of c in first n characters of cs, or NULL if not found.

    void* memset(void* s, int c, int n);
    //Replaces each of the first n characters of s by c and returns s.

    void* memmove(void* s, const void* ct, int n);
    //Copies n characters from ct to s and returns s. s will not be corrupted if objects overlap.

```

## Quick prototype of character related functions :
```c


    int isalnum(int c);
    //The function returns nonzero if c is alphanumeric

    int isalpha(int c);
    //The function returns nonzero if c is alphabetic only

    int iscntrl(int c);
    //The function returns nonzero if c is a control chracter

    int isdigit(int c);
    //The function returns nonzero if c is a numeric digit

    int isgraph(int c);
    //The function returns nonzero if c is any character for which either isalnum or ispunct returns nonzero.

    int islower(int c);
    //The function returns nonzero if c is a lower case character.

    int isprint(int c);
    //The function returns nonzero if c is space or a character for which isgraph returns nonzero.

    int ispunct(int c);
    //The function returns nonzero if c is punctuation

    int isspace(int c);
    //The function returns nonzero if c is space character

    int isupper(int c);
    //The function returns nonzero if c is upper case character

    int isxdigit(int c);
    //The function returns nonzero if c is hexa digit

    int tolower(int c);
    //The function returns the corresponding lowercase letter if one exists and if isupper(c); otherwise, it returns c.

    int toupper(int c);
    //The function returns the corresponding uppercase letter if one exists and if islower(c); otherwise, it returns c.

```

## Quick prototype of character related functions :
```c

    void perror(const char *s);
    //produces a message on standard error output describing the last error encountered.

    char *strerror(int errnum );
    //returns a string describing the error code passed in the argument errnum.

```
