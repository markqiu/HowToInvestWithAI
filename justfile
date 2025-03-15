set dotenv-load

# list command
default:
    @just --list

# run book
start:
    jupyter book start

# build book
build:
    jupyter book build

