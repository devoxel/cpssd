# Twitter Bot

- Author: Aaron Delaney
- Email:  aaron.delaney29@mail.dcu.ie
- Date:   20/11/2015

## Notably uses

- [Sentiment140](http://help.sentiment140.com/for-students/)

  Large corpus full of random tweet data


- [Strapdown.js](http://strapdownjs.com/)

  Dynamically writes markdown to html

## Usage

#### How to use Sentiment140 corpus:

- Download
[Sentiment140](http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip)

- Unzip in corpora folder

### Usage:

    python loader.py (options) [corpus] [col] [lines]

This should work on any `python 2.7.x` platform.

### Arguments

| name   | description                            | default value             |
|--------|----------------------------------------|---------------------------|
| corpus | The relative path to the corpus        |`corpuses/[...].csv`       |
| col    | The col of `.csv` file to look at      |`5`                        |
| lines  | The amount of lines you with to load   |`750000`                   |

## Options

| name   | description                            | default value             |
|--------|----------------------------------------|---------------------------|
| debug  | print tracebacks if errors occur       | `false`                   |

## Other Notes

Sometimes `()` characters are lying around,I think this is due to Sentiment140.

The same goes for the occasional `&gt;` character, which look like
html artifacts.

## Areas that could be improved

- Use given Sentiment140's emotions to have a MarkovChain that is aware of
emotions.

- Support other file types.

- Examine probabilities of tweets using word analysis, for example perhaps
analyze the distribution of words and adjust MarkovChain generation techniques
with these distributions
