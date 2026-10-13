"""Hard network block for runs that must not touch the network (the deterministic baseline).

Patches socket connect/DNS so any attempted connection raises, and sets Hugging Face offline
flags so cached local models load without update checks. Used as a context manager; the
run's meta.json records that the guard was active.
"""

from __future__ import annotations

import os
import socket
from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any


class NetworkBlocked(RuntimeError):
    pass


def _blocked(*args: Any, **kwargs: Any) -> Any:
    raise NetworkBlocked(f"network access attempted during a no-network run: {args[:2]!r}")


@contextmanager
def no_network() -> Iterator[None]:
    saved_env = {k: os.environ.get(k) for k in ("HF_HUB_OFFLINE", "TRANSFORMERS_OFFLINE")}
    saved = (
        socket.socket.connect,
        socket.socket.connect_ex,
        socket.create_connection,
        socket.getaddrinfo,
    )
    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    socket.socket.connect = _blocked  # type: ignore[method-assign]
    socket.socket.connect_ex = _blocked  # type: ignore[method-assign]
    socket.create_connection = _blocked
    socket.getaddrinfo = _blocked
    try:
        yield
    finally:
        (
            socket.socket.connect,  # type: ignore[method-assign]
            socket.socket.connect_ex,  # type: ignore[method-assign]
            socket.create_connection,
            socket.getaddrinfo,
        ) = saved
        for k, v in saved_env.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
