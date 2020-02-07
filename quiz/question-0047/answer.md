```java
final String result = fragments.collect(
    StringBuilder::new,
    StringBuilder::append,
    (builder1, builder2) -> builder1.append(builder2.toString())
).toString();
```

Or

```java
final String result = fragments.collect(Collectors.joining());
```