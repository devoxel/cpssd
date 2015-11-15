###
Author: Aaron Delaney

Find more details in spellcheck/README.md
###

# editor/edit_distance.coffee
# -------------------
# Contains:
# - Edit distance algorithm


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
