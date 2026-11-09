## Add river music

Play some quiet music while Tofu sleeps and swims.

Click on the `Stage`. At the end of its green-flag setup script, set the volume to `10%`, then add a forever loop.

Inside the loop, use `play sound (Flowers Passing By) until done`{:class="block3sound"}. Waiting for the track to finish lets it repeat from the beginning.

```blocks3
when green flag clicked
set [speed v] to (1)
set [score v] to (0)
set [health v] to (3)
set volume to (10) %
forever
play sound (Flowers Passing By v) until done
end
```

The Stage's volume setting affects its sounds. Tofu and the objects keep their own sound volumes.

## Now run your code

Click the green flag. Quiet music plays during the nap and continues into the game.

When health runs out, the existing `stop all`{:class="block3control"} block stops the music too.
