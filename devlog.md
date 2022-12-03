# Cheet dev log

Saturday, July 16, 2022
14:08:10:
Cheet has undergone some pretty drastic changes since the old cli.
There is now a fully functional web app, with only one feature from
the 'old' cheet remaining (that of vim editing; it was too cool not to
use).  That said, I've archived the old version of cheet (parts of it,
at least) in /old_cheet/ for posterity and because I want to
reimplement a cli and compiling / desktop rendering at some point.

# LOG

## Thursday, September 29, 2022

I need sql.  Implementing this is going to be quite a task, so I
should break it up into smaller TODOs.

===============
BOOKMARK: ,./
===============

# TODO

 - [ ] SQL
   - [ ] Connection to sql db
   - [ ] models for sqlalchemy
   - [ ] translation from json => sql db
   - [ ] rework api to use sql
