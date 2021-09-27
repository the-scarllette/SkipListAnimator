import matplotlib.pyplot as plt
import matplotlib.animation as animation
import skiplist
from random import randint


# Takes two patches and copies the coordinates from one onto the coordinates of the other.
def copy_pos(copy_to, copy_from):
    copy_to.set_x(copy_from.get_x())
    copy_to.set_y(copy_from.get_y())

# Creating Axes
axes_width = 100
plt.style.use('dark_background')
fig = plt.figure()
fig.set_dpi(100)
ax = plt.axes(xlim=(0, axes_width), ylim=(0, axes_width))
plt.axis('off')

# Creating random Skiplist
max_value = 50
s_list = skiplist.random_skiplist(length=27, max_value=max_value, height=4)

# Prints out the skiplist
# s_list.print_nice()

# Choses a random element to find and gets the 'directions' on how to reach it in the skiplist
to_find = randint(int(max_value/2), max_value - 1)
search_path = s_list.search(to_find=to_find, with_path=True)
while search_path == -1:
    to_find = randint(int(max_value/2), max_value - 1)
    search_path = s_list.search(to_find=to_find, with_path=True)
# print("to find: " + str(to_find))
# print(search_path)

# Drawing skiplist on axes
box_separate_x = axes_width/s_list.length
box_width = box_separate_x*0.8
box_separate_y = axes_width/s_list.height
box_height = box_separate_y*0.8
current_node = s_list.start_node
box_x = 0
patches = [[] for i in range(s_list.length)] # An array of all the patches drawn
patches_x = 0
while current_node is not None:
    box_y = 0
    for i in range(len(current_node.pointers)):
        patch = plt.Rectangle((box_x, box_y), box_width, box_height, color='white')
        patches[patches_x].append(patch)
        ax.add_patch(patch)
        plt.text(box_x + (box_width/2), box_y + (box_height/2),
                 current_node.data, color='black', ha="center", va="center")
        box_y += box_separate_y
    box_x += box_separate_x
    current_node = current_node.pointers[0]
    patches_x += 1

# Draeing target box which holds number that is being searched for
target_box_pos = axes_width*0.9
target_box_width = axes_width*0.1
ax.add_patch(plt.Rectangle((target_box_pos, target_box_pos), target_box_width, target_box_width, color='white'))
plt.text(target_box_pos + (target_box_width/2), target_box_pos + (target_box_width/2),
                 str(to_find), color='black', ha="center", va="center")

# Using the directions to the search element found to get the patches that are to be traversed
to_change = []
i = 0
j = s_list.height - 1
to_change.append(patches[i][j])
for elm in search_path:
    if elm == 1:
        i += 1
    elif elm == -1:
        j -= 1

    while len(patches[i]) <= j:
        i += 1
    to_change.append(patches[i][j])


# Creating the highlight to show the path to the search element
highlight = plt.Rectangle((0, box_separate_y*(s_list.height - 1)), box_width, box_height, color='yellow')
tail_1 = plt.Rectangle((0, box_separate_y*(s_list.height - 1)), box_width, box_height, color='yellow', alpha=0)
tail_2 = plt.Rectangle((0, box_separate_y*(s_list.height - 1)), box_width, box_height, color='yellow', alpha=0)
tail_3 = plt.Rectangle((0, box_separate_y*(s_list.height - 1)), box_width, box_height, color='yellow', alpha=0)
tail_4 = plt.Rectangle((0, box_separate_y*(s_list.height - 1)), box_width, box_height, color='yellow', alpha=0)
tails = [tail_1, tail_2, tail_3, tail_4]
tail_len = len(tails)


# Initialising function that is run before the animation begins
def init():
    ax.add_patch(highlight)
    for tail in tails:
        ax.add_patch(tail)
    return highlight, tail_1, tail_2, tail_3,


# animation function, this is called repeatedly with an iterating param i in order to create the animation
def animate(i):
    copy_pos(highlight, to_change[i])
    for l in range(tail_len):
        if i > l:
            copy_pos(tails[l], to_change[i - l - 1])
            tails[l].set_alpha((tail_len-l)/(tail_len+1))
    if i == len(to_change) - 1:
        for tail in tails:
            tail.set_alpha(0)
        highlight.set_color('orange')
        return highlight, tail_1, tail_2, tail_3,
    highlight.set_color('yellow')
    return highlight, tail_1, tail_2, tail_3,


# calling the animator to create the animation and saving it
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(to_change), interval=320, blit=True)
anim.save('searching_for_' + str(to_find) + '.gif', writer='pillow')

# Showing the plot
plt.show()