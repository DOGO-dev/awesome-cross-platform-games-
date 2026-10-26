# Требования к данным игр по консолям

Ищите по **исходной консоли** игры и проверяйте точный формат, требуемый каждым проектом. Для Xbox, Xbox 360, PS4 и других систем могут понадобиться разные образы, дампы или файлы; мы не предполагаем, что всем нужен ISO.

> Репозиторий не размещает и не распространяет ссылки на загрузку игр, образов, ROM, BIOS, ключей или защищённых ресурсов. Здесь документируются только форматы и требования, указанные авторами проектов. Используйте законно полученные копии.

Расширенный список новых проверенных PC-портов и их требований к данным по консолям пока ведётся в [версии на испанском языке](README.md).

## Поиск системы

| Производитель | Консоли в каталоге | Статус требований |
|---|---|---|
| Sony | PlayStation, PlayStation 2, PSP, PlayStation 3, PlayStation 4 | Проверены требования для PlayStation, PS2 и PS4 |
| Microsoft | Xbox, Xbox 360 | Проверены требования для Xbox и Xbox 360 |
| Nintendo | NES, Game Boy/Color/Advance, SNES, Nintendo 64, Nintendo DS/3DS, GameCube, Wii, Wii U | Новые проверенные требования перечислены в испанском указателе |
| Другие | Dreamcast, аркадные и другие системы каталога | Форматы пока не задокументированы в этом указателе |

Список отражает исходные платформы, присутствующие в каталоге, но сам по себе не определяет формат, требуемый портом. Используйте Ctrl+F для поиска консоли, расширения или имени файла.

## Nintendo

### GameCube

| Игра | Проект/цель | Требуемые данные | Источник |
|---|---|---|---|
| Animal Crossing (USA, GAFE01 Rev 0) | [ACGC-PC-Port](https://github.com/flyngmt/ACGC-PC-Port) — ПК | Образ: `.iso`, `.gcm` или `.ciso` | [README: Requirements](https://github.com/flyngmt/ACGC-PC-Port#requirements) |
| Animal Crossing (USA, GAFE01 Rev 0) | [ACGC-Android-Port](https://github.com/zwaetschge/ACGC-Android-Port) — Android | Образ: `.iso`, `.gcm`, `.ciso` или `.nkit.iso` | [README](https://github.com/zwaetschge/ACGC-Android-Port) |

## Sony

### PlayStation

| Игра | Проект/цель | Требуемые данные | Источник |
|---|---|---|---|
| Crash Team Racing (NTSC-U) | [CTR Native](https://github.com/CTR-tools/ctr-native) — ПК | Оригинальный однодорожечный образ PSX raw BIN, MODE2/2352. ISO с секторами по 2048 байт не сохраняет необходимые секторы XA/STR. Извлечённые ресурсы необязательны для разработки/моддинга. | [README: Running](https://github.com/CTR-tools/ctr-native#running) |
| Crash Team Racing (NTSC-U) | [CTR Native Android](https://github.com/Simon358/ctr-native-android) — Android | Raw BIN `ctr-u.bin`; `BIGFILE.BIG` и другие извлечённые ресурсы поддерживаются как замена. | [Android README: Assets Setup](https://github.com/Simon358/ctr-native-android/blob/main/README_ANDROID.md#assets-setup-modern-android) |

### PlayStation 4

| Игра | Проект/цель | Требуемые данные | Источник |
|---|---|---|---|
| God of War III Remastered (CUSA01623 или CUSA01715, версии 01.00 или 01.02) | [gow3_pc](https://github.com/FelipePrado0/gow3_pc) — ПК | Собственный дамп PS4 в папке с `eboot.bin`, `sce_module` и `sce_sys`. ISO не указан. | [README: Download and play](https://github.com/FelipePrado0/gow3_pc#download-and-play) |

## Microsoft

### Xbox

| Игра | Проект/цель | Требуемые данные | Источник |
|---|---|---|---|
| Halo: Combat Evolved | [Halo CE Universal](https://github.com/cybersecurity/halo-ce-universal) — ПК, Android и Веб | Образ диска Xbox `.xiso` или `.iso`; проект извлекает папку `maps/`. | [README: Game data](https://github.com/cybersecurity/halo-ce-universal#game-data) |

### Xbox 360

| Игра | Проект/цель | Требуемые данные | Источник |
|---|---|---|---|
| Lost Odyssey (четыре диска; многоязычная азиатская или USA/Europe версия, не смешивать издания) | [Lost Odyssey Recomp](https://github.com/freefrank/LostOdysseyRecomp) — ПК, Android | Извлечённая папка, `default.xex`, ISO или данные GOD. Для запуска нужен диск 1. | [README: Start playing](https://github.com/freefrank/LostOdysseyRecomp#start-playing) |
| Sonic Unleashed (USA или Europe; версия для Японии не поддерживается) | [Unleashed Recompiled](https://github.com/hedge-dev/UnleashedRecomp) — ПК | Розничная или цифровая копия Xbox 360 и обязательное обновление игры. Установщик принимает контейнеры/образы, снятые с Xbox 360, или папку с исходными файлами; DLC необязательно. Документация не задаёт универсальное расширение файла. | [README: How to Install](https://github.com/hedge-dev/UnleashedRecomp#how-to-install) |

## Другие системы

Требования для остальных систем будут добавлены после того, как документация проекта подтвердит тип образа или файла.

## Словарь

- **Образ диска**: цифровая копия диска; формат может отличаться от `.iso`.
- **Raw BIN**: посекторный дамп, которому может требоваться определённый режим или размер сектора; он не всегда равнозначен ISO.
- **ROM**: дамп картриджа или другого оптического носителя.
- **Извлечённые ресурсы/файлы**: необходимые файлы игры, уже извлечённые из образа; они могут заменить или дополнить его.
- **Не проверено**: документация проекта пока не подтверждает требование; это не означает, что проекту не нужны данные игры.
