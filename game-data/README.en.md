# Game data requirements by console

Browse by the game's **original console** and check the exact format required by each project. Xbox, Xbox 360, PS4, and other systems may require different images, dumps, or files; we do not assume every project needs an ISO.

> This repository does not host or link downloads of games, images, ROMs, BIOS files, keys, or protected assets. It documents only formats and requirements stated by project authors. Use legally obtained copies.

The expanded index of newly verified PC ports and their per-console data requirements is currently maintained in the [Spanish version](README.md).

## Find a system

| Manufacturer | Consoles in the catalog | Requirement status |
|---|---|---|
| Sony | PlayStation, PlayStation 2, PSP, PlayStation 3, PlayStation 4 | Verified entries for PlayStation, PS2, and PS4 |
| Microsoft | Xbox, Xbox 360 | Verified entries for Xbox and Xbox 360 |
| Nintendo | NES, Game Boy/Color/Advance, SNES, Nintendo 64, Nintendo DS/3DS, GameCube, Wii, Wii U | Expanded verified entries are listed in the Spanish index |
| Other | Dreamcast, arcade, and other catalog systems | No formats documented in this index yet |

The system list reflects original platforms found in the catalog; it does not determine the format a port needs. Use Ctrl+F to search for a console, file extension, or filename.

## Nintendo

### GameCube

| Game | Project/target | Required data | Source |
|---|---|---|---|
| Animal Crossing (USA, GAFE01 Rev 0) | [ACGC-PC-Port](https://github.com/flyngmt/ACGC-PC-Port) — PC | Image: `.iso`, `.gcm`, or `.ciso` | [README: Requirements](https://github.com/flyngmt/ACGC-PC-Port#requirements) |
| Animal Crossing (USA, GAFE01 Rev 0) | [ACGC-Android-Port](https://github.com/zwaetschge/ACGC-Android-Port) — Android | Image: `.iso`, `.gcm`, `.ciso`, or `.nkit.iso` | [README](https://github.com/zwaetschge/ACGC-Android-Port) |

## Sony

### PlayStation

| Game | Project/target | Required data | Source |
|---|---|---|---|
| Crash Team Racing (NTSC-U) | [CTR Native](https://github.com/CTR-tools/ctr-native) — PC | Retail single-track raw PSX BIN image, MODE2/2352. A cooked 2048-byte ISO does not preserve the required XA/STR sectors. Extracted assets are optional for development/modding. | [README: Running](https://github.com/CTR-tools/ctr-native#running) |
| Crash Team Racing (NTSC-U) | [CTR Native Android](https://github.com/Simon358/ctr-native-android) — Android | Raw BIN `ctr-u.bin`; `BIGFILE.BIG` and other extracted assets are supported as overrides. | [Android README: Assets Setup](https://github.com/Simon358/ctr-native-android/blob/main/README_ANDROID.md#assets-setup-modern-android) |

### PlayStation 4

| Game | Project/target | Required data | Source |
|---|---|---|---|
| God of War III Remastered (CUSA01623 or CUSA01715, versions 01.00 or 01.02) | [gow3_pc](https://github.com/FelipePrado0/gow3_pc) — PC | Your own PS4 dump in a folder containing `eboot.bin`, `sce_module`, and `sce_sys`. An ISO is not specified. | [README: Download and play](https://github.com/FelipePrado0/gow3_pc#download-and-play) |

## Microsoft

### Xbox

| Game | Project/target | Required data | Source |
|---|---|---|---|
| Halo: Combat Evolved | [Halo CE Universal](https://github.com/cybersecurity/halo-ce-universal) — PC, Android, and Web | Xbox disc image `.xiso` or `.iso`; the project extracts the `maps/` folder. | [README: Game data](https://github.com/cybersecurity/halo-ce-universal#game-data) |

### Xbox 360

| Game | Project/target | Required data | Source |
|---|---|---|---|
| Lost Odyssey (four discs; multilingual Asian edition or USA/Europe, do not mix editions) | [Lost Odyssey Recomp](https://github.com/freefrank/LostOdysseyRecomp) — PC, Android | Extracted folder, `default.xex`, ISO, or GOD data. Disc 1 is required to start. | [README: Start playing](https://github.com/freefrank/LostOdysseyRecomp#start-playing) |
| Sonic Unleashed (USA or Europe; Japan is unsupported) | [Unleashed Recompiled](https://github.com/hedge-dev/UnleashedRecomp) — PC | Retail or digital Xbox 360 copy and mandatory title update. The installer accepts Xbox 360-dumped containers/images or the raw game files folder; DLC is optional. Documentation does not specify one universal file extension. | [README: How to Install](https://github.com/hedge-dev/UnleashedRecomp#how-to-install) |

## Other systems

Entries for other systems will be added when project documentation confirms the required image or file type.

## Glossary

- **Disc image**: a digital copy of a disc; it may use a format other than `.iso`.
- **Raw BIN**: a sector-by-sector dump that may require a specific mode or sector size; it is not always equivalent to an ISO.
- **ROM**: a dump of a cartridge or other non-optical media.
- **Extracted assets/files**: required game files that have already been extracted; they may replace or supplement an image.
- **Unverified**: the project documentation has not confirmed the requirement; this does not mean the project needs no game data.
