It is a compile time error since the value of `ticks` is too large for an `int`. So we should at least declare `ticks` as `long`. And we should change the input parameter type of `getYear` from `int` to `long`.

```java
long ticks = 233544534532342L;
int year = getYear(ticks);
```