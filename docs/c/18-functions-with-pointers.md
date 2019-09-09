## Functions with pointers :
Functions with pointers are also known as call by reference functions.

## Points :
1. These functions could contain pointers as formal argument.
- These could return a pointer as a value from function.

## Functions Returning pointers as a value :
> Make sure the address value of variable exists after pop of function from stack, else the output is not guaranteed correct because that memory location could be overwritten by some other program or by your own program.

#### Syntax :
```c
return_type * function_name(arguments) {
  // body of function

  return address_variable;
}
```

#### Example :

```c
char *copy(char *destination, char * source){
  int index = 0;
  while(*(source + index) != '\0'){
    *(destination + index) = *(source + index);
    index++;
}

int main(){

  char *name1 = "Jayant Malik";
  printf("Before Copy : %s\n", name1);

  copy(name1, "Sam Novak");
  printf("After Copy : %s\n", name1);
  printf("After Copy, printing using return value from function : %s\n", copy(name1, "Apples are sweet"));

  return 0;
}
```
