What is the output of the following program. And why?

```java
String greeting = "Hello";
String hello = "Hello";
String another = "Hello World".substring(0, 5);

System.out.println(greeting == hello);
System.out.println(hello == another);
```