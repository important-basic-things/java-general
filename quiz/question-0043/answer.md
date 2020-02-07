Java strings are implemented as sequences of `char` values. The `char` data type is a *code unit* for representing Unicode *code point* in the UTF-16 encoding.

* A **character** is a minimal unit of text that has semantic value.
* A **character set** is a collection of *characters* that might be used by multiple languages. Example: The Latin character set is used by English and most European languages, though the Greek character set is used only by the Greek language.
* A **coded character set** is a *character set* in which each character corresponds to a unique number.
* A **code point** of a *coded character set* is any allowed value in the *character set* or *code space*.
* A **code space** is a range of integers whose values are *code points*
* A **code unit** is a bit sequence used to encode each **character** of a repertoire within a given encoding form.

(See [Wiki](https://en.wikipedia.org/wiki/Character_encoding#Terminology))