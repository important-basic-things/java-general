The `break` and `continue` clause give us additional abilibty to control loop. The code below is a game character class in a game. What is the content of the `characterStatus` variable?

```java
class GameCharacter {
  private String name;
  private final Map<String, Integer> properties = new HashMap<>();

  public GameCharacter(String name) {
    this.name = name;
    properties.put("HP", 100);
    properties.put("MP", 50);
    properties.put("POISONED", null);
  }

  public void makePoisoned() {
    Integer poisoned = properties.get("POISONED");
    if (poisoned == null) {
      properties.put("POISONED", 1);
      return;
    }

    properties.put("POISONED", poisoned + 1);
  }

  public void clearPoisoned() {
    properties.put("POISONED", null);
  }

  @Override
  public String toString() {
    StringBuilder builder = new StringBuilder();
    if (name != null) {
      builder.append("Player: ").append(name).append('\n');
    }

    builder.append("Stats:\n");
    String[] propertyNames = properties.keySet().stream()
      .sorted().toArray(String[]::new);
    for (String propertyName : propertyNames) {
      Integer value = this.properties.get(propertyName);
      if (value == null) {
        continue;
      }
      builder
        .append(" - ").append(propertyName)
        .append(':').append(value)
        .append('\n');
    }

    return builder.toString();
  }
}

// ...

final GameCharacter superman = new GameCharacter("Superman");
superman.makePoisoned();
superman.makePoisoned();
superman.clearPoisoned();
String characterStatus = superman.toString();
System.out.println(characterStatus);
```