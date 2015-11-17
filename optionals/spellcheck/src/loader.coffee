###
Author: Aaron Delaney

Find more details in spellcheck/README.md
###

# loader.coffee
# -------------------
# Contains:
# - Loader class

#= require ./spellchk/edit_distance.coffee
#= require BKTree

class Loader
  constructor: (config) ->
    @config = config
    console.log("loader: initiating loader") if @config.debug
    @loaded = false
    @make_wordlist_request(@config.wordlist_url)

    # kinda hacky way to do a loading icon
    $("body").append('<div id="loader">Loading, please wait..</div>')

  make_wordlist_request: (url) ->
    console.log("loader: loading #{url}")
    @wordlist_request = $.ajax(
      url,
      cache: true,
      crossDomain: true,
      dataType: "text"
    ).done (data, textStatus, jqXHR) =>
      console.log("loader: finished download wordlist") if @config.debug
      @config.word_list = data.split(/\n/)

  generate_bktree: () ->
    @config.wordset = new Set(@config.word_list)
    @config.bktree = new BKTree(@config.word_list, edit_distance)

  update: () ->
    if @config.word_list.length > 0
      @generate_bktree()
      console.log ("loader: finished loading")
      @loaded = true
      $("#loader").css( {"display": "none"} )
