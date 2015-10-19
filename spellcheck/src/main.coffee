
###
# Wand
Created by Aaron Delaney for a DCU Assignment

http://github.com/devoxel | http://twitter.com/devoxel

When I get permission to release open-source it,
you'll be able to find it at my github!

# Dependincies

- jQuery, to make dom manipulations work across all browsers

###


class Config
  constructor: ->
    @debug = true


class EditorModel
  constructor: (@config, @view) ->
    console.log("+ Iniating Model") if @config.debug
    @text = "Welcome to wand."


class EditorView
  constructor: (@config) ->
    console.log("+ Initiating EditorView") if @config.debug
    @initiateTextArea(window.innterHeight, window.innerWidth)

  initiateTextArea: (width, height) ->
    console.log()

class EditorController
  constructor: (@config, @model) ->
    console.log("+ Initiating EditorController") if @config.debug


config            = new Config()
editor_view       = new EditorView(config)
editor_model      = new EditorModel(config, editor_view)
editor_controller = new EditorController(config, editor_model)
