from ..tools.config import Config


def get_wsl_path(config: Config, path: str):
    if not config.get_bool("USE_WSL", False):
        return path

    path_parts = path.split(":\\")
    return f"/mnt/{path_parts[0].lower()}/" + path_parts[1].replace('\\', '/')


def make_wsl_command(config: Config, command: list):
    if not config.get_bool("USE_WSL", False):
        return command

    dist = config["WSL_DISTRO"]
    return ["wsl", "-d", dist, *command]


def get_local_wsl_temp_dir(config: Config):
    if not config.get_bool("USE_WSL", False):
        return "/tmp/"

    return f"\\\\wsl.localhost\\{config['WSL_DISTRO']}\\tmp\\"
