# i3altab

## Alt-tab like behaviour for each monitor individually instead of the global default

## i3 config
Put these two lines on your config
```bash
exec_always --no-startup-id /path/to/daemon.py
bindsym $mod+Tab exec --no-startup-id path/to/altab.py
```
