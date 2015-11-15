###
Author: Aaron Delaney
Date:   29/10/2015

Find more details in spellcheck/README.md
###

# editor/BKTree.coffee
# -------------------
# Contains:
# - the BKTree object


class Node
  constructor: (word) ->
    @children = {}
    @word = word

  get_word: () ->
    return @word

  add_child: (distance, node) ->
    @children[distance] = node

  get_child: (distance) ->
    return @children[distance]

  in: (distance) ->
    return distance.toString() in Object.keys(@children)


class BKTree
  constructor: (words, distance_callback) ->
    root = words[0]
    words = words[1..]
    @tree = new Node(root)
    @distance_callback = distance_callback

    bkadd = (parent, word, callback) ->
      distance = callback(word, parent.get_word())
      if parent.in(distance)
        bkadd(parent.get_child(distance), word, callback)
      else
        parent.add_child(distance, new Node(word))

    for word in words
      bkadd(@tree, word, @distance_callback) if word.length > 0

  query: (word, threshold, length) ->
    # Returns all words that are withen n distance from word
    # Returns a list sorted in ascending order of distance
    recursive_search = (parent) =>
      distance = @distance_callback(word, parent.get_word())
      results = []
      if distance <= threshold
        @search_results.push( [distance, parent.get_word()] )
      for i in [(distance-threshold)..(distance+threshold+1)]
        if parent.in(i)
          @search_results.concat( recursive_search( parent.get_child(i ) ) )

    @search_results = []
    recursive_search(@tree)
    return @search_results.sort( (a,b) -> return a[0] - b[0] )[..length]
           .map( (a) -> a[1])
