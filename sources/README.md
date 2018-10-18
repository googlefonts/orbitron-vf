# Source Notes

The font file `Orbitron/fonts/Orbitron.ttf` is built from source using the following command from the root directory:

```
py sources/BUILD.py && gftools fix-dsig fonts/Orbitron.ttf --autofix
```

Dependencies installed should include:

 - [fontmake](https://github.com/googlei18n/fontmake)
 - [gftools](https://github.com/googlefonts/gftools)
 - [ttfautohint](https://www.freetype.org/ttfautohint/)

