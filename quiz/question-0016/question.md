Floating point computation contains lots of challenging works. For example, how to correctly handle infinity and not-a-number.

What is the following output, and why?

```java
final double zero = 0d;
final double infinite = Double.POSITIVE_INFINITY;

System.out.println((zero / zero) == (infinite / infinite));
```