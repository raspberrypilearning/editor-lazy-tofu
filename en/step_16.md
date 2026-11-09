## Make the objects bob

Add a smaller version of the ripples' pulsing effect to the floating objects.

On `objects`{:class="block3looks"}, add a second `when I start as a clone`{:class="block3control"} script.

Change the size by `2`, wait, change it by `-2`, then wait again. Repeat this in a forever loop.

```blocks3
when I start as a clone
forever
change size by (2)
wait (0.1) seconds
change size by (-2)
wait (0.1) seconds
end
```

You can also copy the ripple's size-changing script and change both size values.

## Now run your code

Click the green flag. Food and rubbish bob as they pass Tofu.
