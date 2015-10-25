###
# Wand
- Created by Aaron Delaney for a DCU Assignment
~ For details refer to the README in the root of this project
###

#= require Config
#= require EditorView
#= require EditorModel
#= require EditorController

config            = new Config()
editor_view       = new EditorView(config)
editor_model      = new EditorModel(config, editor_view)
editor_controller = new EditorController(config, editor_model)
