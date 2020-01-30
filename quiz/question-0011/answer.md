According to the Java Language Specification, the `main` method must be declared public. (https://docs.oracle.com/javase/specs/jls/se8/html/jls-12.html#jls-12.1.4)

So to fix the source code, we should declare `main` method as `public static void main(String[] args) { }`.

However, several versions of the Java launcher were willing to execute Java programs even when the `main` method was not `public`. A programmer filed a bug report. To see it, visit https://bugs.java.com/bugdatabase/view_bug.do?bug_id=4252539 . That bug was marked as “closed, will not be fixed.” A Sun engineer added an explanation that the Java Virtual Machine Specification does not mandate that `main` is public and that “fixing it will cause potential troubles.” Fortunately, sanity finally prevailed. The Java launcher in Java SE 1.4 and beyond enforces that the `main` method is `public`.

See (Core Java Volumn I, 10th edition. Page 44.)