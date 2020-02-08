In a development environment, we usually run our Java program via IDE. But in a production environment, we should run Java program via command line.

Now I have compiled a single file program *Hello.java* into *Hello.class*. I would like to run the program using the following command:

```bash
$ java ./Hello.class
```

But it doesn't work. It shows the follwing executing result:

```bash
Error: Could not find or load main class ..Hello.class
```

Why? What is the correct command to run the program?