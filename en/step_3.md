## Change Tofu's costume

Tofu has a swimming costume ready to use. Show it while moving, then return to the resting pose when neither arrow key is pressed.

Click on the `Tofu`{:class="block3looks"} sprite.

Add `switch costume to (tofu-swimming)`{:class="block3looks"} at the beginning of each arrow-key section.

Replace the right-arrow `if then`{:class="block3control"} with an `if then else`{:class="block3control"} block. Use its new `else` section to switch back to `tofu`.

```blocks3
when green flag clicked
forever
if <key (left arrow v) pressed?> then
switch costume to (tofu-swimming v)
point in direction (-90)
change x by (-10)
else
if <key (right arrow v) pressed?> then
switch costume to (tofu-swimming v)
point in direction (90)
change x by (10)
else
switch costume to (tofu v)
end
end
end
```

## Now run your code

Move Tofu left and right, then release the keys. The swimming pose appears during movement and the resting pose returns afterwards.
