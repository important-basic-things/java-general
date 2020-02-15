In `switch` statement, execution starts at the `case` label that matches the value on which the selection is performed and continues until the next `break` or the end of the switch. If none of the `case` labels match, then the `default` clause is executed, if it is present.

The `break` statements are necessary because without them, statements in switch blocks fall through: All statements after the matching case label are executed in sequence, regardless of the expression of subsequent `case` labels, until a `break` statement is encountered. Using a `break` is recommended so that modifying the code is easier and less error prone.

```
Not supported
Great
```