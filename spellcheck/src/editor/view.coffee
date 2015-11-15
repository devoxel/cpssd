###
Author: Aaron Delaney

Find more details in spellcheck/README.md
###

# editor/view.coffee
# -------------------
# Contains:
# - the EditorView class


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
    <textarea id="text" spellcheck="false">#{@config.welcome_text}</textarea>
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
