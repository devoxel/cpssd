# Usage

Only command line use is supported! That means getting to the directory `yp.py`
is contained in your terminal of choice and running it from there.

```
$ python ./yp.py --h

Usage: python yp.py [MODE] [WORD]...
Checks if a word is a palindrome using various methods

Modes:
  --palindrome           check if a word is a palindrome
  --anagram              check if any anagram of a word is a palindrome
  --test                 test both modes with the same set of words
  --h                    print this help file
```

To use a string with spaces, just encapsulate the string in quotes.

# Support

This program should run on any Python 2.7.X platform.

# To Test

To test, simply leave out the `[WORD]` argument and the program will use a series
of test words.

The `--test` mode just calls both the palindrom and anagram modes

```
$ python yp.py --test

No words entered, using test words
> Rercursive Palindrome Checker
  redivider :   True
  noon :        True
  civic :       True
  radar :       True
  modemimodem : False
  MadamImAdam : True
  aaAbbbB :     False
  fabda :       False
  time (s):     0.00505766946493

> Iterative Palindrom Checker
  redivider :   True
  noon :        True
  civic :       True
  radar :       True
  modemimodem : False
  madamimadam : True
  aaabbbb :     False
  fabda :       False
  time (s):     0.00884573743052

> Anagram Palindrome Possibility
  redivider :   True
  noon :        True
  civic :       True
  radar :       True
  modemimodem : True
  madamimadam : True
  aaabbbb :     True
  fabda :       False
  time (s):     0.0107251682215
```


This documentation was also written in Markdown, and you can see it in
its full glory by opening README.html in a modern browser.

This file was mostly written in linux, so the EOL (end of line) format may
display incorrectly inside your editor.
