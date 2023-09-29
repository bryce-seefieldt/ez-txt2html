#!/usr/bin/python3
import os
import argparse
import re
from shutil import rmtree

VERSION = '0.1'
DEFAULTOUTPUT= './HTML'


def CommandLineParser():
    parser = argparse.ArgumentParser(description='Text to HTML Converter HELP')
    
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {VERSION}',
        help='Display current version and exit')
    
    parser.add_argument('inputPath', help='Provide path to target file or directory')
    
    parser.add_argument('-o','--output',  metavar='<output Path>',
                        help='Define output directory. Defaults to ./HTML')
    
    # Store parsed arguments received from command line
    try:
        commandLineArguments = parser.parse_args()
    except argparse.ArgumentError as e:
        print(f'Error:", {e}')
    except ValueError as e:
        print(f'Error:", {e}')
        
    return commandLineArguments

def deleteOutputDirectory(outputPath):
    if os.path.exists(outputPath):
        rmtree(outputPath)
    os.makedirs(outputPath)


# Validate received command line arguments
def verifyArguments(commandLineArguments):
    inputPath = commandLineArguments.inputPath
    outputPath = commandLineArguments.output or f'{DEFAULTOUTPUT}'
    return inputPath, outputPath

def openCurrentFile(currentFile):
    with open(currentFile, "r") as txt:
        parsedLines = txt.readlines()
    return parsedLines

# Parse markdown to Html
def parseMarkdownToHtml(markdownLines):
    htmlContent = ""
    paragraph = False

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

            htmlContent += line.strip() + "\n"

    if paragraph:
        htmlContent += "</p>\n"

    return htmlContent

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

def writeToHtmlFile(outputPath, content):
    with open(outputPath, "w") as htmlFile:
        htmlFile.write(content)
    print(f'{outputPath} created\n')
    return
    
def textToHtmlConverter(inputPath, outputPath):
    try:
        # Verify if path is a directory or file
        if os.path.exists(inputPath):
            print (f'Path Found')
            if os.path.isdir(inputPath):  
                print (f'Path is directory')
                deleteOutputDirectory(DEFAULTOUTPUT)
                for filename in os.listdir(inputPath):
                    if filename.endswith(('.txt', '.md')):
                        verifiedFile = os.path.join(inputPath, filename)
                        convertedFilename = os.path.splitext(os.path.basename(filename))[0] + '.html'
                        convertedPath = f'{outputPath}/{convertedFilename}'
                        parsedLines = openCurrentFile(verifiedFile) 
                        htmlContent = convertTextContent(parsedLines, verifiedFile)
                        writeToHtmlFile(convertedPath, htmlContent)
                        
            else:
                print (f'Path is file')
                if inputPath.endswith(('.txt', '.md')):
                        deleteOutputDirectory(DEFAULTOUTPUT)
                        print (f'Path is .TXT or .MD file')
                        verifiedFile = inputPath
                        convertedFilename = os.path.splitext(os.path.basename(inputPath))[0] + '.html'
                        convertedPath = f'{outputPath}/{convertedFilename}'
                        parsedLines = openCurrentFile(inputPath)
                        htmlContent = convertTextContent(parsedLines, inputPath)
                        writeToHtmlFile(convertedPath, htmlContent)
                else:
                    print (f'Incorrect file format provided')
            
        else: 
            print (f'No files located in path')
    except ValueError as e:
        print(f'Error:", {e}')
    except Exception as e:
        print(f'Error:", {e}')      
                
    return 
    
if __name__ == '__main__':
    print (f"Python Text to HTML Converter Running")
    commandLineArguments = CommandLineParser()
    inputPath, outputPath = verifyArguments(commandLineArguments)
    textToHtmlConverter(inputPath, outputPath)
    

