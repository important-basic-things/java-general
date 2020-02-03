Because the integer conversion follows the following rules:

When 2 integers are combined with a binary operator. Both operands will be converted to a common type before the operation is executed.

* If either of the operands is of type `long`, the other one will be converted to a `long`.
* Otherwise, both operands will be converted to an `int`.

So, the `short` number will be combined to `int` so the result will be an `int`. An `int` cannot be implicitly cast to `short`.