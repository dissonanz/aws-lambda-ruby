import os
print('Loading function')


def lambda_handler(event, context):
  cmd = u'LD_LIBRARY_PATH=./bin:$LD_LIBRARY_PATH ./bin/ruby -v 2>&1'
  message = os.popen(cmd).read()
  print message
  return