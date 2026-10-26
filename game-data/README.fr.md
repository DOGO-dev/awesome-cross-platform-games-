# Besoins en données par console

Recherchez la **console d'origine** du jeu et vérifiez le format exact requis par chaque projet. Xbox, Xbox 360, PS4 et d'autres systèmes peuvent nécessiter des images, dumps ou fichiers différents ; nous ne supposons pas que tous les projets ont besoin d'un ISO.

> Ce dépôt n'héberge ni ne référence de téléchargements de jeux, d'images, de ROM, BIOS, clés ou ressources protégées. Il documente uniquement les formats et prérequis indiqués par les auteurs. Utilisez des copies obtenues légalement.

L'index détaillé des nouveaux ports PC vérifiés et de leurs données par console est actuellement disponible dans la [version espagnole](README.md).

## Rechercher un système

| Fabricant | Consoles du catalogue | État des prérequis |
|---|---|---|
| Sony | PlayStation, PlayStation 2, PSP, PlayStation 3, PlayStation 4 | Besoins vérifiés pour PlayStation, PS2 et PS4 |
| Microsoft | Xbox, Xbox 360 | Besoins vérifiés pour Xbox et Xbox 360 |
| Nintendo | NES, Game Boy/Color/Advance, SNES, Nintendo 64, Nintendo DS/3DS, GameCube, Wii, Wii U | Les nouveaux prérequis vérifiés figurent dans l'index espagnol |
| Autres | Dreamcast, arcade et autres systèmes du catalogue | Aucun format documenté dans cet index pour le moment |

La liste reflète les plateformes d'origine présentes dans le catalogue ; elle ne détermine pas le format requis par un port. Utilisez Ctrl+F pour rechercher une console, une extension ou un nom de fichier.

## Nintendo

### GameCube

| Jeu | Projet/cible | Données requises | Source |
|---|---|---|---|
| Animal Crossing (USA, GAFE01 Rev 0) | [ACGC-PC-Port](https://github.com/flyngmt/ACGC-PC-Port) — PC | Image : `.iso`, `.gcm` ou `.ciso` | [README: Requirements](https://github.com/flyngmt/ACGC-PC-Port#requirements) |
| Animal Crossing (USA, GAFE01 Rev 0) | [ACGC-Android-Port](https://github.com/zwaetschge/ACGC-Android-Port) — Android | Image : `.iso`, `.gcm`, `.ciso` ou `.nkit.iso` | [README](https://github.com/zwaetschge/ACGC-Android-Port) |

## Sony

### PlayStation

| Jeu | Projet/cible | Données requises | Source |
|---|---|---|---|
| Crash Team Racing (NTSC-U) | [CTR Native](https://github.com/CTR-tools/ctr-native) — PC | Image retail en BIN brut PSX d'une piste, MODE2/2352. Un ISO converti en secteurs de 2048 octets ne conserve pas les secteurs XA/STR requis. Les ressources extraites sont facultatives pour le développement/modding. | [README: Running](https://github.com/CTR-tools/ctr-native#running) |
| Crash Team Racing (NTSC-U) | [CTR Native Android](https://github.com/Simon358/ctr-native-android) — Android | BIN brut `ctr-u.bin` ; `BIGFILE.BIG` et d'autres ressources extraites sont acceptés en remplacement. | [README Android: Assets Setup](https://github.com/Simon358/ctr-native-android/blob/main/README_ANDROID.md#assets-setup-modern-android) |

### PlayStation 4

| Jeu | Projet/cible | Données requises | Source |
|---|---|---|---|
| God of War III Remastered (CUSA01623 ou CUSA01715, versions 01.00 ou 01.02) | [gow3_pc](https://github.com/FelipePrado0/gow3_pc) — PC | Dump PS4 obtenu par vos soins, dans un dossier contenant `eboot.bin`, `sce_module` et `sce_sys`. Aucun ISO n'est indiqué. | [README: Download and play](https://github.com/FelipePrado0/gow3_pc#download-and-play) |

## Microsoft

### Xbox

| Jeu | Projet/cible | Données requises | Source |
|---|---|---|---|
| Halo: Combat Evolved | [Halo CE Universal](https://github.com/cybersecurity/halo-ce-universal) — PC, Android et Web | Image de disque Xbox `.xiso` ou `.iso` ; le projet extrait le dossier `maps/`. | [README: Game data](https://github.com/cybersecurity/halo-ce-universal#game-data) |

### Xbox 360

| Jeu | Projet/cible | Données requises | Source |
|---|---|---|---|
| Lost Odyssey (quatre disques ; édition asiatique multilingue ou USA/Europe, sans mélanger les éditions) | [Lost Odyssey Recomp](https://github.com/freefrank/LostOdysseyRecomp) — PC, Android | Dossier extrait, `default.xex`, ISO ou données GOD. Le disque 1 est nécessaire au démarrage. | [README: Start playing](https://github.com/freefrank/LostOdysseyRecomp#start-playing) |
| Sonic Unleashed (USA ou Europe ; Japon non pris en charge) | [Unleashed Recompiled](https://github.com/hedge-dev/UnleashedRecomp) — PC | Copie retail ou numérique Xbox 360 et mise à jour obligatoire du jeu. L'installateur accepte les conteneurs/images extraits d'une Xbox 360 ou le dossier des fichiers d'origine ; le DLC est facultatif. La documentation ne définit pas d'extension universelle. | [README: How to Install](https://github.com/hedge-dev/UnleashedRecomp#how-to-install) |

## Autres systèmes

Les besoins pour les autres systèmes seront ajoutés lorsque la documentation du projet confirmera le type d'image ou de fichier requis.

## Glossaire

- **Image disque** : copie numérique d'un disque ; son format peut différer de `.iso`.
- **BIN brut** : dump secteur par secteur pouvant nécessiter un mode ou une taille de secteur précise ; il n'est pas toujours équivalent à un ISO.
- **ROM** : dump d'une cartouche ou d'un autre support non optique.
- **Ressources/fichiers extraits** : fichiers du jeu déjà extraits ; ils peuvent remplacer ou compléter une image.
- **Non vérifié** : la documentation du projet n'a pas encore confirmé le prérequis ; cela ne signifie pas que le projet n'a besoin d'aucune donnée du jeu.
