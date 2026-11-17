## Make Tofu move

The starter project is open beside these instructions. It has all the sprites, costumes, backdrop and sounds you need, with empty code areas ready for your blocks.

You'll start by getting Tofu swimming. Later, you'll add the sleeping animation and the jump into the river.

Click on the `Tofu`{:class="block3looks"} sprite.

Add a `when green flag clicked`{:class="block3events"} block and a `forever`{:class="block3control"} loop.

Inside the loop, add an `if then else`{:class="block3control"} block to check whether the left arrow key is pressed. In the `then` section, point in direction `-90` to face left, then change x by `-10` to move Tofu left.

Leave the `else` section empty for now. You'll add right-arrow movement there next.

![Tofu sprite](images/sprite-tofu.png)

```blocks3
when green flag clicked
forever
if <key (left arrow v) pressed?> then
point in direction (-90)
change x by (-10)
else
end
end
```

## Now run your code

Click the green flag and press the left arrow. Tofu faces left and moves left.
