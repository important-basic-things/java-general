The `final` key word can prevent us from accidentally modify the value of the variable. But we should know how `final` really works.

Which of the statement(s) has(have) syntax error? And why?

```java
/* 01 */ final int year = 2020;
/* 02 */ year = 2030;

/* 03 */ final List<String> categories = new ArrayList<>();
/* 04 */ categories.add("Food");
/* 05 */ categories.add("Toy");

/* 06 */ categories = new ArrayList<>();
/* 07 */ categories.add("Furniture");
```