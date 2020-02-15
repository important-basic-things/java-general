The `break` and `continue` clause give us additional abilibty to control loop. The code below is a typical queue consumer. What is the output to the `logger` if the first 3 calls to `queue.take()` return `Message.PAINT`, `Message.STOP` and `Message.CLEAR`.

```java
public class Consumer {
  private final MessageQueue queue;
  private static final Logger logger = 
    LoggerFactory.getLogger(Consumer.class);

  public Consumer(MessageQueue queue) {
    this.queue = queue;
  }

  public void consume() {
    while (true) {
      try {
        Message message = queue.take();
        if (Message.STOP.equals(message)) {
          logger.info("Consumer receives stop message");
          break;
        }

        MessageBody body = message.getBody();
        logger.info("Consumer receives normal message");
      } catch (InterruptedException error) {
        logger.error("Exception occurred", error);
      }
    }
  }
}
```