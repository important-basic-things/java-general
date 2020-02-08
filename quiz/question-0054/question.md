There are cases that you want to format one character multiple times. For example. If I would like to get the following text:

```
The number is 64 in dec and 0x40 in hex.
```

I may write:

```java
String.format("The number is %d in dec and 0x%x in hex", 64, 64);
```

That is not just good enough. How to modify the format string so that I can use:

```java
String.format(formatString, 64);
```

To get the same sentence?