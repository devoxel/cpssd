###
# Wand
Created by Aaron Delaney for a DCU Assignment

Refer to README for more information
###

# editor/model.coffee
# - conatins the EditorModel class and the spell checking functions
#   note: these functions may be moved eventually


countStr = (string, regex) ->
  # countstr(string, regex) ->
  #   counts the amount of occurences of any given regex in a string and returns
  #   the length
  count = 0
  for word in string.split(regex)
    if word.length > 0
      count += 1
  return count


format_misspelling = (l) ->
  # A function that returns a html representation of a mispelling object
  s = ""
  for word, other_spellings of l
    s += "#{word}<br>"
    for spelling in other_spellings
      s += "? #{spelling}<br>"
  return s


get_reccomendations_edit_distance = (word, length, wordlist) ->
  # the meat of the program, todo
  return ["asdf", 'casdf']


check_spelling = (string, word_regex, word_list, recommend_length) ->
  # check_spelling(string, regex, word_list, recommend_length) ->
  #   returns a list of all mispelled words in a string with reccomendations
  misspelled = {}
  if word_list.length == 0 # we can assume the word_list hasn't finished
    return misspelled
  for word in string.split(word_regex)
    if word not in misspelled and word.length > 0 and word.toLowerCase() not in word_list
      misspelled[word] = get_reccomendations_edit_distance(word)
  return misspelled

class EditorModel
  # -> in charge of the data the editor looks after and how it is managed.
  constructor: (@config, @view) ->
    console.log("+ Iniating Model") if @config.debug
    @text = @config.welcome_text
    @container = @view.container # controller needs to set events up on this

  updateText: ->
    # Update the text
    if @text != @view.textarea.html()
      @text = @view.textarea.html()
      @updateInfo()
      @view.drawInfo()

  updateInfo: ->
    # Update the Info panel

    # We don't need the values here, so don't bother storing them as attributes
    # note: if the controller started needing these we would need to store them
    # as attributes of the model (and then set the view ones are references)
    @view.word_count = countStr(@text, @config.word_regex)
    @view.misspelled = check_spelling(@text, @config.word_regex, @config.word_list,
                                 @config.recommend_length)

  updateWindowSize: ->
    @view.updateWindowSize()
