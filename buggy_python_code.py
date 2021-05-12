"""Somehow malicious code."""
# contains bunch of buggy examples
# taken from:
# https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
import cPickle
import subprocess
import base64
import subprocess
import flask


# Input injection
def transcode_file(filename):
    """Transfers code file."""
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)  # a bad idea!


# Assert statements
def assert_function(user):
    """Asserts function."""
    assert user.is_admin, 'user does not have access'
    # secure code...


# Pickles
class RunBinSh(object):
    """Runs bin sh."""
    def __reduce__(self):
        """Reduces."""
        return (subprocess.Popen, (('/bin/sh',),))

    def random_num(self):
        """Randomizes."""
        return 42


@app.route('/')
def index():
    """Indexes."""
    module = flask.request.args.get("module")
    exec("import urllib%s as urllib" % module)  # Noncompliant


print(base64.b64encode(cPickle.dumps(RunBinSh())))
