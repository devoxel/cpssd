
###
# Wand
Created by Aaron Delaney for a DCU Assignment

http://github.com/devoxel | http://twitter.com/devoxel

When I get permission to release open-source it,
you'll be able to find it at my github!

# Dependincies

- jQuery, to make DOM manipulations work across all browsers

###

countStr = (string, regex) ->
  count = 0
  for word in string.split(regex)
    if word.length > 0
      count += 1
  return count

format_misspelling = (l) ->
  console.log(l)
  s = ""
  for word, other_spellings of l
    s += "#{word}<br>"
    for spelling in other_spellings
      s += "? #{spelling}<br>"
  return s

check_spelling = (string, word_regex, word_list) ->
  misspelled = {}
  console.log string.split(word_regex)
  for word in string.split(word_regex)
    if word.length > 0 and word.toLowerCase() not in word_list
      misspelled[word] = ['put reccomendations here']
  return misspelled

class Config
  constructor: ->
    @debug = true
    @welcome_text = "Welcome to wand"
    @word_regex = /[\ ,\.\!\;\?]|<br>/
    @word_list = ["the", "and", "cat", "welcome", "to", "wand"]

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
    Wand /*
    <br><br>
    word count: #{@word_count}
    <br>
    misspelled words:
    <br>
    #{format_misspelling(@misspelled)}
    </div>
    """
    @info = $("#info")

  updateInfo: ->
    @word_count = countStr(@text, @config.word_regex)
    @misspelled = check_spelling(@text, @config.word_regex, @config.word_list)

  drawInfo: ->
    @info.html """
    Wand /*
    <br><br>
    word count: #{@word_count}
    <br>
    misspelled words:
    <br>
    #{format_misspelling(@misspelled)}
    """

  updateText: ->
    @text = @textarea.html()
    @updateInfo()
    @drawInfo()

  updateSize: ->
    h = $(window).innerHeight() /20 * 19
    w = $(window).innerWidth()  /20 * 19
    @container_height = "#{h}px"
    @container_width  = "#{w}px"

  updateWindowSize: ->
    @resize = true
    @updateSize()
    @view.update(@)


class EditorView
  constructor: (@config) ->
    console.log("+ Initiating EditorView") if @config.debug

  update: (model) ->
    if model.resize == true
      console.log("+ Resizing canvas") if @config.debug
      model.container.css("height", model.container_height)
      model.container.css("width", model.container_width)
      model.resize = false


class EditorController
  constructor: (@config, @model) ->
    console.log("+ Initiating EditorController") if @config.debug
    @setupEvents()

  setupEvents: ->
    $(window).resize( => # fat arrow notation means we can pass context too!
      @model.updateWindowSize()
    )
    @model.container.on('keydown keyup focus', (event) =>
      @model.updateText()
    )

config            = new Config()
editor_view       = new EditorView(config)
editor_model      = new EditorModel(config, editor_view)
editor_controller = new EditorController(config, editor_model)
