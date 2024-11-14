from __future__ import annotations
from typing import Optional
import time
import logging
from typing import Any

logger = logging.getLogger(__name__)

class Profile:
    def __init__(self, name: str) -> None:
        self.name = name
        self._cur: Optional[float] = None
        self.ts: list[float] = []
        self.t0 = time.time()

    def start(self) -> None:
        self._cur = time.time()

    def stop(self) -> None:
        if self._cur is None:
            return
        t = time.time()
        self.ts += [t - self._cur]
        self._cur = None

        if t - self.t0 > 1.:
            self.t0 = t
            if len(self.ts) > 0:
                avg = 1000. * sum(self.ts) / len(self.ts)
                ma = 1000. * max(self.ts)
                mi = 1000. * min(self.ts)
                self.ts = []
                logger.debug("TIMER[%-50s]: %7.2fms -- avg %7.2fms -- %7.2fms" % (self.name, mi, avg, ma))


class Profiler:
    def __init__(self) -> None:
        self._profiles: dict[str, Profile] = {}

    def get(self, name: str) -> Profile:
        if name not in self._profiles:
            self._profiles[name] = Profile(name)
        return self._profiles[name]

profiler = Profiler()

def timed(func):  # type: ignore
    profile = profiler.get(str(func))
    def wrapped(*args, **kwargs):  # type: ignore
        profile.start()
        res = func(*args, **kwargs)
        profile.stop()
        return res
    return wrapped

def errorlogged(func):  # type: ignore
    def wrapped(*args, **kwargs):  # type: ignore
        try:
            return func(*args, **kwargs)
        except Exception:
            logger.exception("errorlogged")
    return wrapped

def parse_color(color: Any) -> Any:
    try:
        if isinstance(color, str):
            r = color[1:3]
            g = color[3:5]
            b = color[5:7]
            if len(color) >= 9:
                a = color[7:9]
            else:
                a = "FF"
            return (int(r, 16)/255., int(g, 16)/255., int(b, 16)/255., int(a, 16)/255.)
        elif len(color) in [3, 4]:
            rf = float(color[0])
            gf = float(color[1])
            bf = float(color[2])
            if len(color) > 3:
                af = float(color[3])
            else:
                af = float(color[3])
            return (min(rf, 1.), min(gf, 1.), min(bf, 1.), min(af, 1.))
        else:
            raise Exception("Unknown")
    except Exception:
        logger.warn("Could not parse color '%s'" % color)
        return (1., 1., 1., 1.)

def parse_gradient(gradient: Any) -> Any:
    return (*parse_color(gradient[0]), *parse_color(gradient[1]), gradient[2])

def get_color(color: Any, gradient: Any) -> tuple[float, float, float, float, float, float, float, float, float]:
    if gradient == ('', '', 0):
        # color
        fake_gradient = parse_color(color)
        return (*fake_gradient, *fake_gradient, 0.)
    else:
        return parse_gradient(gradient)


