# Requisitos de dados por console

Pesquise pelo **console original** do jogo e confira o formato exato exigido por cada projeto. Xbox, Xbox 360, PS4 e outros sistemas podem exigir imagens, dumps ou arquivos diferentes; não presumimos que todos precisem de ISO.

> Este repositório não hospeda nem indica downloads de jogos, imagens, ROMs, BIOS, chaves ou assets protegidos. Ele apenas documenta formatos e requisitos informados pelos autores dos projetos. Use cópias obtidas legalmente.

O índice ampliado dos novos ports verificados para PC e seus requisitos de dados por console está atualmente na [versão em espanhol](README.md).

## Encontrar um sistema

| Fabricante | Consoles incluídos no catálogo | Estado dos requisitos |
|---|---|---|
| Sony | PlayStation, PlayStation 2, PSP, PlayStation 3, PlayStation 4 | Requisitos verificados para PlayStation, PS2 e PS4 |
| Microsoft | Xbox, Xbox 360 | Requisitos verificados para Xbox e Xbox 360 |
| Nintendo | NES, Game Boy/Color/Advance, SNES, Nintendo 64, Nintendo DS/3DS, GameCube, Wii, Wii U | O índice em espanhol contém os novos requisitos verificados |
| Outros | Dreamcast, arcade e outros sistemas do catálogo | Ainda não há formatos documentados neste índice |

A lista reflete as plataformas originais presentes no catálogo; ela não determina o formato exigido por um port. Use Ctrl+F para pesquisar um console, extensão ou nome de arquivo.

## Nintendo

### GameCube

| Jogo | Projeto/destino | Dados necessários | Fonte |
|---|---|---|---|
| Animal Crossing (USA, GAFE01 Rev 0) | [ACGC-PC-Port](https://github.com/flyngmt/ACGC-PC-Port) — PC | Imagem: `.iso`, `.gcm` ou `.ciso` | [README: Requirements](https://github.com/flyngmt/ACGC-PC-Port#requirements) |
| Animal Crossing (USA, GAFE01 Rev 0) | [ACGC-Android-Port](https://github.com/zwaetschge/ACGC-Android-Port) — Android | Imagem: `.iso`, `.gcm`, `.ciso` ou `.nkit.iso` | [README](https://github.com/zwaetschge/ACGC-Android-Port) |

## Sony

### PlayStation

| Jogo | Projeto/destino | Dados necessários | Fonte |
|---|---|---|---|
| Crash Team Racing (NTSC-U) | [CTR Native](https://github.com/CTR-tools/ctr-native) — PC | Imagem retail em BIN bruto PSX de uma faixa, MODE2/2352. Um ISO convertido para setores de 2048 bytes não preserva os setores XA/STR necessários. Assets extraídos são opcionais para desenvolvimento/modding. | [README: Running](https://github.com/CTR-tools/ctr-native#running) |
| Crash Team Racing (NTSC-U) | [CTR Native Android](https://github.com/Simon358/ctr-native-android) — Android | BIN bruto `ctr-u.bin`; `BIGFILE.BIG` e outros assets extraídos são aceitos como substituição. | [README Android: Assets Setup](https://github.com/Simon358/ctr-native-android/blob/main/README_ANDROID.md#assets-setup-modern-android) |

### PlayStation 4

| Jogo | Projeto/destino | Dados necessários | Fonte |
|---|---|---|---|
| God of War III Remastered (CUSA01623 ou CUSA01715, versões 01.00 ou 01.02) | [gow3_pc](https://github.com/FelipePrado0/gow3_pc) — PC | Dump próprio de PS4 em uma pasta com `eboot.bin`, `sce_module` e `sce_sys`. Não há indicação de ISO. | [README: Download and play](https://github.com/FelipePrado0/gow3_pc#download-and-play) |

## Microsoft

### Xbox

| Jogo | Projeto/destino | Dados necessários | Fonte |
|---|---|---|---|
| Halo: Combat Evolved | [Halo CE Universal](https://github.com/cybersecurity/halo-ce-universal) — PC, Android e Web | Imagem de disco Xbox `.xiso` ou `.iso`; o projeto extrai a pasta `maps/`. | [README: Game data](https://github.com/cybersecurity/halo-ce-universal#game-data) |

### Xbox 360

| Jogo | Projeto/destino | Dados necessários | Fonte |
|---|---|---|---|
| Lost Odyssey (quatro discos; edição asiática multilíngue ou USA/Europa, sem misturar edições) | [Lost Odyssey Recomp](https://github.com/freefrank/LostOdysseyRecomp) — PC, Android | Pasta extraída, `default.xex`, ISO ou dados GOD. O disco 1 é necessário para iniciar. | [README: Start playing](https://github.com/freefrank/LostOdysseyRecomp#start-playing) |
| Sonic Unleashed (USA ou Europa; Japão não é compatível) | [Unleashed Recompiled](https://github.com/hedge-dev/UnleashedRecomp) — PC | Cópia retail ou digital de Xbox 360 e atualização obrigatória. O instalador aceita contêineres/imagens extraídos do Xbox 360 ou a pasta dos arquivos originais; DLC é opcional. A documentação não define uma extensão universal. | [README: How to Install](https://github.com/hedge-dev/UnleashedRecomp#how-to-install) |

## Outros sistemas

Serão adicionados requisitos para outros sistemas quando a documentação do projeto confirmar o tipo de imagem ou arquivo necessário.

## Glossário

- **Imagem de disco**: cópia digital de um disco; pode usar um formato diferente de `.iso`.
- **BIN bruto**: dump setor por setor que pode exigir modo ou tamanho de setor específico; nem sempre equivale a um ISO.
- **ROM**: dump de um cartucho ou outra mídia não óptica.
- **Assets/arquivos extraídos**: arquivos do jogo já extraídos; podem substituir ou complementar uma imagem.
- **Não verificado**: a documentação do projeto ainda não confirmou o requisito; isso não significa que o projeto não precise de dados do jogo.
