## Swim both ways

Give Tofu a way to swim back across the river, facing the direction of travel.

You're still working on the `Tofu`{:class="block3looks"} sprite.

Keep the left-arrow movement in the `then` section of your `if then else`{:class="block3control"} block.

In the empty `else` section, add an `if then`{:class="block3control"} block that checks whether the right arrow key is pressed. Inside it, change x by `10` to move Tofu right.

Before the new `change x by (10)`{:class="block3motion"} block, add `point in direction (90)`{:class="block3motion"} to face right. Keep direction `-90` in the left-arrow section.

![Tofu sprite](images/sprite-tofu.png)

```blocks3
when green flag clicked
forever
if <key (left arrow v) pressed?> then
point in direction (-90)
change x by (-10)
else
+if <key (right arrow v) pressed?> then
point in direction (90)
change x by (10)
end
end
end
```

## Now run your code

Click the green flag and try both arrow keys. Tofu faces the way you move.

The `left-right` rotation style flips the artwork without turning Tofu upside down.
