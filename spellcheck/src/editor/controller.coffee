###
# Wand
Created by Aaron Delaney for a DCU Assignment

Refer to README for more information
###

# editor/controller.coffee
# - conatins the EditorController class

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
