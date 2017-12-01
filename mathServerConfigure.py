'''set the command line path for mathematica
The program is now rewitten in a very general way that should apply to other command line program.
'''
HOST = ""
PORT = [18175]
COMMAND = ["/usr/local/bin/math"]

COMMAND_NAME = ["mathematica 9"]
'''
this is used to see whether the read_from_process
 should stop. For different backend,
 change it to tell the server stop reading the stdout.
'''
VALIDATE_OUTPUT_PATTERN = ["In\[\d*\]:="]
# EXTRACT_RESULTS_FOR_REMOTE = ["=([\s\S]*)In\[\d*\]:="]
# EXTRACT_RESULTS_FOR_LOCAL = ["Out\[\d*\]=([\s\S]*)\nIn\[\d*\]:="]
# EXTRACT_RESULTS_FOR_INFO = ["([\s\S]*)\nIn\["]

RESULT_FILTERS = [("In\[\d*\]:=", ""),
                  ("Out\[\d*\](.*?)=", ""), (" +", " "),
                  ("\n", ""), ("`", "!")]
