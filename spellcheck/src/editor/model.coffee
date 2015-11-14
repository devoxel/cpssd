###
Author: Aaron Delaney
Date:   29/10/2015

Find more details in spellcheck/README.md
###

#= require spellcheck

# editor/model.coffee
# -------------------
# Contains:
# - the EditorModel class


countStr = (words) ->
  # -> counts the amount of occurences of any given regex in a string
  # and returns the length
  return words.length

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
