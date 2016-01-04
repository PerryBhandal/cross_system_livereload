import config

from sniffer.api import * # import the really small API
import os, termstyle
import subprocess

# you can customize the pass/fail colors like this
pass_fg_color = termstyle.green
pass_bg_color = termstyle.bg_default
fail_fg_color = termstyle.red
fail_bg_color = termstyle.bg_default

# All lists in this variable will be under surveillance for changes.
watch_paths = ["."]

watch_exts = [".py", ".scss"]

def is_watched_ext(file_name):
    for ext in watch_exts:
        if file_name.endswith(ext):
            return True

    return False

# this gets invoked on every file that gets changed in the directory. Return
# True to invoke any runnable functions, False otherwise.
#
# This fires runnables only if files ending with .py extension and not prefixed
# with a period.
@file_validator
def src_files(filename):
    return is_watched_ext(filename) and not os.path.basename(filename).startswith('.')

# This gets invoked for verification. This is ideal for running tests of some sort.
# For anything you want to get constantly reloaded, do an import in the function.
#
# sys.argv[0] and any arguments passed via -x prefix will be sent to this function as
# it's arguments. The function should return logically True if the validation passed
# and logicially False if it fails.
#
# This example simply runs nose.
@runnable
def execute_nose(*args):
    curl_call = "curl %s:%d/reload" % (config.RELOAD_IP, config.RELOAD_PORT)
    subprocess.call(curl_call.split(" "))
    return True
