#! /bin/bash


for d in */ ; do
    # echo "$d"
    cd "$d"
    rm -rf *.tif
    cp *.jpg ../
    cd ..
done

