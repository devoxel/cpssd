###
# Wand
- Created by Aaron Delaney for a DCU Assignment
~ For details refer to the README in the root of this project
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
    @setupEvents()

  setupEvents: ->
    # setupEvents assigns javascript event bindings on each object
    $(window).resize( =>
      @model.updateWindowSize()
    )
    @model.container.on('keypress focus', (event) =>
      if event.type == "keypress"
        if event.which == 32 or event.which == 13 or event.which == 8 or event.which == 17
          @model.updateText()
      else
        @model.updateText()
    )
