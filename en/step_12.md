## Add river ripples

Moving ripples will make the water look as though it's flowing too.

Copy both scripts from `grass-left`{:class="block3looks"} to `water-ripples`{:class="block3looks"}, then select `water-ripples`{:class="block3looks"}.

## Step 1

In the generator, change the random x range to `-180`–`180`. This puts the clones in the water between the banks.

Change the wait to a random number from `1` to `2`, divided by `speed`{:class="block3variables"}.

```blocks3
when I receive [start v]
hide
go to [back v] layer
forever
go to x: (pick random (-180) to (180)) y: (-200)
create clone of (myself v)
wait ((pick random (1) to (2)) / (speed)) seconds
end
```

## Step 2

In the clone script, replace the random costume choice with `water-ripples`. Change the y limit to `180`.

```blocks3
when I start as a clone
switch costume to (water-ripples v)
show
repeat until <(y position) > (180)>
change y by (speed)
end
delete this clone
```

## Now run your code

Click the green flag. Ripples travel through the river at the same speed as the plants on the banks.
