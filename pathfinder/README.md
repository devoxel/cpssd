
# Usage

I suggest a terminal but regardless, just do this:

    python pathfinder.py

The file should work with all python 2.7.X distributions.

# pathfinder.py
    - Written by Aaron Delaney, 2015
    - Built with https://www.python.org/
    - Developed for CPSSD1 @ DCU
    - References:
      - Loading from a file in unix-likes:
       http://unix.stackexchange.com/questions/149726/how-to-pass-each-line-of-a-text-file-as-an-argument-to-a-command
       @konsolebox


## Command Line Interface

Usage: pathfinder.py [OPTIONS] [TABLE ...]

Options:

  --test:
    Initiates test protocol.

    This uses the in-build series of tests to ensure the program works as
    intended.

  --verbose:
    Enables verbose output

  table:
    For example:
        $ pathfinder.py [[1,0],[0,1],[1,1]]

    For info on table structure, read the documentation provided in the file.
    Multiple tables can be passed in.

If no OPTIONS are included, then pathfinder starts asking the user for input.

## Loading from file

I felt it was out of scope to begin building more functions for pathfinder, like
loading from files and all that, since it's not a CLI tool at it's core.

However, here's some unix glue to run lots of tables from a file:
```sh
while IFS= read -r LINE; do
    python pathfinder.py "$LINE"
done < example_tables
```

I've provided the file in load_from_file.sh. Make sure it has +x permissions
or run it like this:
    $ bash load_from_file

You'll have to change example tables to suit your input, or change the filename

This bash script was sourced from:
http://unix.stackexchange.com/questions/149726/how-to-pass-each-line-of-a-text-file-as-an-argument-to-a-command
