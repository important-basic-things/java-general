Strictfp ensures that you get exactly the same results from your floating point calculations on every platform. If you don't use strictfp, the JVM implementation is free to use extra precision where available (espencially on *Intel* based processors).

Within an FP-strict expression, all intermediate values must be elements of the float value set or the double value set, implying that the results of all FP-strict expressions must be those predicted by IEEE 754 arithmetic on operands represented using single and double formats. Within an expression that is not FP-strict, some leeway is granted for an implementation to use an extended exponent range to represent intermediate results; the net effect, roughly speaking, is that a calculation might produce "the correct answer" in situations where exclusive use of the float value set or double value set might result in overflow or underflow.

So to fix it. We can use:

```java
public class Program {
  public static strictfp void main(String[] args) {
    List<Double> numbers = extractNumbersFromArgs(args);
    System.out.println(numbers.get(0) * numbers.get(1) / numbers.get(2));
  }
}
```