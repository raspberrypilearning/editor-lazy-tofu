## Add a swimming splash

Make each swimming stroke sound like a little plunge, with a small change in size to give it movement.

## Step 1

In the `left-arrow`{:class="block3motion"} section, add `start sound (Plunge)`{:class="block3sound"} just after the costume change.

After `change x by ()`{:class="block3motion"}, add `change size by (2)`{:class="block3looks"}, `wait (0.1) seconds`{:class="block3control"} and `change size by (-2)`{:class="block3looks"}.

Inside your `left-arrow`{:class="block3motion"} section, the blocks should now be in this order:

![Tofu sprite](images/sprite-tofu.png)

```blocks3
switch costume to (tofu-swimming v)
+start sound (Plunge v)
point in direction (-90)
change x by (-10)
+change size by (2)
+wait (0.1) seconds
+change size by (-2)
```

## Step 2

Add the same sound and size changes to the `right-arrow`{:class="block3motion"} section.

The two size changes balance each other, so **Tofu** returns to the same size after each stroke.

## Now run your code

Move **Tofu** across the river. Each stroke has a sound and a little pulse, and the short wait makes the movement easier to control.
