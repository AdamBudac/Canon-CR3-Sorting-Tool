# Canon CR3 Sorting Tool

Slovak guide here: [README-SK.md](README-SK.md)

A simple tool for sorting Canon `.CR3` RAW files – it moves them to a separate folder if there is a corresponding `.JPG` preview file with the same name in the selected directory. This approach is especially useful because some `.CR3` files open very slowly, so it is more time-efficient to first sort your photos using the quickly viewable `.JPG` previews and then use this tool to automatically sort the `.CR3` RAWs for further postprocessing.

## Features

- **Interactive folder selection**: Choose the folder to process using a GUI
- **Automatic sorting**: All `.CR3` files that have a `.JPG` with the same name will be moved to a `process` subfolder
- **Safe processing**: Files are only moved, originals are not changed or deleted
- **Cross-platform**: Works on Windows, macOS, and Linux (requires Python and Tkinter)

## Requirements

- Python 3.13
- Tkinter

## Installation

1. Install [Python](https://www.python.org/) 3.13

## Usage

1. Run the script by double-clicking or in the console:

```bash
python cr3sort.py
```

2. Choose the folder containing your `.CR3` and `.JPG` files

## License

Free
