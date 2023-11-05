import tomllib


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
