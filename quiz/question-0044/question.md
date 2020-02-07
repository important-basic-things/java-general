What is the output of the following program and why?

```java
String greeting = "Hello";
int length = greeting.length();
int cpCount = greeting.codePointCount(0, greeting.length());

System.out.println("%d:%d", length, cpCount);
```