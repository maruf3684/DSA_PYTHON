import sys
import sysconfig
from pprint import pprint

config_vars = sysconfig.get_config_vars()
status = config_vars.get("Py_GIL_DISABLED")
pprint(config_vars)

if status == 0:
    print("GIL Active")
elif status == 1:
    print("GIL is off")

