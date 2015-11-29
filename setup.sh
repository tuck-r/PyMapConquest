#!/bin/bash
cd src
cwd=$(pwd)
cd ..
export PYTHONPATH=$PYTHONPATH:$cwd
