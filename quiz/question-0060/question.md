A GUI application is generally an huge loop which continuously detects and handles messages. Such as *rendering*, *mouse move*, mouse click. Given the following infrastructure of such application. What is the execution result of the program.

```java
class Application {
  List<String> messages = Arrays.asList("WM_PAINT", "WM_MOUSEMOVE", "WM_QUIT");
  int currentPosition = 0;

  public String getMessage() {
    return messages.get(currentPosition++);
  }
}

// ...

public void String main(String[] args) {
  final Application application = new Application();
  String message;
  while ((!(message = application.getMessage()).equals("WM_QUIT"))) {
      System.out.println(String.format("Handling message: %s", message));
  }
}
```