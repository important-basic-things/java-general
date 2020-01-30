In Java, you need to make the file name for the source code the same as the name of the public class, with the extension .java appended. Thus, you must store this code in a file called *FirstGreeting.java*. (Again, case is important—don’t use *firstgreeting.java*.)

If you incorrectly named the file, you will receive an error message like this:

```bash
firstgreeting.java:1: error: class FirstGreeting is public, should be declared in a file named FirstGreeting.java
public class FirstGreeting {
       ^
1 error
```