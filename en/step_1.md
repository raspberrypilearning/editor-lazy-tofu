## Make Tofu move

Start by getting **Tofu** swimming.

Add a `when green flag clicked`{:class="block3events"} block and a `forever`{:class="block3control"} loop.

Inside the loop, add an `if then else`{:class="block3control"} block to check whether the left arrow key is pressed. In the `then`{:class="block3control"} section, `point in direction -90`{:class="block3motion"} to face left, then `change x by -10`{:class="block3motion"} to move **Tofu** left.

Leave the `else`{:class="block3control"} section empty for now. You'll add `right-arrow`{:class="block3motion"} movement there next.

![Tofu sprite](images/sprite-tofu.png)

```blocks3
when green flag clicked
forever
if <key (left arrow v) pressed?> then
point in direction (-90)
change x by (-10)
else
end
end
```

## Now run your code

Click the green flag and press the left arrow. **Tofu** faces left and moves left.
