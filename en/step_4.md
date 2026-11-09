## Add a swimming splash

Make each swimming stroke sound like a little plunge, with a small change in size to give it movement.

Click on the `Tofu`{:class="block3looks"} sprite.

## Step 1

In each arrow-key section, add `start sound (Plunge)`{:class="block3sound"} just after the costume change.

After `change x by ()`{:class="block3motion"}, increase the size by `2`, wait `0.1` seconds, then decrease the size by `2`.

Inside your left-arrow section, the blocks should now be in this order:

```blocks3
switch costume to (tofu-swimming v)
start sound (Plunge v)
point in direction (-90)
change x by (-10)
change size by (2)
wait (0.1) seconds
change size by (-2)
```

Keep the arrow-key conditions and the `else` sections around your movement code.

## Step 2

Add the same sound and size changes to the right-arrow section. Keep its direction at `90` and its x change at `10`.

The two size changes balance each other, so Tofu returns to the same size after each stroke.

## Now run your code

Move Tofu across the river. Each stroke has a sound and a little pulse, and the short wait makes the movement easier to control.
