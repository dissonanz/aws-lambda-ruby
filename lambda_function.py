from subprocess import Popen, PIPE, STDOUT
print('Loading function')

def lambda_handler(event, context):
  cmd = u'LD_LIBRARY_PATH=./bin:$LD_LIBRARY_PATH ./bin/ruby ./src/action.rb'
  p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
  output = p.stdout.read()
  print output
  return