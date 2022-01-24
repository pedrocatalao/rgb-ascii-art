# RGB ASCII art tools

Taking a shot with Python for the first time and trying to have a bit of fun in the process.

It consists of a small script that plays with ASCII and ANSI escape sequences to add some color to your terminal.

## colorize_ascii

You can call it by specifying either an `input file` or a `text string` to generate an ASCII banner. It's also possible to call it only with `-l` to show the last login information.

There's a few options available in order to configure the result:
```
  -h, --help   show this help message and exit
  -i file      input file
  -t text      text to generate
  -o file      output file (will not print result in terminal)
  -f font      font to use, check them here: http://www.figlet.org/examples.html
  -c colors    comma separated hex colors (default: RGB)
  -w width     maximum width of the banner
  -s columns   push colors forward n columns in the next line
  -a times     animate n times (requires delay)
  -d delay     print each character with a delay (milliseconds, default: 0)
  -l position  vertical position to show last login information
  -n lines     add or remove lines at the end (negative to remove)
```

For example, this:

```
$ colorize_ascii -t "Hello World" -c FF3355,3355FF,FFFF12 -f graffiti -w 40 -s 4
```

Will result in:

<img src="docs/example1.png" width="575" height="220">


If you want a nice welcome message when you open your terminal, just add it to your shell config (i.e. `.zshrc`, `.bash_profile`, etc).

Some like this:

```
$ colorize_ascii -t "welcome radix" -f drpepper -s 3 -a 1 -d 2 -l 4
```

Will yeld this result:

![Alt Text](docs/example2.gif)


### Dependencies

You'll need `pyfiglet` to run this and you can install it like this:

```
pip3 install pyfiglet
```
