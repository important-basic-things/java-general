In real world we would like to make boundary to reduce the complexity of the problem. In Java, we hate long list of statements too. We would like to separate different kinds of code to different building blocks. And the simplest building block is a pair of `{` and `}`.

What is the execution result of the following code?

```java
public static void main(String[] args) {
  int yearOfBirth = 1990;

  {
    String name = "Ann";
    int yearOfBirth = 2002;

    System.out.println("%s was born in %d", name, yearOfBirth);
  }
}
```