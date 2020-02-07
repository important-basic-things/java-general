To get *nth* code point in Java, we can use the following statement:

```java
int index = greeting.offsetByCodePoints(0, n); 
int cp = greeting.codePointAt(index);
```

Why `codePointAt` method returns `int` value?