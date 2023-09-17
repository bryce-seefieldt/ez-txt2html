# ez-txt2html
ezTxt2Html is a simple open-source Python program that converts plain text files (.txt) into HTML files (.html). You can use it to convert individual text files or all text files in a directory.

## Installation
To use ezTxtToHtml, follow these steps:

1. Clone or download this repository to your local machine:
`git clone https://github.com/bryce-seefieldt/ez-txt2html.git`

2. Change your current working directory to the project folder:
`cd ez-txt2html`

3. Install the required dependencies by running:
`pip install -r requirements.txt`

Now, you have successfully installed ezTxtToHtml.

## Usage
You can run ezTxtToHtml from the command line. It accepts the following command-line arguments:

- '-h' or '--help': Display help screen.
- '-v' or '--version': Display the current version of ezTxtToHtml and exit.
- 'inputPath' (required): Provide the path to the target file or directory containing the text files to be converted.

Here's how you can run ezTxtToHtml:
`python ezTxtToHtml.py inputPath`

- 'inputPath': Replace this with the path to the target text file or directory containing text files.

## Input
1. Convert a single text file to HTML:
`python ezTxtToHtml.py path/to/yourfile.txt`

2. Convert all text files in a directory to HTML:
`python ezTxtToHtml.py path/to/yourdirectory`


## Output
HTML files will be created in a new ./HTML directory within the program folder.
HTML files will have the same name as the input text files but with the .html extension.

## Version
The current version of ezTxtToHtml is 0.0.1.

## License
This program is open-source and released under the [MIT License] (https://opensource.org/license/mit). Feel free to use and modify it as needed.

## Author
ezTxtToHtml is maintained by [Bryce Seefieldt] (https://github.com/bryce-seefieldt/).

If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/bryce-seefieldt/ezTxtToHtml/issues).

Enjoy converting your text files to HTML with ezTxtToHtml!
