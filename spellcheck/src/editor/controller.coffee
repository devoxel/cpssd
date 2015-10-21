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
    @setupEvents()

  setupEvents: ->
    # setupEvents assigns javascript event bindings on each object
    $(window).resize( =>
      @model.updateWindowSize()
    )
    @model.container.on('keydown keyup focus', (event) =>
      @model.updateText()
    )
