# sed did it again


### So I wRoTe(or better said, adapted a dwmblocks script)....
Ok so I adapted a dwmblocks script. It basically grabs the output from mpc and appends the stripped content to a
given file. In my case, I wanted to log songs from <a href="https://uc.pseudot.xyz/posts/History-of-classical-music/History-of-classical-music.html">a big archive of classical music I'm listening to</a> and
automatically output it in markdown-like format. Or, in other words, add a - before the songname and output it.
Soo, here's my little script.

```
#!/bin/sh

echo -n "- ">> $1
printf " %s"$(mpc | sed "/^volume:/d;s/\\&/&amp;/g;s/^/ /;s/ \\[paused\\].*/⏸/g;/\\[playing\\].*/d" | sed -e 's/-//g') >> $1
echo >>$1

```
I left the ⏸ emoji because I like it. It feels like a personal touch (although I'm not sure if I
added it or just left it there).

I also had to create an alias for calling the script

```
alias mlist="addmus ~/list.md"

```
Et voilà, Это все!
