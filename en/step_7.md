## Move the tree clones

Make each tree travel up the screen. Together, the moving trees will make Tofu look as though they're travelling down the river.

Click on `tree-left`{:class="block3looks"} and find its `when I start as a clone`{:class="block3control"} script.

After `show`{:class="block3looks"}, add a `repeat until`{:class="block3control"} loop. Inside it, change y by `speed`{:class="block3variables"}.

Stop repeating when the clone's y position is greater than `180`, then delete the clone.

```blocks3
when I start as a clone
show
repeat until <(y position) > (180)>
change y by (speed)
end
delete this clone
```

A positive y change moves a sprite up. Deleting clones after they leave the screen makes room for new ones.

## Now run your code

Click the green flag and watch the left bank. Trees move from the bottom to the top, then disappear.
