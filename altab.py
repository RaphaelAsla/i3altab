#!/usr/bin/python

import i3ipc
import json
import os

FOCUS_FILE = "/tmp/last_focus.json"

def load_focus_data():
    if not os.path.exists(FOCUS_FILE):
        return {}

    with open(FOCUS_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def get_focused_monitor(i3):
    workspaces = i3.get_workspaces()
    focused_workspace = next((w for w in workspaces if w.focused), None)
    return focused_workspace.output if focused_workspace else None

def switch_to_last_workspace(i3, focused_monitor, last_focus_by_monitor):
    last_workspace_id = last_focus_by_monitor.get(focused_monitor)
    if last_workspace_id:
        existing_workspaces = [w.name for w in i3.get_workspaces()]
        if last_workspace_id in existing_workspaces:
            i3.command(f"workspace {last_workspace_id}")

def main():
    i3 = i3ipc.Connection()
    last_focus_by_monitor = load_focus_data()
    focused_monitor = get_focused_monitor(i3)
    switch_to_last_workspace(i3, focused_monitor, last_focus_by_monitor)

if __name__ == '__main__':
    main()
