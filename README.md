# i3altab

Alt-tab like behaviour for each monitor **individually**.

```
python3 -m pip install i3ipc
git clone https://github.com/RaphaelAsla/i3altab && cd i3altab
chmod +x daemon.py altab.py
```

## i3 config
Put these two lines in your config
```bash
exec_always --no-startup-id /path/to/daemon.py
bindsym $mod+Tab exec --no-startup-id /path/to/altab.py
```
