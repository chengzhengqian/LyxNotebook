import mathServer


mapping_list = [(" ", ""), ("<-", "="), ("`", " "), ("leftleftarrows", ":="), ("leftarrow", "="), ("rightrightarrows", ":>"), ("rightarrow", "->"), ("equiv", "=="), ("Slv", "Solve"), ("/@", "/MAP/"), ("@@", "/APPLY/"), ("@#", "/BLANKSEQ/"), ("@$", "/BLANKSEQZERO/"), ("@", "_"), ("/MAP/", "/@"), ("/APPLY/", "@@"), ("/BLANKSEQ/", "__"), ("/BLANKSEQZERO/", "___"), ("FF", "FullForm"), ("TF", "TreeForm"), ("MF", "MatrixForm"), ("Expt", "Export"), ("FS", "FullSimplify"), ("Func[", "Function["), ("//T", "//TeXForm")
                ]

'''
this is to fool lyx to recogize as if they are output from real mathematica
'''
template = '''%s Wrapper by cheng zhengqian , configured from ''' + __file__ + '''
, change mapping_list variable to add more rules
In[1]:= %s
Out[1]//TeXForm= %s

In[2]:=
------------------------------------
'''

HISTORY_FILES = ["/home/chengzhengqian/Application_local/math_client_mathematica9.m",
                 "/home/chengzhengqian/Application_local/math_client_mathematica11.m"]

MATH_TYPE = 0
MATH_NAME = ["Mathematica 9", "Mathematica 11"]
HOST = ["127.0.0.1", "192.168.1.100"]
PORT = [mathServer.PORT[0], mathServer.PORT[0]]

CONFIGURATION_FILE = "/home/chengzhengqian/Application_local/math_client_configue"
