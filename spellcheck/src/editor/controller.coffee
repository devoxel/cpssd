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
