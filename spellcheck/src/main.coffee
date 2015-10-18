
###
# Wand
Created by Aaron Delaney for a DCU Assignment

http://github.com/devoxel | http://twitter.com/devoxel

When I get permission to release open-source it,
you'll be able to find it at my github!
###


class Config
  constructor: ->
    @debug = true


class EditorModel
  constructor: (@config) ->
    console.log("+ Iniating Model") if @config.debug


class EditorView
  constructor: (@config) ->
    console.log("+ Initiating EditorView") if @config.debug


class EditorController
  constructor: (@config) ->
    console.log("+ Initiating EditorController") if @config.debug


config            = new Config()
editor_model      = new EditorModel(config)
editor_view       = new EditorView(config)
editor_controller = new EditorController(config)
