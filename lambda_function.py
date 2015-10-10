import os
print('Loading function')


def lambda_handler(event, context):
  cmd = u'LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH ./ruby -v 2>&1'
  message = os.popen(cmd).read()
  print message
  return