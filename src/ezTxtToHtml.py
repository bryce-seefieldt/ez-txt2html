#!/usr/bin/python3
import os
import argparse
from shutil import rmtree



VERSION = '0.0.1'
DEFAULTOUTPUT= './HTML/'

def CommandLineParser():
    parser = argparse.ArgumentParser(description='Text to HTML Converter HELP')
    
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {VERSION}',
        help='Display current version and exit')
    
    parser.add_argument('inputPath', help='Provide path to target file or directory')
    
    parser.add_argument('-o','--output',  metavar='<outputPath>',
                        help='Define output directory. Defaults to ./HTML')
    
    #Store parsed arguments received from command line
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
    return inputPath

def openCurrentFile(currentFile):
    with open(currentFile, "r") as txt:
        parseLines = txt.readlines()
        print (f'{parseLines}')
    return parseLines

def convertTextContent(parsedLines, filename):
    htmlContent = f"<html lang='en'>\n<head>\n\t<meta charset='utf-8'>\n"
    pageTitle = os.path.splitext(os.path.basename(filename))[0]  
    htmlContent += f"""\n \t<title>{pageTitle}</title>\n\t<meta name='viewport' content='width=device-width, initial-scale=1'>
    \n</head>\n<body>\n"""

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
    
    print(f'{htmlContent}')
    return htmlContent

def writeToHtmlFile(outputPath, content):
    with open(outputPath, "w") as htmlFile:
        htmlFile.write(content)
    print(f'{outputPath} created\n')
    return
    
def textToHtmlConverter(inputPath):
    try:
        
        #Verify if path is a directory or file
        if os.path.exists(inputPath):
            print (f'Path Found')
            if os.path.isdir(inputPath):  
                print (f'Path is directory')
                deleteOutputDirectory(DEFAULTOUTPUT)
                for filename in os.listdir(inputPath):
                    if filename.endswith('.txt'):
                        verifiedFile = os.path.join(inputPath, filename)
                        convertedFilename = os.path.splitext(os.path.basename(filename))[0] + '.html'
                        convertedPath = f'{DEFAULTOUTPUT}{convertedFilename}'
                        parsedLines = openCurrentFile(verifiedFile) 
                        htmlContent = convertTextContent(parsedLines, verifiedFile)
                        writeToHtmlFile(convertedPath, htmlContent)
                        
            else:
                print (f'Path is file')
                if inputPath.endswith('.txt'):
                        deleteOutputDirectory(DEFAULTOUTPUT)
                        print (f'Path is .TXT file')
                        verifiedFile = inputPath
                        convertedFilename = os.path.splitext(os.path.basename(inputPath))[0] + '.html'
                        convertedPath = f'HERE'
                        convertedPath = f'{DEFAULTOUTPUT}{convertedFilename}'
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
    inputPath = verifyArguments(commandLineArguments)
    textToHtmlConverter(inputPath)
    

