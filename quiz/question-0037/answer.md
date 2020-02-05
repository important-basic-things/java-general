```java
String.join("|", columns);
```

If the answer uses concate operation directly then it should not be a correct answer. Since each concate will generate a new `String` instance. Thus it is not memory efficient.