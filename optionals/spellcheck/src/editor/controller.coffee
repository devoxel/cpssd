###
Author: Aaron Delaney

Find more details in spellcheck/README.md
###

# editor/controller.coffee
# -------------------
# Contains:
# - the EditorController class

class EditorController
  # -> in charge of managing how the model is updated.

  # Browsers means we don't need to do that much work, but it's useful to have
  # this class in case I ever wanted to expand what users can do.
  # (eg. settings)
  constructor: (@config, @model) ->
    console.log("EditorController: Initiating") if @config.debug
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
