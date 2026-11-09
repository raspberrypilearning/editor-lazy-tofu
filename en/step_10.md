## Grow grass on the left bank

Use the same clone pattern for smaller plants. These will appear more often, at slightly different positions along the bank.

Click on `tree-left`{:class="block3looks"} and copy its two scripts to `grass-left`{:class="block3looks"}. Then click on `grass-left`{:class="block3looks"} to edit the copies.

## Step 1

In the generator script, add `go to back layer`{:class="block3looks"} after `hide`{:class="block3looks"}.

Move the `go to x: () y: ()`{:class="block3motion"} block **inside** the forever loop, before making the clone. Pick a random x from `-220` to `-180`, keeping y at `-200`.

Change the wait to `0.5` divided by `speed`{:class="block3variables"}.

```blocks3
when I receive [start v]
hide
go to [back v] layer
forever
go to x: (pick random (-220) to (-180)) y: (-200)
create clone of (myself v)
wait ((0.5) / (speed)) seconds
end
```

Choosing the position inside the loop gives each new plant its own spot.

## Step 2

The grass sprite has four costumes. In its clone script, change the random costume range to `1`–`4`.

Keep the y limit at `180`, so each plant deletes itself when it reaches the top.

```blocks3
when I start as a clone
switch costume to (pick random (1) to (4))
show
repeat until <(y position) > (180)>
change y by (speed)
end
delete this clone
```

## Now run your code

Click the green flag. Tufts, flowers, reeds and bushes move up the left bank, behind the trees.
