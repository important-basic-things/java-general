A boolean expression is a Java expression that, when evaluated, returns a `boolean` value: `true` or `false`. When we write program, it is important to determine whether a conditional expression will be evaluated or not. Please take a look at the following program:

```java
public static void main(String[] args) {
  if (returnTrue() || returnFalse()) {
    System.out.println("Hello");
  }
}

boolean returnFalse() {
  System.out.println("return false");
  return false;
}

boolean returnTrue() {
  System.out.println("return true");
  return true;
}
```

What is the execution result of the following program?