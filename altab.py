#!/usr/bin/python

import i3ipc
import json

def main():
    i3 = i3ipc.Connection()

    with open('/tmp/last_focus.json', 'r') as f:
        last_focused_by_monitor = json.load(f)
        current_focused_monitor = [w for w in i3.get_workspaces() if w.focused][0].output

        if current_focused_monitor in last_focused_by_monitor:
            last_workspace_id = last_focused_by_monitor[current_focused_monitor]
            i3.command(f"workspace {last_workspace_id}")

if __name__ == '__main__':
    main()
