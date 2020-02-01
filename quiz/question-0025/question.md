When you execute the following program, you are likely to have different results on different platforms. Why? If you want to ensure reproducable result, how to fix it?

```java
public class Program {
  public static void main(String[] args) {
    List<Double> numbers = extractNumbersFromArgs(args);
    System.out.println(numbers.get(0) * numbers.get(1) / numbers.get(2));
  }
}
```