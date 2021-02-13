# RGB ASCII art tools

Taking a shot with Python for the first time and trying to have a bit of fun in the process.

This consists of a couple of small scripts that play with ASCII and ANSI escape sequences to add some color to your terminal.

## colorize_ascii

This can be ran by specifying an `input file` or a `text string` to generate an ASCII banner.

It will also take a few other parameters in order to configure the result:
```
  -i file     input file
  -t text     text to generate
  -f font     font to use, check them here: http://www.figlet.org/examples.html
  -c colors   comma separated hex colors (for example: FF0000,00FF00,0000FF)
  -s spin     number of columns which colors will rotate on next line
  -o file     output file
  -w width    max width of the banner
```

So, for example, this:

```
$ colorize_ascii -t "Hello World" -c FF3355,3355FF,FFFF12 -f graffiti -w 40 -s 4
```

Will result in:

<img src="docs/example1.png" width="575" height="220">

## welcome_message

This one prints a colorful welcome message with a bit of lag (retro style) when you open your terminal.

It also accepts a few config parameters:
```
  -u user     override system username
  -m message  custom message (default will be "welcome user")
  -l          hide last login
  -f font     font to use, check them here: http://www.figlet.org/examples.html
  -c colors   comma separated hex colors (for example: FF0000,00FF00,0000FF)
  -s spin     number of columns which colors will rotate on next line
  -a times    animate n times
  -w width    max width of the banner
```

Just add it to your shell config (i.e. `.zshrc`, `.bash_profile`, etc).

Some like this:

```
welcome_message -u radix -f drpepper -s 3 -a 1
```

Will yeld this result:

![Alt Text](docs/example2.gif)


### Dependencies

You'll need `pyfiglet` to run this and you can install it like this:

```
pip3 install pyfiglet
```
