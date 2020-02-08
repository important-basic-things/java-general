In real world we would like to make boundary to reduce the complexity of the problem. In Java, we hate long list of statements too. We would like to separate different kinds of code to different building blocks. And the simplest building block is a pair of `{` and `}`.

What is the execution result of the following code:

```java
public static void main(String[] args) {
  int year = 1990;

  {
    int anotherYear = 1999;
  }

  System.out.println("%d and %d", year, anotherYear);
}
```