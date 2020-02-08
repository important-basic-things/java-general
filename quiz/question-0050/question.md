Suppose that we would like to output as the following format:

```
Hello Ann. Next year, you will be 6 years old.
```

The code is as follows:

```java
final String name = "Ann";
final int age = 6;
String text = String.format(
  "Hello (1). Next year, you will be (2) years old.", name, age);
  
System.out.println(text);
```

Please specify the format string at location (1) and (2).