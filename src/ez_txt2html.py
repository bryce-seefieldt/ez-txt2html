#!/usr/bin/python3
import os
import re
from shutil import rmtree
import sys
import tomllib
import argparse

VERSION = "0.1.2"
DEFAULTOUTPUT = "./til"


# Load arguments from a .toml configuration file
def loadConfig(configPath):
    try:
        with open(configPath, "rb") as f:
            config = tomllib.load(f)
    except FileNotFoundError as e:
        raise Exception(
            f"{e}:Configuration file '{configPath}' could not be found."
        )

    return config


# Define Argument Parser
def commandLineParser(versionNumber):
    parser = argparse.ArgumentParser(description="EZ-TXT2HTML CONVERTER HELP")

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {versionNumber}",
        help="Display current version and exit",
    )

    parser.add_argument(
        "inputPath", help="Provide path to target file or directory"
    )

    parser.add_argument(
        "-o",
        "--output",
        metavar="<output Path>",
        help="Define output directory. Defaults to ./til",
    )

    parser.add_argument(
        "-c",
        "--config",
        metavar="<config Path>",
        help="Provide a TOML file with predefined arguments",
    )

    # Store parsed arguments received from command line
    try:
        commandLineArguments = parser.parse_args()
    except argparse.ArgumentError as e:
        print(f'Error:", {e}')
    except ValueError as e:
        print(f'Error:", {e}')

    return commandLineArguments


# Validate received command line arguments
def verifyArguments(commandLineArguments, defaultOutput):
    configPath = commandLineArguments.config
    inputPath = commandLineArguments.inputPath
    if configPath is None:
        outputPath = commandLineArguments.output or f"{defaultOutput}"
    else:
        config = loadConfig(configPath)
        if "output" in config:
            outputPath = config["output"]
    return inputPath, outputPath


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
    print(f"{outputPath} created\n")
    return


# Parse markdown formatting and convert to HTML tags
def parseMarkdownToHtml(markdownLines):
    htmlContent = ""
    paragraph = False
    code3_occurrence = 0
    code1_occurrence = 0

    for line in markdownLines:
        if line.strip() == "":
            if paragraph:
                htmlContent += "</p>\n"
                paragraph = False
        else:
            if not paragraph:
                htmlContent += "<p>"
                paragraph = True

            line = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", line)
            line = re.sub(r"(\*|_)(.*?)\1", r"<em>\2</em>", line)
            line = re.sub(r"^# (.+)$", r"<h1>\1</h1>", line)
            line = re.sub(r"^## (.+)$", r"<h2>\1</h2>", line)
            line = re.sub(r"^---", r"<hr />", line)

            while "```" in line:
                if code3_occurrence % 2 == 0:
                    line = line.replace("```", "<code>", 1)
                else:
                    line = line.replace("```", "</code>", 1)
                code3_occurrence += 1

            while "`" in line:
                if code1_occurrence % 2 == 0:
                    line = line.replace("`", "<code>", 1)
                else:
                    line = line.replace("`", "</code>", 1)
                code1_occurrence += 1

            htmlContent += line.strip() + "\n"

    if paragraph:
        htmlContent += "</p>\n"

    return htmlContent


# Parse text from file and convert to HTML format
def convertTextContent(parsedLines, filename):
    htmlContent = "<html lang='en'>\n<head>\n\t<meta charset='utf-8'>\n"
    pageTitle = os.path.splitext(os.path.basename(filename))[0]
    htmlContent += f"""\n \t<title>{pageTitle}</title>\n\t\
        <meta name='viewport' content='width=device-width, initial-scale=1'>
    \n</head>\n<body>\n"""

    if filename.endswith(".md"):
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
                htmlContent += f"{htmlLine}"

        if paragraph:
            htmlContent += "</p>\n"

    htmlContent += "</body>\n</html>"

    return htmlContent


# Individual file conversion function
def fileConversion(inputPath, outputPath):
    try:
        # verifiedFile = os.path.join(inputPath, filename)
        verifiedFile = inputPath
        filename = inputPath
        convertedFilename = (
            os.path.splitext(os.path.basename(filename))[0] + ".html"
        )
        convertedPath = f"{outputPath}/{convertedFilename}"
        parsedLines = openCurrentFile(verifiedFile)
        htmlContent = convertTextContent(parsedLines, verifiedFile)
        writeToHtmlFile(convertedPath, htmlContent)
    except Exception as e:
        print(f'Error:", {e}')


# Main program function receives arguments from user and runs conversion
# process
def textToHtmlConverter(inputPath, outputPath):
    try:
        # Verify file path exists
        if os.path.exists(inputPath):
            if os.path.isdir(inputPath):
                # Path is a directory or file
                deleteOutputDirectory(outputPath)
                for filename in os.listdir(inputPath):
                    inputFile = inputPath + f"/{filename}"
                    if filename.endswith((".txt", ".md")):
                        fileConversion(inputFile, outputPath)

            else:
                if inputPath.endswith((".txt", ".md")):
                    deleteOutputDirectory(outputPath)
                    filename = os.path.basename(inputPath).split("/")[-1]
                    fileConversion(inputPath, outputPath)
                else:
                    print(
                        "Incorrect file type, please provide .txt or .md\
                        files"
                    )

        else:
            raise ValueError("Invalid path provided")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

    return

def ez_txt2html_Main(version, defaultOutput):
    print("EZ-TXT2HTML Converter Running\n")
    commandLineArguments = commandLineParser(version)
    try:
        inputPath, outputPath = verifyArguments(
            commandLineArguments, defaultOutput
        )
        textToHtmlConverter(inputPath, outputPath)
    except Exception as e:
        print(e)
        sys.exit(1)
    sys.exit()

if __name__ == "__main__":
    try:
        ez_txt2html_Main(VERSION, DEFAULTOUTPUT)
    except Exception as e:
        print(e)
        sys.exit(1)
    sys.exit()
    # print("EZ-TXT2HTML Converter Running\n")
    # commandLineArguments = commandLineParser(VERSION)
    # :
    #     inputPath, outputPath = verifyArguments(
    #         commandLineArguments, DEFAULTOUTPUT
    #     )
    #     textToHtmlConverter(inputPath, outputPath)
    # except Exception as e:
    #     print(e)
    #     sys.exit(1)
    # sys.exit()