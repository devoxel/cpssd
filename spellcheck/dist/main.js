// Generated by CoffeeScript 1.10.0

/*
 * Wand
Created by Aaron Delaney for a DCU Assignment

http://github.com/devoxel | http://twitter.com/devoxel

When I get permission to release open-source it,
you'll be able to find it at my github!

 * Dependincies

- jQuery, to make DOM manipulations work across all browsers
 */

(function() {
  var Config, EditorController, EditorModel, EditorView, check_spelling, config, countStr, editor_controller, editor_model, editor_view, format_misspelling, get_reccomendations,
    indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };

  countStr = function(string, regex) {
    var count, i, len, ref, word;
    count = 0;
    ref = string.split(regex);
    for (i = 0, len = ref.length; i < len; i++) {
      word = ref[i];
      if (word.length > 0) {
        count += 1;
      }
    }
    return count;
  };

  format_misspelling = function(l) {
    var i, len, other_spellings, s, spelling, word;
    s = "";
    for (word in l) {
      other_spellings = l[word];
      s += word + "<br>";
      for (i = 0, len = other_spellings.length; i < len; i++) {
        spelling = other_spellings[i];
        s += "? " + spelling + "<br>";
      }
    }
    return s;
  };

  get_reccomendations = function(word) {
    return ["asdf", 'casdf'];
  };

  check_spelling = function(string, word_regex, word_list) {
    var i, len, misspelled, ref, ref1, word;
    misspelled = {};
    console.log(word_list);
    ref = string.split(word_regex);
    for (i = 0, len = ref.length; i < len; i++) {
      word = ref[i];
      if (indexOf.call(misspelled, word) < 0 && word.length > 0 && (ref1 = word.toLowerCase(), indexOf.call(word_list, ref1) < 0)) {
        misspelled[word] = get_reccomendations(word);
      }
    }
    return misspelled;
  };

  Config = (function() {
    function Config() {
      this.debug = true;
      this.welcome_text = "Welcome to wand";
      this.word_regex = /[\ ,\.\!\;\?]|<br>/;
      this.word_list = [''];
      this.wordlist_url = "https://raw.githubusercontent.com/shimaore/password/master/lib/wordlist.json";
      this.wordlist_request = $.ajax(this.wordlist_url, {
        cache: true,
        dataType: "json"
      }).done((function(_this) {
        return function(data, textStatus, jqXHR) {
          if (_this.debug) {
            console.log("Finished downloading wordlist");
          }
          return _this.word_list = data['wordlist'];
        };
      })(this));
    }

    return Config;

  })();

  EditorModel = (function() {
    function EditorModel(config1, view) {
      this.config = config1;
      this.view = view;
      if (this.config.debug) {
        console.log("+ Iniating Model");
      }
      this.text = this.config.welcome_text;
      this.initContainer();
      this.initTextArea();
      this.initInfoArea();
      this.updateWindowSize();
    }

    EditorModel.prototype.initContainer = function() {
      $('body').append('<div id="container"></div>');
      return this.container = $('#container');
    };

    EditorModel.prototype.initTextArea = function() {
      this.updateSize();
      this.container.append("<div id=\"text\" contenteditable=\"true\" spellcheck=\"false\">" + this.config.welcome_text + "</div>");
      return this.textarea = $("#text");
    };

    EditorModel.prototype.initInfoArea = function() {
      this.updateInfo();
      this.container.append("<div id=\"info\">\n" + (this.infoHTML(this.word_count, this.misspelled)) + "\n</div>");
      return this.info = $("#info");
    };

    EditorModel.prototype.updateInfo = function() {
      this.word_count = countStr(this.text, this.config.word_regex);
      return this.misspelled = check_spelling(this.text, this.config.word_regex, this.config.word_list);
    };

    EditorModel.prototype.infoHTML = function(word_count, mispellings) {
      return "Wand /*\n<br><br>\nword count: " + this.word_count + "\n<br>\nmisspelled words:\n<br>\n" + (format_misspelling(this.misspelled));
    };

    EditorModel.prototype.drawInfo = function() {
      return this.info.html(this.infoHTML(this.word_count, this.misspelled));
    };

    EditorModel.prototype.updateText = function() {
      if (this.text !== this.textarea.html()) {
        this.text = this.textarea.html();
        this.updateInfo();
        return this.drawInfo();
      }
    };

    EditorModel.prototype.updateSize = function() {
      var h, w;
      w = $(window).innerWidth() / 20 * 19;
      h = $(window).innerHeight() / 20 * 19;
      this.container_height = h + "px";
      return this.container_width = w + "px";
    };

    EditorModel.prototype.updateWindowSize = function() {
      this.resize = true;
      this.updateSize();
      return this.view.update(this);
    };

    return EditorModel;

  })();

  EditorView = (function() {
    function EditorView(config1) {
      this.config = config1;
      if (this.config.debug) {
        console.log("+ Initiating EditorView");
      }
    }

    EditorView.prototype.update = function(model) {
      if (model.resize === true) {
        if (this.config.debug) {
          console.log("+ Resizing canvas");
        }
        model.container.css("height", model.container_height);
        model.container.css("width", model.container_width);
        return model.resize = false;
      }
    };

    return EditorView;

  })();

  EditorController = (function() {
    function EditorController(config1, model1) {
      this.config = config1;
      this.model = model1;
      if (this.config.debug) {
        console.log("+ Initiating EditorController");
      }
      this.setupEvents();
    }

    EditorController.prototype.setupEvents = function() {
      $(window).resize((function(_this) {
        return function() {
          return _this.model.updateWindowSize();
        };
      })(this));
      return this.model.container.on('keydown keyup focus', (function(_this) {
        return function(event) {
          return _this.model.updateText();
        };
      })(this));
    };

    return EditorController;

  })();

  config = new Config();

  editor_view = new EditorView(config);

  editor_model = new EditorModel(config, editor_view);

  editor_controller = new EditorController(config, editor_model);

}).call(this);
