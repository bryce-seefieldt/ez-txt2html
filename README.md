# ez-txt2html

ezTxt2Html is a simple open-source Python program that converts plain text and markdown files (.txt, .md) into HTML files (.html). You can use it to convert individual file or all files in a directory.

## Installation

To use ez-txt2html, Ensure you have the latest version of Python 3 installed.

`python --version`

If needed, download and install [Python 3](https://www.python.org/downloads/)

### Option A) Install and run the program as a Python Package

1. `pip install ez-txt2html-bryce-seefieldt`
2. Run the main module `python -m ez-txt2html.ez_txt2html -h`.
This will describe the command line options for how you can convert your files.
See below for usage details on command line options.

### Option B) Clone or download source code to your local machine 
_(recommended for contributing to this project)_

1. `git clone https://github.com/bryce-seefieldt/ez-txt2html.git`
2. Change your current working directory to the package directory within the project folder: `cd ez-txt2html\ez-txt2html`

Now, you have successfully installed ez-txt2html.

## Usage

You can run ez-txt2html from the command line. It accepts the following command-line arguments:

- '-h' or '--help': Display help screen.
- '-v' or '--version': Display the current version of ez-txt2html and exit.
- 'inputPath' (required): Provide the path to the target file or directory containing the files to be converted.
- '-o' or '--output' (optional): Define the output directory for the HTML files. If not specified, it defaults to ./HTML.
- '-c' or '--config' (optional): Provide a custom [TOML](https://toml.io/en/) config file with pre-defined arguments.

Here's how you can run ez_txt2html:

1) If installed as a package (via pip):
`python -m ez-txt2html.ez_txt2html inputPath [-o outputPath] [-c configPath]`

2) If installed from source codeL
`python ez-txt2html.py inputPath [-o outputPath] [-c configPath]`

- 'inputPath': Replace this with the path to the target file or directory containing text or markdown files.
- 'o outputPath' (optional): Replace this with the desired output directory for the HTML files.
- 'c configPath' (optional): Replace this with the path to a .toml config file.

## Input

1. Convert a single text or markdown file to HTML:

`python ez_txt2html.py path/to/yourfile.txt`

2. Convert all text or markdown files in a directory to HTML:

`python ez_txt2html.py path/to/yourdirectory`

## Output

HTML files will be saved to automatically created ./src/HTML/ directory as a default. Use '-o' or '--output' along with your desirec directory path in order to overide the default save location. This output folder will be overwritten entirely with each execution of the program.
HTML files will have the same name as the input files but with the .html extension.

## Configuration File

Arguments may be pre-defined in a [TOML](https://toml.io/en/) file and passed to the program.

Example TOML configuration (i.e. in a file named `config.toml`):

```toml
output = "./HTML"
```

Note: Using a config file will override other command line switches (if provided).

## Examples 
The included examples folder contains a sample text file which can be run to get an idea of this tool works.  While in the src folder run:

`python ez_txt2html.py ../examples/` to see how it convert all text files in a folder, OR 

`python ez_txt2html.py ../examples/til.md` to see how it converts a single specified file.

The converted HTML files will appear in /src/HTML/ unless otherwise specified. 

To specify the output directory add '-o' or '--output' forllowed by the local or relative destination path to the command line:
`python ez-txt2html.py ../examples/til.md -o ../examples`

To utilize a config file add '-c' or '--output' followed by the path to the .toml file: `python ez_txt2html.py ../examples/ -c ../config.toml`

## Version

The current version of ez-txt2html is 1.0.2

## License

This program is open-source and released under the [MIT License](https://opensource.org/license/mit). Feel free to use and modify it as needed.

## Author

ez-txt2html is maintained by [Bryce Seefieldt](https://github.com/bryce-seefieldt/).

If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/bryce-seefieldt/ez-txt2html/issues).

Enjoy converting your text files to HTML with ez-txt2html!
