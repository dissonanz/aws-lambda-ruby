#!/bin/bash

echo -e "Creating lambda.zip\n"
mkdir out
zip out/lambda.zip bin/* *.rb *.py
if [ $? -eq 0 ];
  then
  echo -e "\nZip created. Upload lambda.zip to AWS Lambda as a python function in the normal way."
else
  echo "Failed to create zip file."
  exit 1
fi