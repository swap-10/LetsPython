If you quit from the Python interpreter and enter it again,<br>
the definitions you have made (functions and variables) are<br>
lost. Therefore, if you want to write a somewhat longer program,<br>
you are better off using a text editor to prepare the input for<br>
the interpreter and running it with that file as input instead.<br>
This is known as creating a script. As your program gets longer,<br>
you may want to split it into several files for easier maintenance.<br>
You may also want to use a handy function that you’ve written in<br>
several programs without copying its definition into each program.<br>
<br>
<br>
To support this, Python has a way to put definitions in a file and<br>
use them in a script or in an interactive instance of the interpreter.<br>
Such a file is called a module; definitions from a module can be<br>
imported into other modules or into the main module (the collection<br>
of variables that you have access to in a script executed at the top<br>
level and in calculator mode).<br>
<br>
<br>
A module is a file containing Python definitions and statements.<br>
The file name is the module name with the suffix .py appended.<br>
Within a module, the module’s name (as a string) is available as<br>
the value of the global variable <code>__name__.</code> <br>
<br>
<br>
A module can contain executable statements as well as function<br>
definitions. These statements are intended to initialize the<br>
module. They are executed only the first time the module name is<br>
encountered in an import statement. [1] (They are also run if the<br>
file is executed as a script.)<br>
<br>
<br>
A module can contain executable statements as well as function<br>
definitions. These statements are intended to initialize the module.<br>
They are executed only the first time the module name is<br>
encountered in an import statement. (They are also run if the<br>
file is executed as a script.)<br>
<br>
<br>
<h2>Executing Modules as scripts</h2>
When you run a Python module with
<blockquote><code>
python fibo.py arguments
</code></blockquote>

the code in the module will be executed, just as if you imported it,<br>
but with the __name__ set to "__main__". That means that by adding<br>
this code at the end of your module:<br>

<blockquote><code>
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
</code></blockquote>

you can make the file usable as a script as well as an importable<br>
module, because the code that parses the command line only runs<br>
if the module is executed as the “main” file<br>
<br>
<br>
<h2>The Module Search Path</h2>
When a module named spam is imported, the interpreter first<br>
searches for a built-in module with that name. If not found, it<br>
then searches for a file named spam.py in a list of directories<br>
given by the variable sys.path. sys.path is initialized from<br>
these locations:
<ul>
<li>The directory containing the input script (or the current<br>
directory when no file is specified).
</li>
<li>PYTHONPATH (a list of directory names, with the same syntax<br>
as the shell variable PATH).
</li>
<li>The installation-dependent default.
</li>
</ul>
The directory containing the script being run is placed at the<br>
beginning of the search path, ahead of the standard library<br>
path. This means that scripts in that directory will be loaded<br>
instead of modules of the same name in the library directory.
<br>
<br>
<h2>Packages</h2>
A package is like a collection of modules, but with some<br>
configurations to be better organized and accessible.<br>
This means that scripts in that directory will be loaded instead<br>
of modules of the same name in the library directory.<br>
<blockquote>
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
</blockquote>
<br>
<br>
Users of the package can import individual modules from the package,<br>
for example:<br>
<code>
import sound.effects.echo
</code>
<br>
This loads the submodule sound.effects.echo. It must be referenced<br>
with its full name.<br>
<code>
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
</code>
<br>
An alternative way of importing the submodule is:<br>
<code>
from sound.effects import echo
</code>
<br>
This also loads the submodule echo, and makes it available<br>
without its package prefix, so it can be used as follows:<br>
<code>
echo.echofilter(input, output, delay=0.7, atten=4)
</code>
<br>
Yet another variation is to import the desired function or<br>
variable directly:<br>
<code>
from sound.effects.echo import echofilter
</code>
<br>
Again, this loads the submodule echo, but this makes its<br>
function echofilter() directly available:<br>
<code>
echofilter(input, output, delay=0.7, atten=4)
</code>
<br>
Note that when using <code>from package import item</code>,<br>
the item can be either a submodule (or subpackage) of the<br>
package, or some other name defined in the package, like a<br>
function, class or variable.<br>
<br>
Contrarily, when using syntax like 
<code>import item.subitem.subsubitem</code>, each item except<br>
for the last must be a package; the last item can be a module<br>
or a package but can’t be a class or function or variable defined<br>
in the previous item.<br>