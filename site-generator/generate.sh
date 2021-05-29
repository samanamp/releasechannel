#!/bin/sh
python3 main.py
rm -rf ../site/src/applications
cp -r applications ../site/src/applications
cd ../site
vuepress build src
