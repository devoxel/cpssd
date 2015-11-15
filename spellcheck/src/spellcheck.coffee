###
Author: Aaron Delaney
Date:   29/10/2015

Find more details in spellcheck/README.md
###

#= require BKTree

# editor/spellcheck.coffee
# -------------------
# Contains:
# - spell checking functions


min = (to_compare) ->
  smallest = to_compare[0]
  for elm in to_compare
    if elm < smallest
      return smallest
  return smallest


class Spellchecker
  constructor: (config) ->
    @bktree = undefined
    @wordset = undefined
    @generated = false
    @pre_misspelled = {}
    @misspelled_keys = new Set()
    @config = config

  edit_distance: (a, b) ->
    last_col = [0..a.length]
    current_col = [0]
    for j in [0..b.length]
      for i in [1..a.length]
        if a[i-1] == b[j-1]
          current_col.push(last_col[i-1])
        else
          x = min([last_col[i-1], last_col[i], current_col[i-1]])
          current_col.push(x + 1)
      last_col = current_col
      current_col = [current_col[0]+1]
    return last_col[a.length]

  generate: (word_list) ->
    @wordset = new Set(word_list)
    @bktree = new BKTree(word_list, @edit_distance)
    @generated = true

  update: (words) ->
    if @config.word_list.length > 0 and not @generated
      console.log ("Generating")
      @generate(@config.word_list)
    if not @generated
      return {}

    misspelled = {}
    for word in words
      lower_word = word.toLowerCase()
      if @misspelled_keys.has(lower_word)
        misspelled[lower_word] = @pre_misspelled[lower_word]
      else if not @wordset.has(lower_word)
        console.log "testing #{lower_word}" if @config.debug
        # lets ignore words which are a large distance away
        mispellings = @bktree.query(word, 3, @config.recommend_length)
        misspelled[lower_word] = mispellings
        @pre_misspelled[lower_word] = mispellings
        @misspelled_keys = @misspelled_keys.add(lower_word)

    return misspelled
