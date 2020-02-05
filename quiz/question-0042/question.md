Given the following class

```java
class Profile {
  public String name;
}
```

What is the output of the following program? And why?

```java
Profile profile = new Profile();
if（profile.name.equals(null)) {
  System.out.println("No name");
} else {
  System.out.println("With name");
}
```