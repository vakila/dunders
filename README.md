# Using and abusing Python's double-underscore methods and attributes

## [github.com/vakila/dunders](https://github.com/vakila/dunders)

### Anjana Vakil, [EuroPython 2016](https://ep2016.europython.eu/conference/talks/using-and-abusing-pythons-double-underscore-methods-and-attributes)

[@AnjanaVakil](https://twitter.com/AnjanaVakil)  
[vakila.github.io](https://vakila.github.io)



## What's this all about?

The curious Python methods and attributes surrounded by double underscores (`__`) go by many names, including "special", "magic", and ["dunder"](https://wiki.python.org/moin/DunderAlias). You probably use some of them, like `__init__`, every day. But that’s just the tip of the iceberg!

In this talk, we’ll explore the weird and wonderful world of the double-underscore, and find out how dunders can be useful, silly, dangerous, and just fun! We’ll play pranks on Python’s builtin operators for arithmetic and comparison. We’ll make arbitrary objects behave like dictionaries and containers. We’ll reduce an object’s memory usage, and speed up tests for membership. We’ll even try some naughty function hacks that we should never use in real life!

## What are dunders?

They're "special" methods that Python expects to find on certain objects, and calls to perform some basic functionality of the language, such as when using operators like `+` (calls `__add__`) or built-in functions like `len` (calls `__len__`) . Taking full advantage of the "magic" of Python, and writing Pythonic code, means using these methods properly.

These methods are generally not meant to be exposed to users - they're supposed to be called by the Python interpreter, not us measly humans. But we *can* call them if we want to, if we know what we're doing - abusing the dunder can be fun! >:D

## Where can I read more about dunders?

* The [Python data model](https://docs.python.org/3/reference/datamodel.html) documentation
* Luciano Ramalho's [Fluent Python](http://shop.oreilly.com/product/0636920032519.do) Chapter 1: The Python data model (PDF available as [free book sample](http://cdn.oreillystatic.com/oreilly/booksamplers/9781491946008_sampler.pdf) from O'Reilly website)

## What's in this repo?

Some sample code that illustrates various dunders and how (not) to use them.

DISCLAIMER: Do NOT write real code that looks like the silly, abusive code in this repo! I accept no responsibility for any dunder-related catastrophes directly or indirectly resulting from this talk. Please dunder responsibly. :)

*Contents*:

* `stringyint.py`: A weird type of number that illustrates:
  * some basic dunders we know & love
  * dunders to use operators like `+`
  * more curious dunders like `__hash__` and `__slots__`


* `crazylist.py`: A loco type of list that illustrates dunders to:
  * give an object length and truthiness
  * make an object iterable
  * make an indexable or keyed object
  * test for membership in a container


* `catification.py`: A meowy module that illustrates:
  * hacking a function's code and docstring
  * creating a context manager to be used with `with`


## What should I do next?

Know some dunder tricks you'd like to share? Describe them on the wiki, or add code to `sharing-is-caring/` and submit a PR!

Want to discuss something? Open an issue and start the conversation!

I hope this repo will be a "meeting place" for exchanging special dunder magic, even after the talk :)
