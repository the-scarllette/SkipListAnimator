# Skiplist Animator
Creates a random skiplist and creates an animation of a search through the data structure.
## Usage
Running animation.py will give you a random skiplist and produce a gif of a search through it.<br>
Altering the parameters that are used to generate the skiplist can give you varying skiplists.
## Skiplists
The skiplist data structure is made in skiplist.py.<br>
Skiplists are directed lists that contain multiple 'layers'.<br>
All elements appear on the base layer and it is determined randomly if an element appears on higher layers.

When searching through the skiplist you can search a higher layer with less elements before moving down a layers.<br>
This makes them more efficient to search.
## Animating
The animations are done using [matplotlib](https://matplotlib.org/). <br>
The skiplist is drawn onto a plot and then animated using FuncAnimation.
## Links
- [matplotlib](https://matplotlib.org/)
- Geeks for Geeks page on [skiplists](https://www.geeksforgeeks.org/skip-list/)