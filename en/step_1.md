## Make Tofu move

The starter project is open beside these instructions. It has all the sprites, costumes, backdrop and sounds you need, with empty code areas ready for your blocks.

You'll start by getting Tofu swimming. Later, you'll add the nap and the jump into the river.

Click on the `Tofu`{:class="block3looks"} sprite.

## Step 1

Make Tofu start in the middle of the river. Set the size, direction and costume so each new game starts the same way.

```blocks3
when green flag clicked
go to x: (0) y: (0)
set size to (23) %
point in direction (90)
set rotation style [left-right v]
show
switch costume to (tofu v)
```

## Step 2

Add another `when green flag clicked`{:class="block3events"} block and a `forever`{:class="block3control"} loop.

Inside the loop, check whether the left arrow key is pressed. A negative change in x moves Tofu left.

```blocks3
when green flag clicked
forever
if <key (left arrow v) pressed?> then
change x by (-10)
end
end
```

## Now run your code

Click the green flag and press the left arrow. Tofu moves left.

Click the green flag again to return Tofu to the middle.
