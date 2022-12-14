# dotnet pre-commit hook linter

This script installs a linter for dotnet as a pre-commit hook for git. It uses Node and husky to install and maintain the git hook and its dependencies. The .NET tool dotnet-format is used as linter.

Amke sure to add a .editorconfig file with all the code formatting rules to the root of your dotnet repo so that the linter uses the correct rules to format your code.

## Pre-requisites

The tool uses node, the dotnet CLI and the dotnet-format tool. Please make sure to install these tools before executing the install script.

## Usage
```zsh
<path to the install script>/install-hook.py
```

After the hook is successfully installed you need to commit the .husky directory, the package.json and the package-lock.json files.
All your colleagues need to do to install it on their machine after you've commited and pushed these files is to pull those changes and execute `npm install`.

If you already have a pre-commit hook set up you don't need to worry about it. The install script takes care of it and so that it is always called after the linting hook succeeded.
