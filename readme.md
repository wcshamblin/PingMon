# PingMon

PingMon monitor ping time minute by minute and graphs the result.

## Gathering data
To daemonize

```bash
chmod 755 ping.py
nohup ./ping.py &
```
## Graphing
```bash
chmod 755 pplot.py
pplot.py
```