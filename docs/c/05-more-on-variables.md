## How much memory does variable reserve ?
It depends on datatype of variable and Architecture of OS, few datatypes as per 16 bit OS are :

1. int    - 2 bytes
2. char   - 1 byte
3. float  - 4 bytes
4. double - 8 bytes

## Using sizeof() function :
1. C provides us some predefined datatypes, such as int, float, char, double etc.

- These datatypes reserves different memory in RAM as per datatype.

- sizeof() function return int as return value in bytes.

- sizeof() function takes datatype as its argument.

- sizeof() function also takes variable_name as its argument.

- sizeof() function also takes direct value as its argument.

## Example of sizeof() function :

```c
	int main(){
		int age = 18;

		// size using variable.
		printf("int has size of %d bytes", sizeof(age));
		// size using datatype
		printf("float has size of %d bytes", sizeof(float));
		// size using value
		printf("char has size of %d bytes", sizeof('A'));

		return 0;
	}
```

## Datatypes in C:

1. unsigned int

- signed int

- unsigned char

- signed char

- unsigned float

- signed float

- and few more..........

## Note :
1. unsigned allows only positive values.

- signed allows positive as well as negative values.

## Memory Allocation for signed datatype :
let's assume the memory in form of blocks that are represented by square brackets [] .

so, memory becomes,

		char = 1 byte = 8 bits  = [1][][][][][][][]

#### In case of signed datatypes :
1. First most bit is reserved for signature info.

- This first most bit is called as sign bit.

- Sign bit holds two values : 0 for positive values.

- and 1 for negative values.

## Points to Remember :
1. OS stores data in RAM in form of bits 0 or 1.

- Bits are states of current experienced by hardware.

- Memory or RAM is divided in bits.

## Calculation of Size and range of values :

#### Representation of memory in case of char:
					[][][][][][][][]

1. Minimum binaries that 8 bits could hold is : 00000000
- Maximum binaries that 8 bits could hold is : 11111111

#### Let's check binary :
	1   | 00000001
	2	| 00000010
	....
	....
	255 | 11111111

>	Here, we notice that when number is converted in binary 255 is the maximum value that results in 11111111 which is equivalent to maximum storage reserved in RAM.

#### How will i convert a number to Binary ?
		255 /2 | 1
		127 /2 | 1
		063 /2 | 1
		031 /2 | 1
		015 /2 | 1
		007 /2 | 1
		003 /2 | 1
		001 /2 | 1

Steps are :

1. Take any number that you want to convert. (255 in our example)

- Divide the number by 2 and note its remainder and quotient as seen above.

- Again divide the quotient by 2 until we get zero as quotient.

- As a remainder we obtain binary of the number.

## Conclusion :
1. we learnt how to convert integer number to binary.

- now you can convert binary to number and find maximum range of variable.

## Cyclic behaviour :
1. Cyclic behaviour is used to determine value of variable that will be provided as result when user enters beyond variable's maximum range.

- Example signed char could hold values from -128 to 127.

- What happens when user enters 128

- Program shows cyclic behaviour.
	//figure of cyclic behaviour
		(0) ---------- (127)
		 '				 '
		 '				 '
		 '				 '
		(-1) --------- (-128)

So, as per the figure the result obtained will be -128

#### The above concept of cyclic behaviour applies to all datatypes in c.
