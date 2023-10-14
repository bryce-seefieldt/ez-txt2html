#!/usr/bin/python3
import os
import re
from shutil import rmtree

import sys
from utilities.process_arguments import CommandLineParser, verifyArguments

VERSION = '0.1.1'
DEFAULTOUTPUT= './til'

# Delete output directory if it currently exists
def deleteOutputDirectory(outputPath):
    if os.path.exists(outputPath):
        rmtree(outputPath)
    os.makedirs(outputPath)
    return

# Open and read the current file being converted
def openCurrentFile(currentFile):
    with open(currentFile, "r") as txt:
        parsedLines = txt.readlines()
    return parsedLines

# Write converted HTML content to file 
def writeToHtmlFile(outputPath, content):
    with open(outputPath, "w") as htmlFile:
        htmlFile.write(content)
    print(f'{outputPath} created\n')
    return

# Parse markdown formatting and convert to HTML tags
def parseMarkdownToHtml(markdownLines):
    htmlContent = ""
    paragraph = False
    codeFenceOpen = False

    for line in markdownLines:
        if line.strip() == "":
            if paragraph:
                htmlContent += "</p>\n"
                paragraph = False
        else:
            if not paragraph:
                htmlContent += "<p>"
                paragraph = True

            line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
            line = re.sub(r'(\*|_)(.*?)\1', r'<em>\2</em>', line)
            line = re.sub(r'^# (.+)$', r'<h1>\1</h1>', line)
            line = re.sub(r'^## (.+)$', r'<h2>\1</h2>', line)
            line = re.sub(r'^---', r'<hr />', line)

            
            if re.search(r'\`\`\`', line):
                
                if codeFenceOpen is True:
                    line = re.sub(r'\`\`\`', r'</code>', line)
                    codeFenceOpen = False
                else:
                    line = re.sub(r'\`\`\`', r'<code>', line)
                    codeFenceOpen = True

            line = re.sub(r'\`(.*?)\`', r'<code>\1</code>', line)

            htmlContent += line.strip() + "\n"

    if paragraph:
        htmlContent += "</p>\n"

    return htmlContent

# Parse text from file and convert to HTML format
def convertTextContent(parsedLines, filename):
    htmlContent = f"<html lang='en'>\n<head>\n\t<meta charset='utf-8'>\n"
    pageTitle = os.path.splitext(os.path.basename(filename))[0]  
    htmlContent += f"""\n \t<title>{pageTitle}</title>\n\t<meta name='viewport' content='width=device-width, initial-scale=1'>
    \n</head>\n<body>\n"""

    if filename.endswith('.md'):
        htmlContent += parseMarkdownToHtml(parsedLines)
    else:
        paragraph = False
        for line in parsedLines:
            htmlLine = line
            if not paragraph:
                htmlContent += "<p>"
                paragraph = True

            if line == "\n":
                htmlContent += "</p>\n"
                paragraph = False

            else:
                htmlLine = line.replace("\n", " ")
                htmlContent += f'{htmlLine}'

        if paragraph:
            htmlContent += "</p>\n"

    htmlContent += f"</body>\n</html>"
    htmlContent += f"</html>"

    return htmlContent

# Individual file conversion function
def fileConversion(inputPath, outputPath, filename):
    try:
        verifiedFile = os.path.join(inputPath, filename)
        convertedFilename = os.path.splitext(os.path.basename(filename))[0] + '.html'
        convertedPath = f'{outputPath}/{convertedFilename}'
        parsedLines = openCurrentFile(verifiedFile) 
        htmlContent = convertTextContent(parsedLines, verifiedFile)
        writeToHtmlFile(convertedPath, htmlContent)
    except Exception as e:
        print(f'Error:", {e}') 

# Main program function receives arguments from user and runs conversion process
def textToHtmlConverter(inputPath, outputPath):
    try:
        # Verify file path exists
        if os.path.exists(inputPath):
            
            # Verify if path is a directory or file 
            if os.path.isdir(inputPath):  
                deleteOutputDirectory(outputPath)
                for filename in os.listdir(inputPath):
                    if filename.endswith(('.txt', '.md')):
                        fileConversion(inputPath, outputPath, filename)
   
            else:
                if inputPath.endswith(('.txt', '.md')):
                        deleteOutputDirectory(outputPath)
                        fileConversion(inputPath, outputPath, filename)
                else:
                    print (f'Incorrect file type, please provide .txt or .md files')
            
        else: 
            print (f'Invalid path provided')

    except ValueError as e:
        print(f'Error:", {e}')
    except Exception as e:
        print(f'Error:", {e}')      
                
    return 
    
if __name__ == '__main__':
    print (f"EZ-TXT2HTML Converter Running")
    commandLineArguments = CommandLineParser(VERSION)
    try:
        inputPath, outputPath = verifyArguments(commandLineArguments, DEFAULTOUTPUT)
        textToHtmlConverter(inputPath, outputPath)
    except Exception as e:
        print(e)
        sys.exit(1)
    sys.exit()
