import argparse
import glob
import os
import subprocess
import time
from fontTools.ttLib import TTFont


# Initialize flag parser
parser = argparse.ArgumentParser()
parser.add_argument(
    "--drawbot", help="Render a specimen with DrawBot", action="store_true"
)
parser.add_argument(
    "--googlefonts", help="Copy output to Google Fonts", action="store_true"
)
parser.add_argument(
    "--fontbakery", help="Test fonts with fontbakery", action="store_true"
)
parser.add_argument(
    "--gfdir", help = "Store GoogleFonts directory name"
)
args = parser.parse_args()


# Initialize empty lists
sources = []
sources_styles = []


def intro():
    """
    Gives basic script info.
    """
    print("#    # #####                    #####    ################")
    time.sleep(0.1)
    print("#    # #                        #   #    #   ##         #")
    time.sleep(0.1)
    print(" #  #  ####                      #   #  #   # #   #######")
    time.sleep(0.1)
    print(" #  #  #     <---------------->  #    ##    # #      #")
    time.sleep(0.1)
    print("  ##   #                          #        #  #   ####")
    time.sleep(0.1)
    print("  ##   #                          ##########  #####")
    time.sleep(0.1)
    print("\n**** Starting build script:", time.ctime())
    time.sleep(0.1)

def display_args():
    """
    Gives info about the args.
    """
    print("\n**** Settings:")
    print("     [+] Drawbot specimen rendering (--drawbot)\t\t", args.drawbot)
    print("     [+] Output to Google Fonts (--googlefonts)\t\t", args.googlefonts)
    print("     [+] Test output with fontbakery (--fontbakery)\t", args.fontbakery)
    print("     [+] User set GoogleFonts directory:\t\t", args.gfdir)
    time.sleep(1)


def check_root_dir():
    """
    Checks to make sure script is run from a git repo root directory.
    """
    print(
        "\n**** Checking to make sure the build script is working in the font repo root directory:"
    )
    REPO_ROOT = [".gitignore", ".git"]
    repo_test = os.listdir(path=".")
    repo_test_result = all(elem in repo_test for elem in REPO_ROOT)
    if repo_test_result:
        print("     [+] OK: Looks good")
    else:
        print(
            "     [!] ERROR: Please run this script from the root directory of a git repo."
        )
    time.sleep(1)


def get_source_list():
    """
    Gets a list of source files.
    """
    print("\n**** Making a list of Glyphsapp source files:")
    os.chdir("sources")
    for name in glob.glob("*.glyphs"):
        sources.append(os.path.splitext(name)[0])
    os.chdir("..")
    print("     [+] SOURCES: List of sources =", sources)
    time.sleep(1)


def get_style_list():
    """
    Gets a list of styles from the source list.
    """
    print("\n**** Starting FAFR (Fully Automated Font Repository) build process:")
    for source in sources:
        time.sleep(0.5)
        print("     [+] SOURCES: Preparing to build", source)
        print("     [+] SOURCES: Style =", source.rpartition("-")[2])
        sources_style = str(source.rpartition("-")[2])
        sources_styles.append(sources_style)
    print("     [+] SOURCES: Styles =", sources_styles)
    time.sleep(1)


def run_fontmake():
    """
    Builds ttf fonts files with font make.
    """
    for source in sources:
        print("\n**** Building %s font files with Fontmake:" % source)
        print(
            "     [+] Run: fontmake -g sources/%s.glyphs -o variable --output-path fonts/%s-VF.ttf"
            % (source, source)
        )
        subprocess.call(
            "fontmake -g sources/%s.glyphs -o variable --output-path fonts/%s-VF.ttf > /dev/null 2>&1"
            % (source, source),
            shell=True,
        )
        print("     [!] Done")


def rm_build_dirs():
    """
    Cleanup build dirs
    """
    print("\n**** Removing build directories")
    print("     [+] Run: rm -rf variable_ttf master_ufo instance_ufo")
    subprocess.call("rm -rf variable_ttf master_ufo instance_ufo", shell=True)
    print("     [+] Done")
    time.sleep(1)


def ttfautohint():
    """
    Runs ttfautohint with various flags set. For more info run: ttfautohint --help
    """
    print("\n**** Run: ttfautohint")
    os.chdir("fonts")
    cwd = os.getcwd()
    print("     [+] In Directory:", cwd)
    for source in sources:
        subprocess.call(
            "ttfautohint \
                         -I \
                         -W \
                         --increase-x-height=0 \
                         --stem-width-mode=sss \
                         --default-script=latn \
                         %s-VF.ttf %s-VF-Fix.ttf"
            % (source, source),
            shell=True,
        )
        subprocess.call("cp %s-VF-Fix.ttf %s-VF.ttf" % (source, source), shell=True)
        subprocess.call("rm -rf %s-VF-Fix.ttf" % source, shell=True)
        os.chdir("..")
        cwd = os.getcwd()
        print("     [+] In Directory:", cwd)
        print("     [+] Done:", source)
    print("     [+] Done")
    time.sleep(1)


def fix_dsig():
    """
    Fixes DSIG table
    """
    print("\n**** Run: gftools")
    for source in sources:
        subprocess.call(
            "gftools fix-dsig fonts/%s-VF.ttf --autofix > /dev/null 2>&1" % source,
            shell=True,
        )
        print("     [+] Done:", source)
    print("     [+] Done")
    time.sleep(1)


def google_fonts():
    """
    Copy font output to the Google Fonts repo.
    """
    print("\n****  Copying font output to the Google Fonts repo.")
    for source in sources:
        subprocess.call(
            "cp fonts/%s-VF.ttf ~/Google/fonts/ofl/%s/" % (source, args.gfdir),
            shell=True,
        )
        print("     [+] Done:", source)
    print("     [+] Done")
    time.sleep(1)


def render_specimens():
    """
    Render specimens
    """
    print("\n**** Run: DrawBot")
    subprocess.call(
        "python3 docs/drawbot-sources/basic-specimen.py > /dev/null 2>&1", shell=True
    )
    print("     [+] Done")
    time.sleep(1)


if __name__ == "__main__":
    intro()
    display_args()
    check_root_dir()
    get_source_list()
    get_style_list()
    run_fontmake()
    rm_build_dirs()
    ttfautohint()
    fix_dsig()
    if args.drawbot == True:
        render_specimens()
    else:
        pass
    if args.googlefonts == True:
        google_fonts()
    else:
        pass
    quit()
