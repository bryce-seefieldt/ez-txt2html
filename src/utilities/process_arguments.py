import argparse
from utilities.process_configurations import loadConfig


# Define Argument Parser
def CommandLineParser(versionNumber):
    parser = argparse.ArgumentParser(description="EZ-TXT2HTML CONVERTER HELP")

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {versionNumber}",
        help="Display current version and exit",
    )

    parser.add_argument("inputPath", help="Provide path to target file or directory")

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
