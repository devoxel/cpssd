###
Author: Aaron Delaney
Date:   29/10/2015

Find more details in spellcheck/README.md
###

# editor/spellcheck.coffee
# -------------------
# Contains:
# - spell checking functions


min = (to_compare) ->
  smallest = to_compare[0]
  for elm in to_compare
    if elm < smallest
      return smallest
  return smallest


check_spelling = (words, word_list, total_reccomends, already_mispelled) ->
  # -> returns a list of all mispelled words in a string with recomendations
  misspelled = {}
  if word_list.length == 0 # we can assume the word_list hasn't finished dl
    return misspelled
  for word in words
    if already_mispelled[word] != undefined
      misspelled[word] = already_mispelled[word]
    else if word not in misspelled and word.toLowerCase() not in word_list
      misspelled[word] = edit_distance_reccomendations(
                          word, 
                          total_reccomends,
                          word_list
                        )
  return misspelled


edit_distance = (a, b) ->
  last_col = [0..a.length]
  current_col = [0]
  for j in [0..b.length]
    for i in [1..a.length]
      if a[i-1] == b[j-1]
        current_col.push(last_col[i-1])
      else
        x = min([last_col[i-1], last_col[i], current_col[i-1]])
        current_col.push(x + 1)
    last_col = current_col
    current_col = [current_col[0]+1]
  return last_col[a.length]


edit_distance_reccomendations = (word, total_reccomends, word_list) ->
  best_words = []
  while best_words.length < total_reccomends
    i = 0
    best_score = -1
    best_word = false
    while i < word_list.length
      current_word = word_list[i]
      score = edit_distance(word, current_word)
      if best_score == -1 and current_word not in best_words
        best_word = current_word
        best_score = score
      if score <= best_score and current_word not in best_words
        best_word = current_word
        best_score = score
      if score == 1
        break
      i = i + 1
    best_words.push(best_word)
  return best_words
