cronjobs:

Front End: crontab
- List: crontab -l
- Remove: crontab -r
- Insert/Edit: crontab -e

Back-end:
- TODO

cronjobs are executed in an special environment without access to the display by default.

## Example

Run /home/dbremont/Documents/mind-moment.sh, every minute, with display activiated.

```bash
* * * * * . $HOME/.profile; export DISPLAY=:0 &&  /usr/bin/bash /home/dbremont/Documents/mind-moment.sh
```

## Debug

```bash
grep CRON /var/log/syslog    
````


##  References

- https://askubuntu.com/questions/56683/where-is-the-cron-crontab-log
- https://unix.stackexchange.com/questions/348113/how-do-i-run-a-cronjob-on-a-display
