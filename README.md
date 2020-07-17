# All Capist
Mathieu Reguer


## Installation

The following external package are required: `fonttools`, `click`. 
The required packages will be intalled automatically with the following instalation process:

Just press `enter` in the terminal after each of the commands below to launch them.

1. Copy the whole `AllCapist` folder to a chosen location on your computer, (the top level folder, the one that contains `setup.py`) 

2. Then run the following command in the terminal
    ``` bash
    pip install path/to/AllCapist/Top/Folder
    ```
3. Done! If everything worked, you should be abble to run the following command in the terminal:
    ``` bash
    AllCapist --help
    ```

4. To update the tool, just copy the updated package to your computer, and run the following command (`-U` is for update):
    ``` bash
    pip install -U path/to/AllCapist/top/Folder
    ```
    
Once the tools are intalled, their name can be autocompleted in the Terminal window by pressing the `tab` key.

- Typing `AllC` then `tab` file automatically complete to `AllCapist`

## Usage

### AllCapist

AllCapist is a command to double unicode uppercase with lowercase unicodes for all caps font. 
The target font should have no lowercase glyph (the toolw will not subset them out of the font)

``` bash
AllCapist path/to/my/font.otf
```

It works on both font files and folder. If you feed it a path to a folder instead of a font file, it will run for every otf in that folder

``` bash
AllCapist path/to/my/folder
```

The fonts are saved in place unless an output directory is specified (see below)

##### output option

The `-o` (or `--output_dir`) option can be used to specify a name for the output directory.

``` bash
AllCapist path/to/my/folder -o myOutputFolder
```






