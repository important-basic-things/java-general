According to the Java Language Specification, the `main` method must be declared public. (https://docs.oracle.com/javase/specs/jls/se8/html/jls-12.html#jls-12.1.4)

So to fix the source code, we should declare `main` method as `public static void main(String[] args) { }`.

However, several versions of the Java launcher were willing to execute Java programs even when the `main` method was not `public`. The Java launcher in Java SE 1.4 and beyond enforces that the `main` method is `public`.

See (Core Java Volumn I, 10th edition. Page 44.)