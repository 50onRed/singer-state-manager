# singer-stage-manager

Tool to update a Singer.io (https://www.singer.io/) pipeline's state ASAP after a target flushes.

Singer docs specify things should work like this (pseudocode):

    tap --state state.json | target >> state-log.txt
    tail -1 state-log.txt > state.json

This works, but this does not "persist" the tap's progress until the entire run completes. For an initial sync of a slow
tap, this could be days. This risks losing a lot of progress unnecessarily.

This program fixes this like so:

    tap --state state.json | target | singer-state-manager --state state.json

As soon as a target "persists" some data relevant to a state message, it emits it again. This tool immediately persists
this state to save progress. Internally this tool uses atomic file operations and a temporary file to assure the state
file is never invalid.

