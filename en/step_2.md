## Swim both ways

Give Tofu a way to swim back across the river, facing the direction of travel.

You're still working on the `Tofu`{:class="block3looks"} sprite.

Replace the movement loop's `if then`{:class="block3control"} block with an `if then else`{:class="block3control"} block. Keep the left-arrow movement in its first section.

In the `else` section, add another `if then`{:class="block3control"} block for the right arrow.

Use direction `-90` to face left and `90` to face right.

```blocks3
when green flag clicked
forever
if <key (left arrow v) pressed?> then
point in direction (-90)
change x by (-10)
else
if <key (right arrow v) pressed?> then
point in direction (90)
change x by (10)
end
end
end
```

## Now run your code

Click the green flag and try both arrow keys. Tofu faces the way you move.

The `left-right` rotation style flips the artwork without turning Tofu upside down.
