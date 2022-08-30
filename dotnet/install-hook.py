#!/usr/bin/python3
import json
import pathlib
import subprocess


def install_or_update_node():
    __check_exit_code(subprocess.run("sudo npm cache clean -f", shell=True))
    __check_exit_code(subprocess.run("sudo npm install -g n", shell=True))
    __check_exit_code(subprocess.run("sudo n stable", shell=True))


def init_pre_commit_hook_files():
    __check_exit_code(subprocess.run("npm init --yes", shell=True))
    __check_exit_code(subprocess.run("npx husky-init && npm install", shell=True))
    __check_exit_code(subprocess.run("npm install lint-staged --save-dev", shell=True))


def add_lint_filter():
    package_json_file = pathlib.Path("package.json")
    with open("package.json", "r+") as raw_json_file:
        package_content = json.load(raw_json_file)
        package_content["lint-staged"] = {"*.cs": "dotnet format --include"}
    package_json_file.write_text(json.dumps(package_content, indent=4))


def install_pre_commit_hook():
    custom_pre_commit_hook = ".git/hooks/pre-commit"
    pre_commit_hook = ""
    if pathlib.Path(custom_pre_commit_hook).exists():
        pre_commit_hook = f" && {custom_pre_commit_hook}"
    pre_commit_hook_file = pathlib.Path(".husky/pre-commit")
    content = pre_commit_hook_file.read_text()
    content = content.replace(f"npm test", f"npx lint-staged --relative{pre_commit_hook}")
    pre_commit_hook_file.write_text(content)


def __check_exit_code(exit_code: subprocess.CompletedProcess):
    if exit_code.returncode != 0:
        exit(exit_code)


if __name__ == '__main__':
    install_or_update_node()
    init_pre_commit_hook_files()
    add_lint_filter()
    install_pre_commit_hook()
