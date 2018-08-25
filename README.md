# Quadtree

Faced with the challenge of limited processing power on the raspberry pi, to solve spatial indexing, I chose a quadtree.

This allows me to section off the screen so I can easily query that section of the screen.
This can be used in things such as hit detection. area of effect skills/spells, etc.

Hit detection before was done in O(n^2), every frame, every entity had to check every other entity that existed if they touched.
Quadtree brought it down to O(n log(n)), having only to look at the entities in a range.

Here is the simulator that adds particles to the screen, builds the quadtree, then can be queryed and used to highlight all of the particles that collide. 
