###
# Wand
Created by Aaron Delaney for a DCU Assignment

Refer to README for more information
###

# editor/view.coffee
# - conatins the EditorView class

class EditorView
  constructor: (@config) ->
    console.log("+ Initiating EditorView") if @config.debug

  update: (model) ->
    if model.resize == true
      console.log("+ Resizing canvas") if @config.debug
      model.container.css("height", model.container_height)
      model.container.css("width", model.container_width)
      model.resize = false
