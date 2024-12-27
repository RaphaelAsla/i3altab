#!/usr/bin/python

import i3ipc
import json

FOCUS_FILE = "/tmp/last_focus.json"
last_focused_by_monitor = {}
last_monitor = ""

def save_focus_data():
    with open(FOCUS_FILE, 'w') as f:
        json.dump(last_focused_by_monitor, f)

def on_workspace_focus(i3, e):
    global last_monitor
    old_workspace = e.old
    monitor = [w for w in i3.get_workspaces() if w.focused][0].output
    if old_workspace and old_workspace.name and last_monitor == monitor:
        update_focus(old_workspace.name, monitor)
    last_monitor = monitor

def update_focus(last_workspace, monitor):
    last_focused_by_monitor[monitor] = last_workspace
    save_focus_data()

def main():
    i3 = i3ipc.Connection()
    i3.on("workspace::focus", on_workspace_focus)
    i3.main()

if __name__ == "__main__":
    main()
