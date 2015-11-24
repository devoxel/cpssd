"""
--> See README.md for info

Author: Aaron Delaney
Email:  aaron.delaney29@mail.dcu.ie
Date:   20/11/2015
"""

def safe_get(l, index, default=None):
    """Get value from sequence l at index, if it doesn't exist return default"""
    if len(l) >= index+1 :
        if len(l[index]) > 0:
            return l[index]
    return default
