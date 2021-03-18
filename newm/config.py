import pathlib
import importlib
import logging
import sys
import os

_provider = None
_consumer = {}

logger = logging.getLogger(__name__)


class _ConfiguredValue:
    def __init__(self, value, default):
        self._value = None
        self._default = default

        self.update(value)

    def update(self, value):
        self._value = value if value is not None else self._default

    def __call__(self):
        return self._value

def _update_config(at_c, at_p):
    if isinstance(at_c, _ConfiguredValue):
        at_c.update(at_p)
    else:
        if isinstance(at_c, dict):
            for k in at_c.keys():
                _update_config(at_c[k], at_p[k] if at_p is not None and k in at_p else None)

def load_config():
    global _provider

    path = pathlib.Path(os.environ['HOME']) / '.config' / 'newm' / 'config.py'

    if not path.is_file():
        path = pathlib.Path('/etc') / 'newm' / 'config.py'

    if not path.is_file():
        path = pathlib.Path(__file__).parent.absolute() / 'default_config.py'

    if not path.is_file():
        raise Exception("Unexpected")

    logger.info("Loading config at %s", path)

    module = path.stem

    try:
        del sys.modules[module]
    except KeyError:
        pass

    sys.path.insert(0, str(path.parent))
    try:
        _provider = importlib.import_module(module).__dict__
    except:
        logger.exception("Could not load config")
        _provider = {}

    _update_config(_consumer, _provider)


def configured_value(path, default=None):
    global _consumer

    if _provider is None:
        load_config()

    result = None
    try:
        v = _provider
        for k in path.split("."):
            v = v[k]

        result = v
    except KeyError:
        pass

    c = _consumer
    for k in path.split(".")[:-1]:
        try:
            c = c[k]
        except KeyError:
            c[k] = {}

    k = path.split(".")[-1]
    if k in c and isinstance(c[k], _ConfiguredValue):
        return c[k]

    result = _ConfiguredValue(result, default)
    c[k] = result
    return result



if __name__ == '__main__':
    scale = configured_value('output_scale', 1.0)
    pywm = configured_value('pywm', {})
    while True:
        print("Scale is %f" % scale())
        print("PyWM is %s" % pywm())
        input("Update? ")
        load_config()