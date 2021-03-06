#!/bin/bash

source ../functions.sh

logEcho "[Korali] Running Composability Test..."

pushd ../../tutorials/advanced/8.composite
check_result
dir=$PWD

logEcho "-------------------------------------"
logEcho " Entering Folder: $dir"

log "[Korali] Removing any old result files..."
rm -rf _korali_results >> $logFile 2>&1
check_result

for file in *.py
do
  if [ ! -f $file ]; then continue; fi

   logEcho "  + Running File: $file"
   ./$file >> $logFile 2>&1
   check_result
done

logEcho "-------------------------------------"

popd

