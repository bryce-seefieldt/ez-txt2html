# ez-txt2html

ezTxt2Html is a simple open-source Python program that converts plain text and markdown files (.txt, .md) into HTML files (.html). You can use it to convert individual file or all files in a directory.

## Installation

To use ezTxtToHtml, follow these steps:

1. Ensure you have the latest version of Python 3 installed.

`python --version`

2. If needed, download and install [Python 3](https://www.python.org/downloads/)

3. Clone or download this repository to your local machine:

`git clone https://github.com/bryce-seefieldt/ez-txt2html.git`

4. Change your current working directory to the src directory within the project folder:

`cd ez-txt2html\src`

5. Install the required dependencies by running:

`pip install -r requirements.txt`

Now, you have successfully installed ezTxtToHtml.

## Usage

You can run ezTxtToHtml from the command line. It accepts the following command-line arguments:

- '-h' or '--help': Display help screen.
- '-v' or '--version': Display the current version of ezTxtToHtml and exit.
- 'inputPath' (required): Provide the path to the target file or directory containing the files to be converted.
- '-o' or '--output' (optional): Define the output directory for the HTML files. If not specified, it defaults to ./HTML.
Here's how you can run ezTxtToHtml:

`python ezTxtToHtml.py inputPath [-o outputPath]`

- 'inputPath': Replace this with the path to the target file or directory containing text or markdown files.
- 'o outputPath' (optional): Replace this with the desired output directory for the HTML files.

## Input

1. Convert a single text or markdown file to HTML:

`python ezTxtToHtml.py path/to/yourfile.txt`

2. Convert all text or markdown files in a directory to HTML:

`python ezTxtToHtml.py path/to/yourdirectory`

## Output

HTML files will be saved to automatically created ./src/HTML/ directory as a default. Use '-o' or '--output' along with your desirec directory path in order to overide the default save location. This output folder will be overwritten entirely with each execution of the program.
HTML files will have the same name as the input files but with the .html extension.

## Examples 
The included examples folder contains a sample text file which can be run to get an idea of this tool works.  While in the src folder run:

`python ezTxtToHtml.py ../examples/` to see how it convert all text files in a folder, OR 

`python ezTxtToHtml.py ../examples/blogPost.txt` to see how it converts a single specified file.

The converted HTML files will appear in /src/HTML/ unless otherwise specified. 

To specify the output directory add '-o' or '--output' forllowed by the local or relative destination path to the command line:
`python ezTxtToHtml.py ../examples/blogPost.txt -o ../examples`

## Version

The current version of ezTxtToHtml is 0.1.

## License

This program is open-source and released under the [MIT License](https://opensource.org/license/mit). Feel free to use and modify it as needed.

## Author

ezTxtToHtml is maintained by [Bryce Seefieldt](https://github.com/bryce-seefieldt/).

If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/bryce-seefieldt/ez-txt2html/issues).

Enjoy converting your text files to HTML with ezTxtToHtml!
