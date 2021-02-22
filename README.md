# RGB ASCII art tools

Taking a shot with Python for the first time and trying to have a bit of fun in the process.

This consists of a small script that plays with ASCII and ANSI escape sequences to add some color to your terminal.

## colorize_ascii

This can be ran by specifying an `input file` or a `text string` to generate an ASCII banner.

It will also take a few other parameters in order to configure the result:
```
usage: colorize_ascii [-h] (-i file | -t text) [-f font] [-c colors] [-s [0-100]] [-w width] [-d delay] [-o file | -a times] [-l line] [-n lines]

Generate and colorize ASCII art

optional arguments:
  -h, --help  show this help message and exit
  -i file     input file
  -t text     text to generate
  -f font     font to use, check them here: http://www.figlet.org/examples.html
  -c colors   comma separated hex colors (default: RGB)
  -s [0-100]  push colors forward n columns in the next line
  -w width    max width of the banner
  -d delay    print each character with a delay (milliseconds, default: 0)
  -o file     output file
  -a times    animate n times
  -l line     line number to show last login information
  -n lines    new lines to append to the end

Have fun! :)
```

So, for example, this:

```
$ colorize_ascii -t "Hello World" -c FF3355,3355FF,FFFF12 -f graffiti -w 40 -s 4
```

Will result in:

<img src="docs/example1.png" width="575" height="220">


If you want a nice welcome message when you open your terminal, just add it to your shell config (i.e. `.zshrc`, `.bash_profile`, etc).

Some like this:

```
colorize_ascii -t "welcome radix" -f drpepper -s 3 -a 1 -d 2 -l 5
```

Will yeld this result:

![Alt Text](docs/example2.gif)


### Dependencies

You'll need `pyfiglet` to run this and you can install it like this:

```
pip3 install pyfiglet
```
