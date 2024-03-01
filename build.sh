#!/bin/bash

rm -rf build dist
rm main.spec

pyinstaller --onefile ./src/main.py
