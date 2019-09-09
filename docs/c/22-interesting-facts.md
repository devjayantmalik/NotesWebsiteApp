## We can use <% %> in place of braces.
```c
#include<stdio.h>
int main(int argc, char const *argv[])
<%
	printf("FILE : %s\n",__FILE__);
	printf("TIME : %s\n",__TIME__);
	printf("DATE : %s\n",__TIME__);
	printf("LINE NUMBER : %d\n",__LINE__);
	return 0;
%>
```

## We can take keep stdin buffer open till our custom letter is typed :
```c
#include<stdio.h>
int main()
{
	int age = 0;
	printf("Enter your age :\t");
	scanf("%d[^-]",&age);

	printf("Your age is %d\n",age);

	return 0;
}

```
