
###

# Wand
Created by Aaron Delaney for a DCU Assignment

http://github.com/devoxel | http://twitter.com/devoxel

When I get permission to release open-source it,
you'll be able to find it at my github!

# Dependincies

- jQuery, to make DOM manipulations work across all browsers

# Wordlist
- https://github.com/sindresorhus/word-list

# Limitations of wand

Wand was not designed with real world text editing in mind. It's slower than
most modern text editors and doesn't actually keep track of things like cursor
position or what's currently being rendered.

###

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


class Config
  constructor: ->
    @debug = true
    @welcome_text = "Welcome to wand"
    @word_regex = /[\ ,\.\!\;\?]|<br>/
    @word_list = []
    @wordlist_url = "https://raw.githubusercontent.com/sindresorhus/word-list/master/words.txt"
    @wordlist_request = $.ajax(@wordlist_url,
      cache: true,
      crossDomain: true,
      dataType: "text"
    ).done (data, textStatus, jqXHR) =>
      console.log("Finished downloading wordlist") if @debug
      @word_list = data.split(/\n/)
    @length_of_reccomends = 4


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
