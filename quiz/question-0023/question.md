Do you think the following class is syntactically correct? If it is not, why?

```java
class Date {
    private final short year = 1990;
    private final byte month = 1;
    private final byte day = 1;

    public Date(short year, byte month, byte day) {
        // validation omitted.
        this.year = year;
        this.month = month;
        this.day = day;
    }

    public Date() {
    }
}
```