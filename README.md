# Linux CPU Temp Monitor

[![license](https://img.shields.io/badge/license-MIT-green.svg?style=flat&cacheSeconds=2592000)](https://github.com/SorkOs09/LinuxCpuTempMonitor/blob/main/LICENSE)

One day my laptop's fan was broken and I had to use an external fan. To keep my laptop from overheating I needed a program to track the temperature in real time. Solutions what I found in internet everything was not good enough for me (somewhere it was not possible to see the entire history of the temperature for the day, somewhere it was not possible to save the data to a log file, etc.). 
So I decided to make my own program.

## Required Additional Programms, Modules And Libraries

[stress](https://linux.die.net/man/1/stress/)
[termcolor](https://pypi.org/project/termcolor/)


## Features

(Features list is available by <code>cpu_temp_monitor.py -help</code>)


Color visualization of the temperature graph and display of the CPU cores frequency.

<code>-mhz</code>

<img src="https://raw.githubusercontent.com/SorkOs09/LinuxCpuTempMonitor/main/demos/mhz.png" width="800">



Stretching by console size

<img src="https://raw.githubusercontent.com/SorkOs09/LinuxCpuTempMonitor/main/demos/stretching.gif" width="800">



CPU stress test

<code>-stress</code>

<img src="https://raw.githubusercontent.com/SorkOs09/LinuxCpuTempMonitor/main/demos/stress.gif" width="800">



Save logs to file

<code>-save_log</code>

<img src="https://raw.githubusercontent.com/SorkOs09/LinuxCpuTempMonitor/main/demos/log_file.gif" width="800">





## Author
[SorkOs09](https://github.com/SorkOs09)

## License
[MIT](https://github.com/SorkOs09/LinuxCpuTempMonitor/blob/main/LICENSE)
