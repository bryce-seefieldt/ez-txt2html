# Contributing to ez-txt2html

ezTxt2Html is a simple open-source Python program that converts plain text and markdown files (.txt, .md) into HTML files (.html). You can use it to convert individual file or all files in a directory.


## Installation for Developers

To use ez-txt2html, follow these steps:

1. Ensure you have the latest version of Python 3 installed.
`python --version`

2. If needed, download and install [Python 3](https://www.python.org/downloads/)

3. Fork https://github.com/bryce-seefieldt/ez-txt2html.git to your GitHub repo

4. Clone or download your remote repository to your local machine:
`git clone <<your-github-repo>>/ez-txt2html.git`

5. Change your current working directory to ez-txt2html:
`cd ez-txt2html`

6. Install developer dependencies (Black and Flake8):
`python dev-setup.py`

7. Create a working branch for your work:
`git checkout -b "<<branch-name>>"`

Now, you have successfully installed ez-txt2html and are ready to run the program and make changes.
To run the program see *Usage* instructions below.

8. a) Test your code changes as you go:
 `pytest src\test_textToHtmlConverter.py`

    b) Try to add tests to \src\test_textToHtmlConverter.py for any code changes made.

9. When you've completed your changes run the following to implement Black formatter and Flake8 linter:
`python format.py`
Black will automatically implement format changes.
Flake8 will provide a list of changes required for any .py files you have changed.
Make the suggested changes and run format.py again until all messages are cleared.

10. Once all Flake8 linting is complete, you can commit and push your changes to youre remote repository (It is suggested you maintain the branch structure on your remote repo).
`git add <<your/changed/files>>`
`git commit -m "<<detailed commit message>>"`
**Add and commit can be done as many times in the process as you prefer**
`git push origin <<branchname>>`

11. Create a pull-request on the [ez-txt2html upstream repository](https://github.com/bryce-seefieldt/ez-txt2html.git).


## Usage

You can run ez-txt2html from the command line. It accepts the following command-line arguments:

- '-h' or '--help': Display help screen.
- '-v' or '--version': Display the current version of ez-txt2html and exit.
- 'inputPath' (required): Provide the path to the target file or directory containing the files to be converted.
- '-o' or '--output' (optional): Define the output directory for the HTML files. If not specified, it defaults to ./HTML.
- '-c' or '--config' (optional): Provide a custom [TOML](https://toml.io/en/) config file with pre-defined arguments.

Here's how you can run ez-txt2html:

`python src/ez-txt2html.py inputPath [-o outputPath] [-c configPath]`

- 'inputPath': Replace this with the path to the target file or directory containing text or markdown files.
- 'o outputPath' (optional): Replace this with the desired output directory for the HTML files.
- 'c configPath' (optional): Replace this with the path to a .toml config file.

## Input

1. Convert a single text or markdown file to HTML:

`python src\ez_txt2html.py path/to/yourfile.txt`

2. Convert all text or markdown files in a directory to HTML:

`python src\ez_txt2html.py path/to/yourdirectory`

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

`python src\ez_txt2html.py ./examples/` to see how it convert all text files in a folder, OR 

`python src\ez_txt2html.py ./examples/til.md`to see how it converts a single specified file.

The converted HTML files will appear in /til directory unless otherwise specified. 

To specify the output directory add '-o' or '--output' forllowed by the local or relative destination path to the command line:
`python src\ez_txt2html.py ./examples/til.md -o ../newFolder`

To utilize a config file add '-c' or '--output' followed by the path to the .toml file: `python ez_txt2html.py ./examples/ -c ./config.toml`

## License

This program is open-source and released under the [MIT License](https://opensource.org/license/mit). Feel free to use and modify it as needed.

## Author

ez-txt2html is maintained by [Bryce Seefieldt](https://github.com/bryce-seefieldt/).

If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/bryce-seefieldt/ez-txt2html/issues).

