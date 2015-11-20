# Twitter Bot

## Provided corpus

[Sentiment140](http://help.sentiment140.com/for-students/)

## Usage

How to run:

    python loader.py (options) [corpus] [col] [lines]


## Arguments

| name   | description                            | default value             |
|--------|----------------------------------------|---------------------------|
| corpus | The relative path to the corpus        |`corpuses/sentiment140.csv`|
| col    | The col of CSV file to look at         |`5`                        |
| lines  | The amount of lines you with to load   |`750000`                   |

## Optional Options

| name   | description                            | default value             |
|--------|----------------------------------------|---------------------------|
| debug  | print tracebacks if errors occur       |`corpuses/sentiment140.csv`|

## Other Notes

Sometimes `()` characters are lying around, I think this is due to Sentiment140.

The same goes for the occasional `&gt;` character, which look like
html artifacts.

## Areas that could be improved

- Use given Sentiment140's emotions to have a MarkovChain that is aware of
emotions.

- Support other file types.

- Examine probabilities of tweets using word analysis, for example perhaps
analyze the distribution of words and adjust MarkovChain generation techniques
with these distributions
