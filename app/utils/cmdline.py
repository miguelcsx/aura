# aura/app/utils/cmdline.py

import subprocess


def run_cli_command(command: str, *args) -> str:
    """
    Run a command line command with the given arguments
    """
    command_args = [command, *args]
    with subprocess.Popen(command_args, stdout=subprocess.PIPE) as process:
        output, _ = process.communicate()
    return output.decode("utf-8")


def run_npx_command(command: str, *args) -> str:
    """
    Run an npx command with the given arguments
    """
    command_args = ["npx", command, *args]
    with subprocess.Popen(command_args, stdout=subprocess.PIPE) as process:
        output, _ = process.communicate()
    return output.decode("utf-8")
