When using the combined assignment operator, if the operator yields a value of which the type is different with the left side, then it will try to fit to the original type. For example.

```java
int x = 2;
x += 3.5;
```

Is as if 

```java
x = (int)(x + 3.5)
```

The floating point cast will not be rounded, so the result is `5`.