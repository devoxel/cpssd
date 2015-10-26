###
# Wand
- Created by Aaron Delaney for a DCU Assignment
~ For details refer to the README in the root of this project
###

# editor/model.coffee
# - conatins the EditorModel class and the spell checking functions
#   note: these functions may be moved eventually
min = (to_compare) ->
  smallest = to_compare[0]
  for elm in to_compare
    if elm < smallest
      return smallest
  return smallest


countStr = (words) ->
  # -> counts the amount of occurences of any given regex in a string
  # and returns the length
  return words.length


edit_distance = (a, b) ->
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


edit_distance_reccomendations = (word, total_reccomends, word_list) ->
  best_words = []
  while best_words.length < total_reccomends
    i = 0
    best_score = -1
    best_word = false
    while i < word_list.length
      current_word = word_list[i]
      score = edit_distance(word, current_word)
      if best_score == -1 and current_word not in best_words
        best_word = current_word
        best_score = score
      if score < best_score and current_word not in best_words
        best_word = current_word
        best_score = score
      i = i + 1
    best_words.push(best_word)

  return best_words


check_spelling = (words, word_list, total_reccomends, already_mispelled) ->
  # -> returns a list of all mispelled words in a string with recomendations
  misspelled = {}
  if word_list.length == 0 # we can assume the word_list hasn't finished dl
    return misspelled
  for word in words
    if already_mispelled[word] != undefined
      misspelled[word] = already_mispelled[word]
    else if word not in misspelled and word.toLowerCase() not in word_list
      misspelled[word] = edit_distance_reccomendations( word, total_reccomends, word_list)
  return misspelled


class EditorModel
  # -> in charge of the data the editor looks after and how it is managed.
  constructor: (@config, @view) ->
    console.log("+ Initiating Model") if @config.debug
    @text = @config.welcome_text
    @container = @view.container # controller needs to set events up on this
    @word_regex = /[a-zA-Z]+'?[a-zA-Z]+/ig

  updateText: ->
    # Update the text
    if @view.textarea.val().match(@word_regex) == null
      @text = []
      @updateInfo()
      @view.drawInfo()
    else if @text != @view.textarea.val().match(@word_regex) #only update when changed
      @text = @view.textarea.val().match(@word_regex)
      @updateInfo()
      @view.drawInfo()

  updateInfo: ->
    if @text.length < 1
      @view.word_count = 0
      @view.misspelled = {}
    else
      @view.word_count = countStr(@text)
      @view.misspelled = check_spelling(@text, @config.word_list,
                                   @config.recommend_length, @view.misspelled)

  updateWindowSize: ->
    @view.updateWindowSize()
