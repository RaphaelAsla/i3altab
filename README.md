# i3altab

Alt-tab like behaviour for each monitor **individually**.

## i3 config
Put these two lines in your config
```bash
exec_always --no-startup-id /path/to/daemon.py
bindsym $mod+Tab exec --no-startup-id /path/to/altab.py
```
