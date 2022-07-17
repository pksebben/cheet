# Cheet

Create cheat sheets, for just the things you want to learn.

I got sick of having cheat sheets made by other people.  Not because they were bad in general, but because invariably they had at most five or six things I wanted on them, and about a hundred things I didn't want on them (either because I didn't need them or I had the muscle memory already.)

# Requirements

 - set up a venv
 - `pip install -r requirements.txt`

# Usage / Workflow

 - `python3 app.py` from /server/
 - go to localhost:8765 in your browser
 - create cheets

Cheet will save to `cheets.json` on every update, delete, etc.

# Roadmap

 - emacs integration
   - export cheets from apropos docs
   - import cheets as apropos docs
 - vim integration
   - export docs to cheet
 - dockerize
 - pack into binary
 - server improvements
 - cli reimplementation
   - SSE display updating
 - configuration page
 - sort / reduce (DONE)
