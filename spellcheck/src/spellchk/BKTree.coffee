###
Author: Aaron Delaney

Find more details in spellcheck/README.md
###

# editor/BKTree.coffee
# -------------------
# Contains:
# - the BKTree object and supporting objects


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
    good_result = (elm) ->
      if elm[0] < 1
        return elm[0]
      return undefined

    @search_results = []
    recursive_search = (parent, length) =>
      distance = @distance_callback(word, parent.get_word())
      # javascript is evil so this wont raise an exception, it'll return false
      # if length is out of range
      if @search_results[length] < length - threshold
          return
      if distance <= threshold
        @search_results.push( [distance, parent.get_word()] )
        @search_results.sort( (a, b) -> a[0] - b[0] )
      for i in [(distance-threshold)..(distance+threshold+1)]
        if parent.in(i)
          (recursive_search(parent.get_child(i), length))


    recursive_search(@tree, length)
    return @search_results[..length-1].map((elm) -> return elm[1])
