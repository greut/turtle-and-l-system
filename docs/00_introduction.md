---
title: Introduction
---

## Prerequisites

### Installing Python

The very first step of our journey starts by installing the Python programming
language. We will pick the 3 version and not directly embrace the future.

1. Go to `http://python.org/downloads`
2. Click on `Download Python 3.x.x` (at this time it's `3.4.3`)
3. Install it on your machine.

#### Microsoft Windows

You may want to tick the option that adds `python.exe` to the `PATH`.

#### Linux users

You may not need to download it, check if your system has it. It might be an
alias like `python3` instead of `python`. Distributions like _Arch Linux_, _Gentoo
Linux_, and []many more](http://distrowatch.com/search.php?pkg=Python&pkgver=3#pkgsearch)

The following code should work alike for both versions.

#### OSX users

OSX comes with a Python version that might be quite old. Please follow [the
following tutorial to install or update it on
OSX](https://wolfpaulus.com/jounal/mac/installing_python_osx/).

#### What about Python 2.x?

Python 2 sticks out there because the new version changed many low level
mechanisms of the language like how strings are handled. It takes a very long
time for libraries and companies to adapt to new systems. As an example, look
at how long it takes for your school or company to upgrade the computers to the
latest Microsoft Windows version.

Python 2 is great but new project should start with the 3 branch because not
many novelties are expected to land in Python 2. For more information, take a
look at the [PEP 404](http://legacy.python.org/dev/peps/pep-0404/).

### First step with Python

On Microsoft Windows, it comes with IDLE which will be a good companion to help
us discover Python. The first step will be to run IDLE (or `python` or
`ipython`) and learn more a about it.

```
Python 3.4.3 (default, Mar 25 3015, 17:13:50)
[GCC 4.9.2 20150304 (prerelease)] on linux
Type "help", "copyright", "credits" or "license" for information
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> quit
Use quit() or Ctrl-D (i.e. EOF) to exit
```

Okay, we know how to seek for help and quit the interactive shell. A gentle
introduction to Python is to get acquainted with its philosophy. Yes, languages
create wars because they have different philosophies that shape our brains
differently.

```
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

_this_ is great! Never ever forget that languages, natural or programming ones,
are meant to be read and **not** written.

### The obligatory `Hello world!`

That's way too simple to even be important but it would bring bad luck to not
do it, I guess.

```python
>>> print("Hello world!")
Hello world!
```
