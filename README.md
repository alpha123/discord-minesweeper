# Discord minesweeper

This script generates minesweeper games that use Discord's spoiler tags and emoji.

Sample output:
```
||       ||||       ||||       ||||       ||||       ||||       ||||       ||||:one:||||:one:||
||       ||||       ||||       ||||       ||||       ||||:one:||||:one:||||:two:||||:bomb:||
||       ||||       ||||:one:||||:one:||||:one:||||:one:||||:bomb:||||:two:||||:one:||
||       ||||       ||||:one:||||:bomb:||||:one:||||:one:||||:one:||||:one:||||       ||
||:one:||||:one:||||:one:||||:one:||||:one:||||       ||||       ||||       ||||       ||
||:bomb:||||:one:||||       ||||:one:||||:one:||||:one:||||       ||||       ||||       ||
||:one:||||:one:||||       ||||:one:||||:bomb:||||:one:||||       ||||       ||||       ||
||       ||||       ||||       ||||:one:||||:one:||||:one:||||       ||||       ||||       ||
||       ||||       ||||       ||||       ||||       ||||       ||||       ||||       ||||       ||
```

Produces (oops):

![sample minesweeper board](https://raw.githubusercontent.com/alpha123/discord-minesweeper/master/sample.png)

**Usage**

`python discord_minesweeper.py nrows ncols nbombs [blank]`

[blank] is an optional argument indicating the representation to use
for blank squares. By default it is seven spaces, which aligns
properly in the default font. If your server has a custom blank emoji
like [this one](https://cdn.discordapp.com/emojis/392542407796850699.png?v=1),
use that instead, because it will align properly for people with
non-default fonts.

# License

This script is under the CC0 license (public domain). You're free to do whatever you want with it, copy it straight into your bot, I don't care.