# python-orvibo

Control Orvibo devices with Python 2. Currently supports the S20 WiFi Smart Switch.

## Usage

```python
from orvibo.s20 import S20

s20 = S20("x.x.x.x", "mac") # Supply IP and MAC address
print(s20.on) # Current state (True = ON, False = OFF).
s20.on = True # Turn it on.
s20.on = False # Turn it off.
```
