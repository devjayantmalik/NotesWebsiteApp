## Basic Input and output Functions (stdio.h) :
| Function | Description
| -------- | -----------
| fopen(name, “r”) | opens file name for read, returns FILE *f; “w” allows write
| fclose(f) | closes file f
| getchar() | read 1 char from stdin or pushback; is EOF (int -1) if none
| ungetch(c) | pushback char c into stdin for re-reading; don’t change c
| putchar(c) | write 1 char, c, to stdout
| fgetc(f) | same as getchar(), but reads from file f
| ungetc(c,f) | same as ungetchar() but onto file f
| fputc(c,f) | same as putchar(c), but onto file f
| fgets(s,n, f) | read string of n-1 chars to a s from f or til eof or \n
| fputs(s,f) |writes string s to f: e.g. fputs(“Hello world\n”, stdout);
| scanf(p,...) | reads ... args using format p (below); put &w/non-pointers
| printf(p, ...) | write ... args using format p (below); pass args as is
| fprintf(f,p,...) | same, but print to file f
| fscanf(f,p,...) | same, but read from file f
| sscanf(s,p,...) | same, but read from string s
| sprintf(s,p,...) | same, as printf, but to string s
| feof(f) | return true iff at end of file f

## Memory management Functions (stdlib.h):
| Function | Description |
| -------- | ----------- |
| malloc(n) | alloc n bytes of memory; for type T: p = (T*)malloc(sizeof(t));
| free(p) | free memory pointed at p; must have been alloc’d; don’t re-free
| calloc(n,s) | alloc n-array size s & clear; typ: a = (T*)calloc(n, sizeof(T));

## Math Related Functions (math.h) (link -lm) :

All functions take and return double unless otherwise noted:

| Function | Description
| -------- | -----------
| sin(a), cos(a), tan(a) | sine, cosine, tangent of double (in radians)
| asine(y),acos(x),atan(r) | principle inverse of above
| atan2(y,x) | principal inverse of tan(y/x) in same quadrant as (x,y)
| sqrt(x) | root of x
| log(x) | natural logarithm of x; others: log2(x) and log10(x)
| exp(p) | e to the power of p; others: exp2(x) and exp10(x)
| pow(x,y) | x to the power of y; like (expy*log(x))
| ceil(x) | smallest integer (returned as double) no less than x
| floor(x) | largest integer (returned as double) no greater than y
| abs(x) | absolute value of x
| random() | returns a random long
| srandom(seed) | seeds the random generator with a new random seed

## String related functions (string.h) :
| Function | Description |
| -------- | ----------- |
| strlen(s) | return length of string; number of characters before ASCII 0
| strcpy(d,s) | copy string s to d and return d; N.B. parameter order like =
| strncpy(d,s,n) | copy at most n characters of s to d and terminate; returns d
| stpcpy(d,s) | like strcpy, but returns pointer to ASCII 0 terminator in d
| strcmp(s,t) | compare strings s and t and return first difference; 0=> equal
| strncmp(s,t,n) | stop after at most n characters; needn’t be null terminated
| memcpy(d,s,n) | copy exactly n bytes from s to d; may fail if s overlaps d
| memmove(d,s,n) | (slow) copy n bytes from s to d; won’t fail if s overlaps d
