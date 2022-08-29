#!bin/zsh

# TODO save custom pre-commit hook before it gets overridden
brew install ktlint
ktlint installGitPreCommitHook
