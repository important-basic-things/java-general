The methods in the `Math` class will use the fastest routines in the computer’s floating point unit. And this may produce different results against different platforms. To have a uniform result, you should use the `StrictMath` library. Besides you may want to check `strictfp` for additional information.