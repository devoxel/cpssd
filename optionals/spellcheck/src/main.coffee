###
Author: Aaron Delaney

Find more details in spellcheck/README.md
###

# main.coffee
# -------------------
# Handles:
# - instantiating the config, view, model and controller

#= require Config
#= require Loader
#= require EditorView
#= require EditorModel
#= require EditorController


config = new Config()
loader = new Loader(config)

update_loader = (interval) ->
  if loader.loaded
    clearInterval(interval)
    create_editors()
  else
    loader.update()

load_interval = setInterval( (() -> update_loader(load_interval) ),  100 )

create_editors = () ->
  editor_view       = new EditorView(config)
  editor_model      = new EditorModel(config, editor_view)
  editor_controller = new EditorController(config, editor_model)
