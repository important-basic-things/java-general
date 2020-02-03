Note that `int` and `long` can be converted to `float`, and `long` can be converted to `double`. But that does not mean it is safe to do that conversion. The conversion mentioned above may lose precision.

So, it is not safe to do `int`/`long` to `float` conversion or `long` to `double` conversion without knowing its possible range.