# Requisitos de datos por consola

[Español](README.md) · [English](README.en.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Français](README.fr.md)

Busca por la **consola original** y revisa el formato exacto que pide cada proyecto. Xbox, Xbox 360, PS4 y otros sistemas pueden requerir imágenes, volcados o archivos distintos: no asumimos que todos necesiten un ISO.

> El repositorio no aloja ni enlaza descargas de juegos, imágenes, ROMs, BIOS, claves ni assets protegidos. Solo documenta formatos y requisitos indicados por los autores. Usa copias obtenidas legalmente.

## Buscar un sistema

| Fabricante | Consolas incluidas en el catálogo | Estado de los requisitos |
|---|---|---|
| Sony | [PlayStation](#playstation), [PlayStation 2](#playstation-2), PSP, PlayStation 3, [PlayStation 4](#playstation-4) | PlayStation, PS2 y PS4 tienen entradas verificadas |
| Microsoft | [Xbox](#xbox), [Xbox 360](#xbox-360) | Xbox y Xbox 360 tienen entradas verificadas |
| Nintendo | NES, Game Boy/Color/Advance, [SNES](#snes), [Nintendo 64](#nintendo-64), Nintendo DS/3DS, [GameCube](#gamecube), [Wii](#wii), Wii U | SNES, Nintendo 64, GameCube y Wii tienen entradas verificadas |
| Otros | Dreamcast, arcade y otros sistemas del catálogo | Aún sin formato documentado en este índice |

La lista de sistemas refleja las plataformas originales presentes en el catálogo; no indica por sí sola qué formato pide un port. Usa Ctrl+F para buscar una consola, extensión o nombre de archivo.

## Nintendo

### GameCube

| Juego | Proyecto/destino | Datos requeridos | Fuente |
|---|---|---|---|
| Animal Crossing (USA, GAFE01 Rev 0) | [ACGC-PC-Port](https://github.com/flyngmt/ACGC-PC-Port) — PC | Imagen: `.iso`, `.gcm` o `.ciso` | [README: Requirements](https://github.com/flyngmt/ACGC-PC-Port#requirements) |
| Animal Crossing (USA, GAFE01 Rev 0) | [ACGC-Android-Port](https://github.com/zwaetschge/ACGC-Android-Port) — Android | Imagen: `.iso`, `.gcm`, `.ciso` o `.nkit.iso` | [README](https://github.com/zwaetschge/ACGC-Android-Port) |
| Scooby-Doo! Night of 100 Frights (USA v1.01, GIHE78 rev. 1) | [Scooby-Doo-Refrightened](https://github.com/josiahg2502-glitch/Scooby-Doo-Refrightened) — PC | ISO de GameCube USA v1.01. | [README](https://github.com/josiahg2502-glitch/Scooby-Doo-Refrightened#readme) |

### Nintendo 64

| Juego | Proyecto/destino | Datos requeridos | Fuente |
|---|---|---|---|
| Glover (USA) | [Glover-R](https://github.com/ThatGuyMcd/Glover-R) — PC | ROM USA; acepta `.z64`, `.n64` y `.v64`. | [README](https://github.com/ThatGuyMcd/Glover-R#readme) |

### SNES

| Juego | Proyecto/destino | Datos requeridos | Fuente |
|---|---|---|---|
| Go! Go! Ackman | [gogoackman1recomp](https://github.com/catmidori/gogoackman1recomp) — PC | ROM/dump de SNES; el formato exacto no está especificado. | [README](https://github.com/catmidori/gogoackman1recomp#readme) |

### Wii

| Juego | Proyecto/destino | Datos requeridos | Fuente |
|---|---|---|---|
| Pandora's Tower | [pandora-tower-pc](https://github.com/RecompPort/pandora-tower-pc) — PC | ISO propia de Wii; la ficha de PortIntegration indica que la recompilación se genera durante la instalación. | [Repositorio](https://github.com/RecompPort/pandora-tower-pc) |
| Super Paper Mario | [NewSuperPaperBros](https://github.com/josiahg2502-glitch/NewSuperPaperBros) — PC | Dump/imagen propia del disco de Wii; el formato exacto no está especificado. | [README](https://github.com/josiahg2502-glitch/NewSuperPaperBros#readme) |

## Sony

### PlayStation

| Juego | Proyecto/destino | Datos requeridos | Fuente |
|---|---|---|---|
| Crash Team Racing (NTSC-U) | [CTR Native](https://github.com/CTR-tools/ctr-native) — PC | Imagen retail BIN cruda PSX de una pista, MODE2/2352. Un ISO cocido de 2048 bytes no conserva los sectores XA/STR necesarios. Assets extraídos opcionales para desarrollo/modding. | [README: Running](https://github.com/CTR-tools/ctr-native#running) |
| Crash Team Racing (NTSC-U) | [CTR Native Android](https://github.com/Simon358/ctr-native-android) — Android | BIN crudo `ctr-u.bin`; `BIGFILE.BIG` y otros assets extraídos se admiten como override. | [README Android: Assets Setup](https://github.com/Simon358/ctr-native-android/blob/main/README_ANDROID.md#assets-setup-modern-android) |

### PlayStation 2

| Juego | Proyecto/destino | Datos requeridos | Fuente |
|---|---|---|---|
| Ridge Racer V (USA, SLUS-20002) | [Fukami](https://github.com/danisandoval/fukami) — PC | Volcado propio de la versión USA; la extensión/formato de imagen no está especificado. | [README](https://github.com/danisandoval/fukami#readme) |

### PlayStation 4

| Juego | Proyecto/destino | Datos requeridos | Fuente |
|---|---|---|---|
| God of War III Remastered (CUSA01623 o CUSA01715, versiones 01.00 o 01.02) | [gow3_pc](https://github.com/FelipePrado0/gow3_pc) — PC | Volcado propio de PS4 en carpeta con `eboot.bin`, `sce_module` y `sce_sys`. No se indica un ISO. | [README: Download and play](https://github.com/FelipePrado0/gow3_pc#download-and-play) |

## Microsoft

### Xbox

| Juego | Proyecto/destino | Datos requeridos | Fuente |
|---|---|---|---|
| Halo: Combat Evolved | [Halo CE Universal](https://github.com/cybersecurity/halo-ce-universal) — PC, Android y Web | Imagen de disco Xbox `.xiso` o `.iso`; el proyecto extrae la carpeta `maps/`. | [README: Game data](https://github.com/cybersecurity/halo-ce-universal#game-data) |
| Call of Duty: Finest Hour | [FinestHourRemastered](https://github.com/crazyriddler/FinestHourRemastered) — PC | Imagen compatible: `.iso`, imagen Redump completa o XISO. | [README](https://github.com/crazyriddler/FinestHourRemastered#readme) |

### Xbox 360

| Juego | Proyecto/destino | Datos requeridos | Fuente |
|---|---|---|---|
| 3 on 3 NHL Arcade (Title ID 58410975) | [3on3NHL-recomp](https://github.com/Wndwsqrrl/3on3NHL-recomp) — PC | Paquete propio de Xbox Live Arcade; no es una ISO. | [README](https://github.com/Wndwsqrrl/3on3NHL-recomp#readme) |
| Kameo: Elements of Power | [KameoRePowered](https://github.com/MaxDeadBear/KameoRePowered) — PC | ISO propia de Xbox 360 (`kameo.iso`). | [README](https://github.com/MaxDeadBear/KameoRePowered#readme) |
| Naruto: The Broken Bond | [Naruto-The-Broken-Bond-PC-Port](https://github.com/Auremana666/Naruto-The-Broken-Bond-PC-Port) — PC | ISO propia de Xbox 360. | [README](https://github.com/Auremana666/Naruto-The-Broken-Bond-PC-Port#readme) |
| Lost Odyssey (cuatro discos; edición asiática multilingüe o USA/Europa, sin mezclar ediciones) | [Lost Odyssey Recomp](https://github.com/freefrank/LostOdysseyRecomp) — PC, Android | Carpeta extraída, `default.xex`, ISO o datos GOD. El disco 1 es necesario para iniciar. | [README: Start playing](https://github.com/freefrank/LostOdysseyRecomp#start-playing) |
| Sonic Unleashed (USA o Europa; Japón no compatible) | [Unleashed Recompiled](https://github.com/hedge-dev/UnleashedRecomp) — PC | Copia retail o digital de Xbox 360 y actualización obligatoria. El instalador acepta contenedores/imágenes volcados desde Xbox 360 o la carpeta de archivos originales; DLC opcional. La documentación no establece una extensión universal. | [README: How to Install](https://github.com/hedge-dev/UnleashedRecomp#how-to-install) |
| Lost Odyssey (cuatro discos; edición asiática multilingüe o USA/Europa, sin mezclar ediciones) | [LostOdysseyRecomp](https://github.com/faligame/lost-odyssey-hd-remaster) — PC | Carpeta extraída, `default.xex`, ISO o datos Games on Demand. El disco 1 es necesario para iniciar. | [README: Start playing](https://github.com/faligame/lost-odyssey-hd-remaster#start-playing) |

## Otros sistemas

Para los demás sistemas, se añadirán entradas cuando la documentación del proyecto confirme el tipo de imagen o archivo requerido.

## Glosario

- **Imagen de disco**: copia digital de un disco; puede usar un formato distinto de `.iso`.
- **BIN crudo**: volcado sector por sector cuyo modo o tamaño de sector puede ser necesario; no equivale siempre a un ISO.
- **ROM**: volcado de un cartucho u otro medio no óptico.
- **Assets/archivos extraídos**: archivos del juego requeridos ya extraídos; pueden sustituir o complementar una imagen.
- **No verificado**: aún no se confirmó el requisito en documentación del proyecto; no significa que el proyecto no necesite datos.
