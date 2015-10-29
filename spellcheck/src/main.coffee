###
Author: Aaron Delaney
Date:   29/10/2015

Find more details in spellcheck/README.md
###

# main.coffee
# -------------------
# Handles:
# - instantiating the config, view, model and controller

#= require Config
#= require EditorView
#= require EditorModel
#= require EditorController

config            = new Config()
editor_view       = new EditorView(config)
editor_model      = new EditorModel(config, editor_view)
editor_controller = new EditorController(config, editor_model)
