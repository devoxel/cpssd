
# Usage Info

    python pathfinder.py --help

The file should work with all python 2.7.X distributions.

# pathfinder.py
- Written by Aaron Delaney, 2015
- Built with https://www.python.org/
- Developed for CPSSD1 @ DCU


## Command Line Interface

#### Usage: pathfinder.py [OPTIONS]

- ### Options:

  `--help`:

    Print this help file

  `--test`st:

    Initiates test protocol.

    This uses the in-build series of tests to ensure the program works as
    intended.

  `--verbose`:

    Enables verbose output

- ### CLI:

  The command line interface is simple but powerful.

  Table Input Format:
      [ [1,1,0,0], [1,1,1,1], [1,1,1,1], [1,1,1,1] ]

  To use it normally just run the script.

  However to use it efficiently you can just make a file with your tables and
  use bash (or your equivalent) to pass the arguments in, like so:
  ```sh
  $ cat example_tables.txt | python pathfinder.py
  ```
