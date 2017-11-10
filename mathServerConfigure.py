
HOST = ""
PORT = [18165, 18257]
COMMAND = ["/usr/local/bin/math"]

COMMAND_NAME = ["mathematica 9"]
VALIDATE_OUTPUT_PATTERN = ["In\[\d*\]:="]
EXTRACT_RESULTS_FOR_REMOTE = ["=([\s\S]*)In\[\d*\]:="]
EXTRACT_RESULTS_FOR_LOCAL = ["Out\[\d*\]=([\s\S]*)\nIn\[\d*\]:="]
EXTRACT_RESULTS_FOR_INFO = [ "([\s\S]*)\nIn\["]
