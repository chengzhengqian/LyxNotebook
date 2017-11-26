LyxNotebook is a lightweight tool to enable lyx users to execute mathematica and python code within lyx. The tool is written in python3 and tested in Ubuntu 16.04.

There are two ways to use LyxNotebook.

1) Use Lyx default CAS (computer algebra system) interface.

The default CAS interface convert a latex formula into mathematica code and use `math` to execute it. Then extract the result back to lyx. The drawback is that it just works for simple formulas, as if the user trys to use advance function like solve equations etc, lyx will automaically ignore equal sign. Also, each calculation is independent so a sequenctial calculation is not possible. To overcome these problems, we use a server to hold a mathematica process and pipe the code to its stdin. Then we use a new script named as `math` to let lyx envoke. The script will get the mathematica code passed from Lyx and parse some of the special keywords to standard mathematica code, i.e, we could circumvent the Lyx layer to write arbrary mathematica code. Then the script send the command to math server and retrieve the result. As the math server keeps running in background, so all previous assignments are available.

First, start a math server: (edit ./mathServerConfigure.py to specify the math path and server port and host)

python3 ./mathServer.py

This starts a repl for mathematca and hold a thread to listen external requests.

Then, we put ./math to the environmental path so that Lyx will find it first then the standard math command. (This is kind of black magic and to avoid inconvinience, one could start Lyx with a specify $PATH env variable)

Note, edit the path of ./math according to your location.

Now, start lyx, type some formula, and use CAS to run. You could see the corresponding command in mathServer's output.

2) The second way is more robust which use the standard lyx pipe (you should enable it first) to communicate.

First, append the keyboard binding in user.bind to ~/.lyx/bind/user.bind
Notice the key binding name is important as LyxNotebook will use it to identify which language you are using. You could change this by edit dispatchCmd.py

Then start the server you want,

python3 ./mathServer.py

python3 ./pythonServer.py

./sageServer

(notice you edit the path of sage to make script works)


Now, start a server to listen to lyx.pipe.out (edit according to your path)

python3 ./readPipe.py

Everything is set and in lyx, insert a Program List, type some code, use the corresponding shortcut, then you could see the output (you should print them in your code) in minibuffer and they are automaticall copied to clipboard.



