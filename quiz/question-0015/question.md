There are 2 different errors. Compiler error and runtime error. The compiler error occured while the source code contains syntax error, and runtime error often caused by unhandled runtime exceptions. We have to distinguish those 2 types of errors.

Suppose that `getYear` function is properly implemented. What is the problem of the following source code? Is it a compile time error or runtime error?

```java
int ticks = 233544534532342;
int year = getYear(ticks);
```