#!/bin/bash

echo -e "Creating lambda.zip\n"
zip lambda.zip ruby libruby.so.2.0 *.rb *.py
if [ $? -eq 0 ];
  then
  echo -e "\nZip created. Upload lambda.zip to AWS Lambda as a python function in the normal way."
else
  echo "Failed to create zip file."
  exit 1
fi