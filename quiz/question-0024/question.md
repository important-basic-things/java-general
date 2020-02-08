In Java, one of the most vulnerable operation is doing integer arithmetics. So we should always very careful while doing that kind of operation. 

What is the execution result of the following statement? And why?

```java
final int ZERO = 0;
final double floatingPointResult = 0.0 / ZERO;
final int integerResult = 3 / ZERO;

System.out.println(floatingPointResult);
System.out.println(integerResult);
```