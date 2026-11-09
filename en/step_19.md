## Dodge the rubbish

Food is worth collecting, but rubbish should cost Tofu some health.

On `objects`{:class="block3looks"}, replace the **inner** `if then`{:class="block3control"} block, which checks the costume number, with `if then else`{:class="block3control"}.

Keep the food code in its first section. In `else`, change health by `-1`, start the `Scream1` sound and delete the clone.

```blocks3
if <touching (Tofu v)?> then
if <(costume [number v]) < (4)> then
change [score v] by (5)
start sound (Chomp v)
delete this clone
else
change [health v] by (-1)
start sound (Scream1 v)
delete this clone
end
end
```

The costume numbers `4`, `5` and `6` all go through `else`, so bottles, cans and crisp packets have the same effect.

## Now run your code

Click the green flag and touch a piece of rubbish. It disappears and health drops by `1`.

Try food too: it should still add points without taking health away.
