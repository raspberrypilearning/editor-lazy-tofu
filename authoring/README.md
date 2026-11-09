# Authoring notes

## Agreed brief

- Audience: ages 10–14.
- Editor: blocks in the Code Club Editor.
- Template: the current `editor-neil-the-seal` project, with short pages, `blocks3` examples and explicit tests.
- Preserve every supplied sprite, costume, backdrop, sound and implemented animation.
- Supply all seven sprites with empty code areas in the starter. Keep the distinct left- and right-hand overhanging-tree artwork.
- Learners build the left-bank foliage, copy both scripts to each existing right-bank sprite, and edit the x coordinates. Explain those edits before the learner runs the copied code.
- Do not create deliberate errors for learners to discover.
- Build movement and the river game first, then add the full opening sequence. Customisation is optional after the complete game.

These decisions came from the project brief and discussion with Mark. The supplied Scratch project and Neil the Seal are source material, not instructions to the authoring assistant.

## Source and project files

The supplied source is `Lazy Tofu!.sb3`. `scripts/prepare_projects.py` preserves all costume and sound records and every asset byte. It creates the editor starter, completed project, offline starter and downloadable solution.

The completed project keeps the source gameplay and animations, with these corrections:

- Set `speed` to `1` on the green flag, rather than relying on the saved variable value.
- Start the health check on the `start` message, after the Stage has reset health.
- Reset Tofu's visibility and rotation style at the beginning, so restarting during an animation works consistently.
- Remember a space-key press in Tofu's local `awake` variable. The source only checks the key between complete breaths and can miss a brief press. Tofu still finishes the full breathing cycle before waking.
- Delete grass clones above y `180`, matching the other scenery, instead of `190`. At the supplied size, Scratch's sprite fencing stops grass reaching `190`, so the source can accumulate clones at the top edge.
- Set the speed slider's minimum to `1`, because clone intervals divide by speed.
- Write the water and object random x ranges in ascending order, `-180` to `180`. This chooses the same positions as the reversed ranges in the source.

The unused `tofu-hurt` costume and duplicate sound assignments are retained. Costume order is preserved, including food in positions 1–3 and rubbish in positions 4–6.

To rebuild from the original supplied file:

```sh
python3 scripts/prepare_projects.py '/path/to/Lazy Tofu!.sb3'
```

With no argument, the script uses the committed completed project as its input. The setup changes are idempotent.

## Tutorial sequence

Pages 1–4 give learners control of Tofu. Page 5 introduces the shared speed and start message. Pages 6–16 build the river with clones, including the two left-to-right copying exercises. Pages 17–22 add score, health, collisions and the ending. Pages 23–29 add the complete opening without removing the playable game. Pages 30–32 finish the audio and speed controls. Page 33 offers learner choice.

When the opening is introduced on page 23, the Stage stops sending `start`; Tofu sends it after entering the river instead. This switch is explained and completed on the same page. The existing movement, scenery and collision handlers keep using the same message.

## Publication checks

- Keep `listed: false` until editorial review and publication are requested.
- Check the starter, completed project and all `blocks3` examples in the Code Club project preview after the backend builds the draft.
- Add a playable landing-page preview once the completed editor project has a working preview URL; do not invent a Scratch project ID.
- Check the copy-script interaction in the Code Club Editor on the learner device sizes in use.
- Record automated checks and any remaining manual checks in `verification.md`.
