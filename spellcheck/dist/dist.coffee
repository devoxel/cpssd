###
# Wand
Created by Aaron Delaney for a DCU Assignment

Refer to README for more information
###

# editor/view.coffee
# - conatins the EditorView class


class EditorView
  # -> This charge is of the view of the model
  constructor: (@config) ->
    console.log("+ Initiating EditorView") if @config.debug
    @word_count = @config.welcome_text_length
    @misspelled = []

    @initContainer()
    @initTextArea()
    @initInfoArea()
    @updateWindowSize()

  initContainer: ->
    # The container handles the width and height updates
    # TextArea and Info are therefore sized relativly in the CSS
    $('body').append '<div id="container"></div>'
    @container = $('#container')

  initTextArea: ->
    @updateSize()
    @container.append """
    <div id="text" contenteditable="true" spellcheck="false">#{@config.welcome_text}</div>
    """
    @textarea = $("#text")

  initInfoArea: ->
    @container.append """
    <div id="info">
    #{@infoHTML(@word_count, @misspelled)}
    </div>
    """
    @info = $("#info")

  drawInfo: ->
    @info.html(@infoHTML(@word_count, @misspelled))

  updateSize: ->
    w = $(window).innerWidth()  /20 * 19
    h = $(window).innerHeight() /20 * 19
    @container_height = "#{h}px"
    @container_width  = "#{w}px"

  updateWindowSize: ->
    @updateSize()
    @container.css("height", @container_height)
    @container.css("width", @container_width)

  format_misspelling: (l) ->
    # A function that returns a html representation of a mispelling object
    s = ""
    for word, other_spellings of l
      s += "<ul class='misspelling'><b>#{word}</b>"
      for spelling in other_spellings
        s += "<li>#{spelling}</li>"
      s += "</ul>"
    return s

  infoHTML: (word_count, mispellings) ->
    return """
    <h1>Wand /*</h1>
    word count: #{@word_count}
    <br>
    misspelled words:
    <br>
    #{@format_misspelling(@misspelled)}
    """

###
# Wand
Created by Aaron Delaney for a DCU Assignment

Refer to README for more information
###

# editor/model.coffee
# - conatins the EditorModel class and the spell checking functions
#   note: these functions may be moved eventually


countStr = (string, regex) ->
  # -> counts the amount of occurences of any given regex in a string
  # and returns the length
  count = 0
  for word in string.match(regex)
    if word.length > 0
      count += 1
  return count


get_reccomendations_edit_distance = (word, length, word_list) ->
  # the meat of the program, todo
  return ["asdf", 'casdf']


check_spelling = (string, word_regex, word_list, recommend_length) ->
  # -> returns a list of all mispelled words in a string with recomendations
  misspelled = {}
  if word_list.length == 0 # we can assume the word_list hasn't finished dl
    return misspelled
  for word in string.match(word_regex)
    if word not in misspelled and word.length > 1 and
                              word.toLowerCase() not in word_list
      misspelled[word] = get_reccomendations_edit_distance(word, recommend_length, word_list)
  return misspelled


class EditorModel
  # -> in charge of the data the editor looks after and how it is managed.
  constructor: (@config, @view) ->
    console.log("+ Iniating Model") if @config.debug
    @text = @config.welcome_text
    @container = @view.container # controller needs to set events up on this
    @word_regex = /[^\W]([A-Za-z]+)[^\W]/ig

  updateText: ->
    # Update the text
    if @text != @view.textarea.html()
      @text = @view.textarea.html()
      @updateInfo()
      @view.drawInfo()

  updateInfo: ->
    # We don't need the values here, so don't bother storing them as attributes
    # note: if the controller started needing these we would need to store them
    # as attributes of the model (and then set the view ones are references)
    @view.word_count = countStr(@text, @word_regex)
    @view.misspelled = check_spelling(@text, @word_regex, @config.word_list,
                                 @config.recommend_length)

  updateWindowSize: ->
    @view.updateWindowSize()

###
# Wand
Created by Aaron Delaney for a DCU Assignment

Refer to README for more information
###

# editor/controller.coffee
# - conatins the EditorController class

class EditorController
  # -> in charge of managing how the model is updated.

  # Browsers means we don't need to do that much work, but it's useful to have
  # this class in case I ever wanted to expand what users can do.
  # (eg. settings)
  constructor: (@config, @model) ->
    console.log("+ Initiating EditorController") if @config.debug
    @skipped_renders = 0
    @setupEvents()

  setupEvents: ->
    # setupEvents assigns javascript event bindings on each object
    $(window).resize( =>
      @model.updateWindowSize()
    )
    @model.container.on('keypress focus', (event) =>
      if event.type == "keypress"
        if @skipped_renders < 4 or event.which == 32 or event.which == 13 or event.which == 8 or event.which == 17
          @model.updateText()
          @skipped_renders = 0
        else
          @skipped_renders += 1
      else
        @model.updateText()
    )

###
# Wand
Created by Aaron Delaney for a DCU Assignment

Refer to README for more information
###

# config.coffee
# - contains the Config class

class Config
  # The config class handles all of the constant-like data, as well as defaults
  # for things like edit message, and debug mode.
  constructor: ->
    @debug = true
    @welcome_text = "Welcome to wand"
    @welcome_text_length = 3
    @word_list = []
    @wordlist_url = "https://raw.githubusercontent.com/sindresorhus/word-list/master/words.txt"
    @wordlist_request = $.ajax(@wordlist_url,
      cache: true,
      crossDomain: true,
      dataType: "text"
    ).done (data, textStatus, jqXHR) =>
      console.log("Finished downloading wordlist") if @debug
      @word_list = data.split(/\n/)
    @length_of_reccomends = 4 # the amount of reccomended words provided

###
Wand
-> Created by Aaron Delaney for a DCU Assignment
Refer to:
-> the README, included in the root of this project
###






config            = new Config()
editor_view       = new EditorView(config)
editor_model      = new EditorModel(config, editor_view)
editor_controller = new EditorController(config, editor_model)

