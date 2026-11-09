# First-draft verification

Checked on 9 November 2026. This is a source and Scratch-runtime check, not acceptance in the Code Club project preview.

## Content and assets

- All 33 page headings match the ordered titles in `en/meta.yml`.
- All 39 `blocks3` examples parse and render with scratchblocks 3.7.1 without unrecognised blocks.
- Both editor configurations use `code_editor_scratch`, matching directory, identifier and SB3 names, with `build: true`.
- `listed` remains `false`.
- The starter has all seven sprites and the Stage, zero blocks, and no pre-created variables, lists, messages or monitors.
- Both projects preserve all 31 costume/backdrop records, 11 sound assignments and 33 unique asset files from the supplied source. Every asset byte and the costume order were compared with the original archive.
- Offline starter and downloadable solution are byte-identical to their editor counterparts.
- The preparation script can rebuild from either the original or the completed project without changing the generated project bytes.
- The banner is a direct capture of the running project's Stage, not replacement artwork.

Original supplied archive: `Lazy Tofu!.sb3`.

Original SHA-256: `6c98ea9570c14e5c3f6cf7ae9c3b2c949332aa3a65f87abab63af221a468ee7c`.

## Runtime checks passed

The starter and completed project were opened in headless Chrome using Scratch VM 5.0.300, the Scratch renderer, SVG bitmap adapter and audio engine.

- All 11 sound assignments decoded into audio players.
- Green flag resets speed, score and health, and waits for Tofu to wake before starting scenery and collision checks.
- A 100 ms space-key press is remembered while Tofu finishes breathing.
- Sleeping, waking, waving, running, jumping and splash costumes appear in the opening, followed by the game starting in the river.
- Tree clones use x `-180` and `180`; grass clones use the correct left- and right-bank ranges.
- Both arrow keys move and flip Tofu. The swimming costume and size return to rest after release.
- Food adds five points once and disappears without changing health.
- Rubbish removes one health, disappears and leaves score unchanged.
- Both banks' trees cause damage and reset Tofu to the middle.
- Grass clones delete at the top. The source's y `190` threshold was unreachable: the supplied grass size was fenced at y `183`. The corrected threshold is `180`.
- Zero health stops the running game scripts.
- Restarting during the jump returns Tofu to the nap and resets rotation, score and health.
- The starter renders with all seven sprites present and no blocks.

## Remaining manual checks

- Open the backend-built draft with its starter beside the instructions in the Code Club Editor.
- Check code copying between sprites, menu labels, monitor controls and page layout at the intended learner screen sizes.
- Complete a learner walkthrough of the incremental instructions; the runtime checks above used the completed project.
- Listen to the full mix on a learner device. Successful decoding is not a listening test.
- Add a playable landing-page preview after confirming the completed editor project's preview URL.

The repository contains a complete first draft. These checks remain before learner acceptance or publication.
