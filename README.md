## Short logger configuration

### Configuration
* `debug.conf` - plik konfiguracyjny do __logger'a__
> Można (warto) zmienić ścieżke do pliku końcowego: `debug.conf` ->  *args*
> `/var/log/<name>` wymaga uprawnień root'a (sudo python3 <filename>)
>
> Nazwa pliku końcowego: `piGrad.log`
* `debug.py` - inicjalizacja __logger'a__

### Usage
* W pliku w którym należy użyć __logger'a__

```python
from debug import log
```

* Możliwe użycie 
  * `log.<level>('<Message>')`
  * `log.<level>('<Message> %s', argument)`


```python
log.warning('Message %s', arguments)
OR
log.warning('Message')

log.info('Message %s', arguments)
OR
log.info('Message')

log.error('Message %s', arguments)
OR
log.error('Message')
```

* Obecna configuracja produkuje podobne linijki:

|Date       | Time         | Log level | PID  | Thread ID | FileName      | FuncName | Message  |
|-----------|--------------|-----------|------|-----------|---------------|----------|----------|
|2020-03-04 | 19:42:04,789 | ERROR     | 5473 | Thread-2  | testLogger.py | logInfo: | I'm there|
|2020-03-04|19:42:04,791|INFO|5473|Thread-1|testLogger.py|logInfo:|I'm there|
|2020-03-04|19:42:04,791|WARNING|5473|Thread-2|testLogger.py|logInfo:|I'm there|

For more information:
[Logger configruation](https://docs.python.org/3/library/logging.html)

### WARNING
```
├── realizeScheduledPh.py
├── debug.conf -> piGrad/debug.conf (link to a subfolder debug.conf)
├── piGrad
│   ├── debug.py
│   ├── debug.conf
│   └── schedulePh.py <- file in which logger should be used
│── piGrad.log
└── README.md

ln -s piGrad/debug.conf debug.conf - creating link in a main folder

./realizeScheduledPh.py <parameters> - logger should produce the output file in
```
