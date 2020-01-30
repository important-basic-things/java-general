> 1. The JDK version 1.3.0 is one of the release of Java Platform 2 (aka Java 2).

Correct. The term *Java 2* is an outdated term that described Java versions from 1998 until 2006.

In 1998 when the marketing folks at Sun felt that a fractional version number increment did not properly communicate the momentous advances of JDK 1.2. However, because they had that insight only after the release, they decided to keep the version number 1.2 for the development kit. Subsequent releases were numbered 1.3, 1.4, and 5.0 (See Core Java Vol I)

> 2. The internal JDK version of Java SE 8 is 8.0.

Incorrect. The internal JDK version of Java SE 8 is 1.8.0.

From 2006, the version numbering of Java SE was simplified. The next version of the Java Standard Edition was called Java SE 6, followed by Java SE 7 and Java SE 8. However, the “internal” version numbers are 1.6.0, 1.7.0, and 1.8.0. (See Core Java Vol I)

> 3. Java SE 8_u_31 means the 31st update of Java SE 8.

Correct. When Oracle makes a minor version change to fix urgent issues, it refers to the change as an update. For example, Java SE 8u31 is the 31st update of Java SE 8, and it has the internal version number 1.8.0_31.  (See Core Java Vol I)

> 4. The update sequence is strictly 1 by 1. That means the next public released update of Java SE 8_u_31 is Java SE 8_u_32.

Incorrect. An update does not need to be installed over a prior version—it contains the most current version of the whole JDK. Also, not all updates are released to the public. (See Core Java Vol I)

> 5. The Java FX is another implementation of Java SE.

Incorrect. JavaFX is a software platform for creating and delivering desktop applications, as well as rich Internet applications (RIAs) that can run across a wide variety of devices. (See [Wikipedia](https://en.wikipedia.org/wiki/JavaFX)). JavaFX is intended to replace Swing as the standard GUI library for Java SE.

Java FX is not part of Java SE. But it is now part of Oracle JDK (since Oracle Java SE 7 update 6). Since the JDK 11 release in 2018, JavaFX is part of the open-source OpenJDK, under the OpenJFX project.