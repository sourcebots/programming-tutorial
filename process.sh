#!/usr/bin/env bash

set -e

rm -rf zip_dir/

echo "> Unzipping Archive..."
unzip -qxK Sourcebots_Programming_Tutorial.zip -d zip_dir

cd zip_dir/

echo "> Cleaning out zip..."
rm -rf env/
rm -rf test/
rm -rf .git/
rm -rf Sourcebots_Programming_Tutorial.zip
rm -rf **/__pycache__


echo "> Moving robot stub into tasks..."
for task in lesson*/**; do
    cp -r robot/ $task
done

echo "> Recompressing..."
zip -rlqX Sourcebots_Programming_Tutorial.zip *

cd ../

echo "> Cleaning up..."
mv zip_dir/Sourcebots_Programming_Tutorial.zip .

rm -rf zip_dir/

echo "> Done!"
