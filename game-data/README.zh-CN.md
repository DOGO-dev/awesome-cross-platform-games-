# 按主机分类的游戏数据要求

请按游戏的**原始主机平台**查找，并确认每个项目所需的具体格式。Xbox、Xbox 360、PS4 等系统可能需要不同的镜像、转储或文件；我们不会假设所有项目都需要 ISO。

> 本仓库不托管或链接游戏、镜像、ROM、BIOS、密钥或受保护资源的下载内容。这里只记录项目作者注明的格式和要求。请使用合法取得的副本。

新增已核实 PC 移植项目及其主机数据要求的完整索引目前维护在[西班牙语版本](README.md)中。

## 查找系统

| 厂商 | 目录中的主机 | 要求状态 |
|---|---|---|
| Sony | PlayStation、PlayStation 2、PSP、PlayStation 3、PlayStation 4 | PlayStation、PS2 和 PS4 有已核实条目 |
| Microsoft | Xbox、Xbox 360 | Xbox 和 Xbox 360 有已核实条目 |
| Nintendo | NES、Game Boy/Color/Advance、SNES、Nintendo 64、Nintendo DS/3DS、GameCube、Wii、Wii U | 新增的已核实要求请参阅西班牙语索引 |
| 其他 | Dreamcast、街机及目录中的其他系统 | 此索引尚未记录格式 |

系统列表反映目录中出现的原始平台，但不能据此推断移植项目所需格式。可使用 Ctrl+F 搜索主机、扩展名或文件名。

## Nintendo

### GameCube

| 游戏 | 项目/目标平台 | 所需数据 | 来源 |
|---|---|---|---|
| Animal Crossing (USA, GAFE01 Rev 0) | [ACGC-PC-Port](https://github.com/flyngmt/ACGC-PC-Port) — PC | 镜像：`.iso`、`.gcm` 或 `.ciso` | [README: Requirements](https://github.com/flyngmt/ACGC-PC-Port#requirements) |
| Animal Crossing (USA, GAFE01 Rev 0) | [ACGC-Android-Port](https://github.com/zwaetschge/ACGC-Android-Port) — Android | 镜像：`.iso`、`.gcm`、`.ciso` 或 `.nkit.iso` | [README](https://github.com/zwaetschge/ACGC-Android-Port) |

## Sony

### PlayStation

| 游戏 | 项目/目标平台 | 所需数据 | 来源 |
|---|---|---|---|
| Crash Team Racing (NTSC-U) | [CTR Native](https://github.com/CTR-tools/ctr-native) — PC | 零售版单轨 PSX 原始 BIN 镜像，MODE2/2352。转换为 2048 字节扇区的 ISO 不包含所需的 XA/STR 扇区。开发/修改时可选用已提取资源。 | [README: Running](https://github.com/CTR-tools/ctr-native#running) |
| Crash Team Racing (NTSC-U) | [CTR Native Android](https://github.com/Simon358/ctr-native-android) — Android | 原始 BIN `ctr-u.bin`；支持用 `BIGFILE.BIG` 和其他已提取资源覆盖。 | [Android README: Assets Setup](https://github.com/Simon358/ctr-native-android/blob/main/README_ANDROID.md#assets-setup-modern-android) |

### PlayStation 4

| 游戏 | 项目/目标平台 | 所需数据 | 来源 |
|---|---|---|---|
| God of War III Remastered (CUSA01623 或 CUSA01715，版本 01.00 或 01.02) | [gow3_pc](https://github.com/FelipePrado0/gow3_pc) — PC | 自行转储的 PS4 游戏文件夹，包含 `eboot.bin`、`sce_module` 和 `sce_sys`。文档未要求 ISO。 | [README: Download and play](https://github.com/FelipePrado0/gow3_pc#download-and-play) |

## Microsoft

### Xbox

| 游戏 | 项目/目标平台 | 所需数据 | 来源 |
|---|---|---|---|
| Halo: Combat Evolved | [Halo CE Universal](https://github.com/cybersecurity/halo-ce-universal) — PC、Android 和 Web | Xbox 光盘镜像 `.xiso` 或 `.iso`；项目会提取 `maps/` 文件夹。 | [README: Game data](https://github.com/cybersecurity/halo-ce-universal#game-data) |

### Xbox 360

| 游戏 | 项目/目标平台 | 所需数据 | 来源 |
|---|---|---|---|
| Lost Odyssey（四张光盘；多语言亚洲版或 USA/欧洲版，不要混用版本） | [Lost Odyssey Recomp](https://github.com/freefrank/LostOdysseyRecomp) — PC、Android | 已提取的文件夹、`default.xex`、ISO 或 GOD 数据。启动需要第 1 张光盘。 | [README: Start playing](https://github.com/freefrank/LostOdysseyRecomp#start-playing) |
| Sonic Unleashed（USA 或欧洲版；不支持日本版） | [Unleashed Recompiled](https://github.com/hedge-dev/UnleashedRecomp) — PC | Xbox 360 零售版或数字版，以及必需的游戏更新。安装器接受从 Xbox 360 转储的容器/镜像或原始游戏文件夹；DLC 可选。文档未规定统一扩展名。 | [README: How to Install](https://github.com/hedge-dev/UnleashedRecomp#how-to-install) |

## 其他系统

只有在项目文档确认所需镜像或文件类型后，才会添加其他系统的条目。

## 术语表

- **光盘镜像**：光盘内容的数字副本；格式可能不是 `.iso`。
- **原始 BIN**：逐扇区转储，可能要求特定模式或扇区大小；不一定等同于 ISO。
- **ROM**：卡带或其他非光学介质的转储。
- **已提取资源/文件**：已从游戏中提取的必需文件；可替代或补充镜像。
- **尚未核实**：项目文档尚未确认要求；这不代表项目不需要游戏数据。
