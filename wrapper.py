import os
print('Loading function')

# This will fetch the traveling ruby runtime from cloudfront, unpack it, and run ruby
# as a proof of concept. The runtime should be packaged and uploaded to the lambda function
# to avoid paying for the download and unpacking process upon each lamba execution
# See http://phusion.github.io/traveling-ruby/ for details of traveling ruby

def lambda_handler(event, context):

  cmds = [
    u'curl http://d6r77u77i8pq3.cloudfront.net/releases/traveling-ruby-20150715-2.2.2-linux-x86_64.tar.gz -o /tmp/ruby.tar.gz 2>&1',
    u'tar zxf /tmp/*.gz -C /tmp',
    u'ls /tmp',
    u'PATH=/tmp/bin:$PATH LD_LIBRARY_PATH=/tmp/lib:$LD_LIBRARY_PATH ruby -v 2>&1'
  ]
  for cmd in cmds:
    print os.popen(cmd).read()

  return