# ----------------------------------------
# imports
# ----------------------------------------

from fontTools.ttLib import TTFont
import click

import os
import time
import glob


# ----------------------------------------
# constants
# ----------------------------------------

TARGETS = [".otf", ".woff", ".woff2", ".ttf"]
IGNORE_UNICODES = [304]  # idotaccent

# ----------------------------------------
# helpers
# ----------------------------------------


def get_lowercase_unicode(uni):
    import unicodedata
    s = (chr(uni))
    lc = s.lower()
    if s != lc:
        return ord(lc)


def walk_input_path(input_path, target_extentions=[".otf"], recursive=False):
    fonts = []
    if os.path.isdir(input_path):
        input_dir = input_path
        if recursive:
            inputs = [root for root, dir, files in os.walk(input_path)]
        else:
            inputs = [input_path]
        for p in inputs:
            for ext in target_extentions:
                fonts.extend(
                    glob.glob(os.path.join(p, "*%s" % (ext))))
    elif input_path.endswith(tuple(target_extentions)):
        input_dir = os.path.dirname(input_path)
        fonts = [input_path]
    assert len(
        fonts) > 0, "The input path does not contain any fonts (%s)" % target_extentions
    return(input_dir, fonts)


# ----------------------------------------


@click.command()
@click.option('-o', '--output_dir', default=None, help='Specify a path for the output directory', type=click.Path(exists=False))
@click.option('--subfolder/--no_subfolder', default=False, help='process subfolders recursively')
@click.argument("input_path", type=click.Path(exists=False))
def double_encode_uc(input_path, output_dir, subfolder):
    t = time.time()
    print("AllCapist")
    font_count = 0

    # walk the i,put directory
    input_dir, font_path = walk_input_path(input_path,
                                           target_extentions=TARGETS,
                                           recursive=subfolder)

    for p in font_path:

        if output_dir:
            dir_, font_file = os.path.split(p)
            out_path = os.path.join(output_dir, font_file)
        else:
            out_path = p

        f = TTFont(p)
        f_cmap = f.get("cmap")

        for table in f_cmap.tables:
            # if table.format in [4, 12, 13, 14]:
            cmap = {}
            for u, n in list(table.cmap.items()):
                cmap[u] = n
                if u not in IGNORE_UNICODES:
                    lc = get_lowercase_unicode(u)
                    if lc and lc != u and lc not in list(table.cmap.keys()):
                        cmap[lc] = n
            table.cmap = cmap

        f.save(out_path)
        f.close()
        print(f"{p} -> done")
        font_count += 1

    print("")
    print(f"All done: {font_count} font processed in {time.time() - t} secs")
