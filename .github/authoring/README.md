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

The completed project is based on Mark's updated `Lazy Tofu! (1).sb3`, with four breathing cycles followed by a space-key wait. The starter is the supplied `editor-lazy-tofu-starter.sb3`, copied byte-for-byte, including its saved sprite properties and default `my variable` variable.

The editor project identifiers, code folders and SB3 filenames are `editor-lazy-tofu-starter` and `editor-lazy-tofu-complete`. Both `project_config.yml` files use `type: 'code_editor_scratch'` and `build: true`.

`.github/authoring/prepare_projects.py` preserves all costume and sound records and every asset byte in the completed project. It keeps the supplied starter unchanged and synchronises the offline starter and downloadable solution.

Keep authoring notes and tools under `.github/authoring/`. The site importer treats additional top-level directories as project content: the original top-level `authoring` folder caused an `authoring/images missing` import failure.

The completed project keeps the source gameplay and animations, with these corrections:

- Set `speed` to `1` on the green flag, rather than relying on the saved variable value.
- Start the health check on the `start` message, after the Stage has reset health.
- Reset Tofu's visibility and rotation style at the beginning, so restarting during an animation works consistently.
- Keep Mark's updated sleeping sequence: `repeat (4)` around the breathing animation, then `wait until <key (space) pressed?>` outside the loop. The earlier `awake` variable and keypress script are removed.
- Delete grass clones above y `180`, matching the other scenery, instead of `190`. At the supplied size, Scratch's sprite fencing stops grass reaching `190`, so the source can accumulate clones at the top edge.
- Set the speed slider's minimum to `1`, because clone intervals divide by speed.
- Write the water and object random x ranges in ascending order, `-180` to `180`. This chooses the same positions as the reversed ranges in the source.
- Start trees at y `-300` and delete them above y `220`, matching the revised tutorial.
- Use one shared clone-deletion block after the food/rubbish conditional, plus the existing deletion after the movement loop.
- Restore `left-right` rotation immediately after the waddle loop, before the jump costume, matching its introduction in step 23.

The unused `tofu-hurt` costume and duplicate sound assignments are retained. Costume order is preserved, including food in positions 1–3 and rubbish in positions 4–6.

To rebuild from the original supplied file:

```sh
python3 .github/authoring/prepare_projects.py '/path/to/Lazy Tofu! (1).sb3'
```

With no argument, the script uses the committed completed project as its input. The setup changes are idempotent. It never generates a replacement starter from the completed project.

To import an updated supplied starter while rebuilding:

```sh
python3 .github/authoring/prepare_projects.py --starter '/path/to/editor-lazy-tofu-starter.sb3'
```

## Tutorial sequence

Use bold for sprite names in prose; retain Scratch block colours for block labels and costume names. Each page has one "Now run your code" section; intermediate tests do not repeat the heading.

Refer to scripts by their starting block or visible behaviour; do not use the term "generator" in learner instructions.

Style the words `left-arrow` and `right-arrow` with `block3motion` in learner instructions.

Keep learner instructions brief. Avoid black inline-code highlighting wherever possible: use the matching Scratch block colour for block names, parts, options and values. For example, `then` and `else` use `block3control`, while movement amounts, directions and rotation styles use `block3motion`. Match each number to the block it belongs to; use plain text for ordinary prose.

Let the sprite and Stage cards identify where to code; omit repeated sprite-selection instructions. Keep source and destination names where needed for copying scripts. Focus on additions and changes, without reminders to keep unchanged code unless a specific edit makes that clarification necessary.

Place the appropriate labelled card from `en/images/sprite-*.png` directly above each script, with no intervening instructions. Always include a card above the first script in every Markdown file, even when continuing with the same sprite from the previous page. Use the Stage card for Stage scripts and the destination sprite's card above copied scripts being edited. If a page asks learners to select a sprite or the Stage but shows no script, place its card beside the selection instruction. The cards use each target's saved costume in the starter and preserve the different left- and right-bank artwork. Regenerate them with `.github/authoring/make_sprite_cards.py` (Pillow and `rsvg-convert` required).

Each editor-project page must produce an observable change to the game. Pages 1–4 give learners control of Tofu. Pages 5–14 build the river with clones, including the two left-to-right copying exercises. Page 5 starts the tree generator on the green flag; page 6 introduces the shared speed and start message alongside tree movement, switching both the Tofu movement loop and tree generator to the message. Pages 15–18 add score, health, collisions and the ending. Page 19 adds river music. Pages 20–24 add the complete opening without removing the playable game. Pages 25–26 finish the sound and speed controls, with optional customisation ideas at the end of page 26.

When the opening is introduced on page 20, the Stage stops sending `start`; Tofu sends it after entering the river instead. This switch is explained and completed on the same page. The existing movement, scenery and collision handlers keep using the same message.

## Publication checks

- Keep `listed: false` until editorial review and publication are requested.
- Check the starter, completed project and all `blocks3` examples in the Code Club project preview after the backend builds the draft.
- Add a playable landing-page preview once the completed editor project has a working preview URL; do not invent a Scratch project ID.
- Check the copy-script interaction in the Code Club Editor on the learner device sizes in use.
- Record automated checks and any remaining manual checks in `verification.md`.
