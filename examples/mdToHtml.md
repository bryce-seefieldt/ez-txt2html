
ezTxt2Html, a simple open-source Python program that converts plain text (.txt) into HTML files (.html).  It can be used to convert individual files or all files in a directory. It’s easy to install with the following these steps:

1. Ensure you have the latest version of Python 3 installed.

```python --version```

2. If needed, download and install [Python 3](https://www.python.org/downloads/)

3. Clone or download my repository to your local machine:

`git clone https://github.com/bryce-seefieldt/ez-txt2html.git`

4. Change your current working directory to the src directory within the project folder:

`cd ez-txt2html\src`

5. Install the required dependencies by running:

`pip install -r requirements.txt`

That’s it, ez, the program is ready to run.

You can run the program from the command line. It accepts the following command-line arguments:

- '-h' or '--help': Display help screen.
- '-v' or '--version': Display the current version of ezTxtToHtml and exit.
- 'inputPath' (required): Provide the path to the target file or directory containing the files to be converted.
- '-o' or '--output' (optional): Define the output directory for the HTML files. If not specified, it defaults to ./HTML.
Here's how you can run ezTxtToHtml:

To can run ezTxtToHtml use the command `python ezTxtToHtml.py inputPath [-o outputPath]`from the ./src/ directory in repository. Replace 'inputPath':  this with the path to the target file or directory containing text or markdown files. For example:

1. Convert a single text or markdown file to HTML:

`python ezTxtToHtml.py path/to/yourfile.txt`

2. Convert all text or markdown files in a directory to HTML:

`python ezTxtToHtml.py path/to/yourdirectory`

The generated HTML files will be saved to automatically created ./src/HTML/ directory as a default. Use '-o' or '--output' along with your desirec directory path in order to overide the default save location. This folder will be overwritten entirely with each execution of the program. The resulting HTML files will have the same name as the input files but with the .html extension.  The repo includes an examples folder containing  a sample text file which can be run to get an idea of this tool works.  While in the src folder run:
`python ezTxtToHtml.py ../examples/` to see how it convert all text files in a folder, OR 

`python ezTxtToHtml.py ../examples/blogPost.txt` to see how it converts a single specified file.

The converted files will be saved to  the /src/til/ directory, unless otherwise specified.

