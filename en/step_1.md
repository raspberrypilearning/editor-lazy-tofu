## Make Tofu move

The starter project is open beside these instructions. It has all the sprites, costumes, backdrop and sounds you need, with empty code areas ready for your blocks.

You'll start by getting Tofu swimming. Later, you'll add the sleeping animation and the jump into the river.

Click on the `Tofu`{:class="block3looks"} sprite.

Add a `when green flag clicked`{:class="block3events"} block and a `forever`{:class="block3control"} loop.

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
