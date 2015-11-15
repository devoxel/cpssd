###
Author: Aaron Delaney

Find more details in spellcheck/README.md
###

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
    @generated = false
    @pre_misspelled = {}
    @misspelled_keys = new Set()
    @config = config

  update: (words) ->
    misspelled = {}
    for word in words
      lower_word = word.toLowerCase()
      if @misspelled_keys.has(lower_word)
        misspelled[lower_word] = @pre_misspelled[lower_word]
      else if not @config.wordset.has(lower_word)
        console.log "spellchecker: testing #{lower_word}" if @config.debug
        # lets ignore words which are a large distance away
        mispellings = @config.bktree.query(word, @config.max_tolerence, @config.recommend_length)
        misspelled[lower_word] = mispellings
        @pre_misspelled[lower_word] = mispellings
        @misspelled_keys = @misspelled_keys.add(lower_word)

    return misspelled
