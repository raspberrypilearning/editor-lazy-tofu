## Swim both ways

Give Tofu a way to swim back across the river, facing the direction of travel.

In the empty `else`{:class="block3control"} section, add an `if then else`{:class="block3control"} block that checks whether the right arrow key is pressed.

In its `then`{:class="block3control"} section, add `point in direction (90)`{:class="block3motion"} and `change x by (10)`{:class="block3motion"}. Leave its `else`{:class="block3control"} section empty.

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
else
end
end
end
```

## Now run your code

Click the green flag and try both arrow keys. Tofu faces the way you move.
