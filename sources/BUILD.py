import argparse
import os
import subprocess
from fontTools.ttLib import TTFont


# FONTMAKE
try:
    print("\n**** Running Fontmake")
    print("     [+] Run: fontmake -g sources/Orbitron.glyphs -o variable")
    subprocess.call("fontmake -g sources/Orbitron.glyphs -o variable > /dev/null 2>&1", shell=True)
    print("     [+] Done")
except:
    print("     [!] Error! Try installing Fontmake: https://github.com/googlei18n/fontmake")


# MOVE FONTS
print("\n**** Moving fonts to fonts directory")
subprocess.call("cp variable_ttf/Orbitron-VF.ttf fonts/", shell=True)
print("     [+] Done")


# CLEANUP
print("\n**** Removing build directories")
print("     [+] Run: rm -rf variable_ttf master_ufo")
subprocess.call("rm -rf variable_ttf master_ufo", shell=True)
print("     [+] Done")


# AUTOHINT
print("\n**** Run: ttfautohint")
os.chdir('fonts')
cwd = os.getcwd()
print("     [+] In Directory:", cwd)
subprocess.call("ttfautohint -I Orbitron-VF.ttf Orbitron-VF-Fix.ttf", shell=True)
subprocess.call("cp Orbitron-VF-Fix.ttf Orbitron-VF.ttf", shell=True)
subprocess.call("rm -rf Orbitron-VF-Fix.ttf", shell=True)
print("     [+] Done")


# GFTOOLS
print("\n**** Run: gftools")
os.chdir("..")
cwd = os.getcwd()
print("     [+] In Directory:", cwd)
#subprocess.call("gftools fix-dsgi fonts/Foo-VF.ttf --autofix", shell=True)


# FONTTOOLS
print("\n**** Run: edit xAvgCharWidth")
cwd = os.getcwd()
print("     [+] In Directory:", cwd)
font = TTFont('fonts/Orbitron-VF.ttf')
print("     [+] font =", font)
print("     [+] Done")

# DRAWBOT
print("\n**** Run: DrawBot")
subprocess.call("python3 docs/drawbot-sources/basic-specimen.py > /dev/null 2>&1", shell=True)
print("     [+] Done")

