"""
You're given three inputs, all of which are instances of an AncestralTree class that have an ancestor property pointing to their youngest ancestor. 
The first input is the top ancestor in an ancestral tree (i.e., the only instance that has no ancestor--its ancestor property points to None / null), 
and the other two inputs are descendants in the ancestral tree.

Write a function that returns the youngest common ancestor to the two descendants.

Note that a descendant is considered its own ancestor. 
So in the simple ancestral tree below, the youngest common ancestor to nodes A and B is node A.
"""