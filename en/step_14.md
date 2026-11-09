## Make the ripples pulse

Give the water a little movement of its own by making each ripple grow and shrink.

On `water-ripples`{:class="block3looks"}, add a **second** `when I start as a clone`{:class="block3control"} script.

Inside a forever loop, increase the size by `5`, wait `0.1` seconds, then decrease it by `5` and wait again.

```blocks3
when I start as a clone
forever
change size by (5)
wait (0.1) seconds
change size by (-5)
wait (0.1) seconds
end
```

Both clone scripts run together: one moves the ripple up the river, and the other changes its size. When the movement script deletes the clone, both stop.

## Now run your code

Click the green flag. The ripples pulse as they drift through the water.
