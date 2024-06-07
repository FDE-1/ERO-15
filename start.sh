#!/bin/bash

check_and_install_package() {
    PACKAGE=$1
    if python -c "import $PACKAGE" &> /dev/null; then
        echo "$PACKAGE is already installed."
    else
        echo "$PACKAGE is not installed. Installing..."
        pip install $PACKAGE
    fi
}

check_and_install_package osmnx
check_and_install_package networkx

python3 src/main.py
