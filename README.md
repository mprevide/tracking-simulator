# tracking-simulator
It simulates a device randomly moving from a starting point with sinr decreasing as
it distances itself from the origin.

The simulator sends data to dojot through MQTT with the following JSON payload:

```json
{"sinr": "<value>",
 "gps": "<latitude-value>,<longitude-value>"}
```

# Usage

```
$ python3 -m trackingsim.main -h
Usage: main.py [options]

Options:
  -h, --help            show this help message and exit
  -H HOST, --host=HOST  Host to connect. Defaults to localhost.
  -P PORT, --port=PORT  Port to connect to. Defaults to 1883.
  -s SERVICE, --service=SERVICE
                        Service identifier in dojot. Defaults to admin.
  -d DEVICES, --device=DEVICES
                        Device identifier in dojot. Multiple devices can be
                        simulated simultaneously repeating this option.
  -x LATITUDE, --latitude=LATITUDE
                        Starting latitude for the simulation. Defaults to
                        -22.815970.
  -y LONGITUDE, --longitude=LONGITUDE
                        Starting longitude for the simulation. Defaults to
                        -47.045121.
```