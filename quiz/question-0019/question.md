The way which turns characters into series of bytes is called encoding. There are different encoding algorithms. For example, UTF-8, UTF-16, UTF-32, GB2312, GBK, Shift-JIS. In Java, The `String` class uses UTF-16 for character encoding. So understanding how UTF-16 works with `String` and `char` is important.

Suppose that you have a unicode character `U+1F602` (the `U+` is the prefix of unicode character code indicator). If there is a `String` object which contains only this unicode character. What is the output of the following program? And why?

```java
System.out.println(theStringObject.length());
```