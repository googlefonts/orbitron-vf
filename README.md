
![Orbitron](https://github.com/theleagueof/orbitron/raw/master/images/orbitron-1.jpeg)

# Orbitron

_by [Matt McInerney](http://pixelspread.com)_

Orbitron is a geometric sans-serif typeface intended for display purposes. It features four weights (light, medium, bold, and black), stylistic alternatives, small caps, and a ton of alternate glyphs. 

Orbitron was designed so that graphic designers in the future will have some alternative to typefaces like Eurostile or Bank Gothic. If you’ve ever seen a futuristic sci-fi movie, you have may noticed that all other fonts have been lost or destroyed in the apocalypse that led humans to flee earth. Only those very few geometric typefaces have survived to be used on spaceship exteriors, space station signage, monopolistic corporate branding, uniforms featuring aerodynamic shoulder pads, etc. Of course Orbitron could also be used on the posters for the movies portraying this inevitable future.

## Variable Font Specimen 
<!-- Updated image from variable mastering fork -->
![Orbitron](https://github.com/eliheuer/orbitron/raw/vf-mastering/docs/images/animated-specimen.gif)

## Building From Source
Note: A few dependencies are required for this to work, please see the source documentation [here](https://github.com/eliheuer/orbitron-vf/tree/master/sources).

To build the fonts; clone this repo, then navigate to its root directory in a terminal and run:
```
python3 sources/BUILD.py --ttfautohint "-v -W --increase-x-height=0 --stem-width-mode=sss" --static
```
This will build new fonts in the `fonts` directory and apply autohinting.

Additional options are available by adding flags to the build script, for example, if you wanted to update the DrawBot specimen, prepare the font for a PR to Google Fonts and test with FontBakery, we could run:
```
python3 sources/BUILD.py --googlefonts ~/Google/fonts/ofl/orbitron --fontbakery --drawbot --ttfautohint "-v -W --increase-x-height=0 --stem-width-mode=sss" --static
```
For more help, run:
```
python3 sources/BUILD.py --help
```

## License
Orbitron is licensed under the SIL Open Font License v1.1 (<http://scripts.sil.org/OFL>). 
To view the copyright and specific terms and conditions please refer to [OFL.txt](https://github.com/theleagueof/orbitron/blob/master/OFL.txt)

## Downloading Font Files (TTF)
Find binary releases on <https://github.com/theleagueof/orbitron/releases>

## Installation Instructions
- [GNU+Linux](https://wiki.archlinux.org/index.php/fonts#Manual_installation)
- [MacOS](https://support.apple.com/en-us/HT201749)
- [Windows](https://support.microsoft.com/en-us/help/314960/how-to-install-or-remove-a-font-in-windows)

## Getting Involved
Would you like to contribute to the development of this font? Here is how **you** can help:

1. Tell us about any bugs you find, or enhancements you would like to see on the issue tracker: [https://github.com/theleagueof/orbitron/issues](https://github.com/theleagueof/orbitron/issues)

2. Contribute directly to the fonts. This repository contains a complete set of source files and build documentation. Make changes and submit a pull request. Make changes and submit a pull request.
