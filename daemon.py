#!/usr/bin/python

import i3ipc
import json

last_focused_by_monitor = {}
last_monitor = ""

def on_workspace_focus(i3, e):
    global last_monitor
    last_workspace = e.old.name
    output = [w for w in i3.get_workspaces() if w.focused][0].output
    if last_monitor == output:
        update_focus(last_workspace, output)
    last_monitor = output

def update_focus(last_workspace, output):
    last_focused_by_monitor[output] = last_workspace

    with open("/tmp/last_focus.json", 'w') as f:
        json.dump(last_focused_by_monitor, f)

def main():
    i3 = i3ipc.Connection()

    i3.on("workspace::focus", on_workspace_focus) 

    i3.main()

if __name__ == "__main__":
    main()
