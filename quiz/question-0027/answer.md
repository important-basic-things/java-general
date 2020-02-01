Because the method `pow` is a `static` method defined in `Math` class. We can avoid the `Math` prefix by adding the following line to the top of your file:

```java
import static java.Math.pow;
```

This manner can only be used when you are importing an accessable static method.