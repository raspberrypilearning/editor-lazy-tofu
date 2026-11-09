# First-draft verification

Checked on 9 November 2026. This is a source and Scratch-runtime check, not acceptance in the Code Club project preview.

## Content and assets

- All 33 page headings match the ordered titles in `en/meta.yml`.
- All 38 current `blocks3` examples parse with scratchblocks 3.7.1 without unrecognised blocks.
- Both editor configurations use `code_editor_scratch`, matching directory, identifier and SB3 names, with `build: true`.
- `listed` remains `false`.
- The supplied starter has all seven sprites and the Stage, zero blocks, and no lists, messages or monitors. Its default `my variable` variable and saved sprite properties are retained unchanged.
- Both projects preserve all 31 costume/backdrop records, 11 sound assignments and 33 unique asset files from the supplied source. Every asset byte and the costume order were compared with the original archive.
- Offline starter and downloadable solution are byte-identical to their editor counterparts.
- The preparation script can rebuild from either the original or the completed project without changing the generated project bytes.
- The banner is a direct capture of the running project's Stage, not replacement artwork.

Original supplied archive: `Lazy Tofu!.sb3`.

Original SHA-256: `6c98ea9570c14e5c3f6cf7ae9c3b2c949332aa3a65f87abab63af221a468ee7c`.

## Earlier runtime checks

The starter and completed project were opened in headless Chrome using Scratch VM 5.0.300, the Scratch renderer, SVG bitmap adapter and audio engine.

- All 11 sound assignments decoded into audio players.
- Green flag resets speed, score and health, and waits for Tofu to wake before starting scenery and collision checks.
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

## Supplied-starter update

Mark supplied `editor-lazy-tofu-starter.sb3` on 9 November 2026 to replace the generated starter. The editor starter and offline download are exact copies of that file. The project preparation script now preserves this supplied starter rather than regenerating it.

The replacement starter was opened and rendered in the same Scratch runtime: the Stage and seven sprites loaded with zero blocks, all 11 sound assignments decoded, and Tofu's supplied sleeping position, size and costume were retained. Its 33 asset files and all costume and sound records were compared with the original archive and match exactly.

Supplied starter SHA-256: `f8273e9d269e78a017a9151d5087cb29b45d96383f55ac23b6c9fd65b4570147`.

The starter and completed identifiers, code directories and SB3 filenames are now `editor-lazy-tofu-starter` and `editor-lazy-tofu-complete`. Both project YAML files retain `build: true` and `type: 'code_editor_scratch'`. The completed SB3 content is unchanged by this naming update.

## Import layout correction

The site rejected the initial imports with `Expected a file or directory at authoring/images`, reported in [issue 4](https://github.com/raspberrypilearning/editor-lazy-tofu/issues/4) and three earlier duplicate reports. The webhook had accepted the push; the site import had failed afterwards.

Authoring notes and the preparation script were moved into the existing `.github/authoring/` area so the importer only sees `en` as project content. `listed: false` and both `build: true` settings are retained. A GitHub push alone is not proof of a successful site import.

## Four-breath sleeping-animation update

Mark supplied `Lazy Tofu! (1).sb3` and updated the shared Scratch project on 9 November 2026. The source uses four complete breathing cycles, followed by `wait until <key (space) pressed?>` outside the loop. The instructions and completed archives now match this sequence; the temporary `awake` variable and keypress script are removed.

Updated source SHA-256: `6cf90e012f6daf5e9c365966f2d728f8f8444431a8d225fc9e338cf10f05d703`.

Updated completed archive SHA-256: `d96dc390cee7509de5f80f4d896e00fcfbde49096b974382260e310ec114c029` (258 blocks). The starter is unchanged.

A focused Scratch VM logic check confirmed exactly 40 growth and 40 shrink changes across four cycles, no early start from a released keypress during breathing, a persistent space-key wait afterwards, and the full wave/waddle/jump/splash before the river starts. Restarting restores the sleeping state and removes old clones. This check did not render images or play audio; the asset bytes and costume/sound records are preserved.

Both guides use “add the sleeping animation” rather than “add the nap”. The current editor guide has 38 code examples; all parse without unrecognised blocks.

The manual checks above remain before full learner acceptance.
