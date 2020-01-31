The output should be `false`. 

This is because either side will produce `NaN` result, and you cannot test `NaN` value using `==` operator. To check whether a particular result equals `Double.NaN`, you should use `Double.isNaN(x)`.