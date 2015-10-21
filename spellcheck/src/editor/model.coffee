###
# Wand
Created by Aaron Delaney for a DCU Assignment

Refer to README for more information
###

# editor/model.coffee
# - conatins the EditorModel class


countStr = (string, regex) ->
  count = 0
  for word in string.split(regex)
    if word.length > 0
      count += 1
  return count


format_misspelling = (l) ->
  s = ""
  for word, other_spellings of l
    s += "#{word}<br>"
    for spelling in other_spellings
      s += "? #{spelling}<br>"
  return s


get_reccomendations_edit_distance = (word, length) ->
  return ["asdf", 'casdf']


check_spelling = (string, word_regex, word_list, length_of_reccomends) ->
  misspelled = {}
  if word_list.length == 0 # we can assume the word_list hasn't finished
    return misspelled
  for word in string.split(word_regex)
    if word not in misspelled and word.length > 0 and word.toLowerCase() not in word_list
      misspelled[word] = get_reccomendations_edit_distance(word)
  return misspelled

class EditorModel
  constructor: (@config, @view) ->
    console.log("+ Iniating Model") if @config.debug
    @text = @config.welcome_text

    @initContainer()
    @initTextArea()
    @initInfoArea()
    @updateWindowSize()

  initContainer: ->
    $('body').append '<div id="container"></div>'
    @container = $('#container')

  initTextArea: ->
    @updateSize()
    @container.append """
    <div id="text" contenteditable="true" spellcheck="false">#{@config.welcome_text}</div>
    """
    @textarea = $("#text")

  initInfoArea: ->
    @updateInfo()
    @container.append """
    <div id="info">
    #{@infoHTML(@word_count, @misspelled)}
    </div>
    """
    @info = $("#info")

  updateInfo: ->
    @word_count = countStr(@text, @config.word_regex)
    @misspelled = check_spelling(@text, @config.word_regex, @config.word_list,
                                 @config.length_of_reccomends)

  infoHTML: (word_count, mispellings) ->
    return """
    Wand /*
    <br><br>
    word count: #{@word_count}
    <br>
    misspelled words:
    <br>
    #{format_misspelling(@misspelled)}
    """

  drawInfo: ->
    @info.html(@infoHTML(@word_count, @misspelled))

  updateText: ->
    if @text != @textarea.html()
      @text = @textarea.html()
      @updateInfo()
      @drawInfo()

  updateSize: ->
    w = $(window).innerWidth()  /20 * 19
    h = $(window).innerHeight() /20 * 19
    @container_height = "#{h}px"
    @container_width  = "#{w}px"

  updateWindowSize: ->
    @resize = true
    @updateSize()
    @view.update(@)
