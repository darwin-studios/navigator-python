"""Navigator SDK. Darwin imports remain supported by the underlying SDK."""
from typing import TYPE_CHECKING
import darwin_sdk as _sdk
from darwin_sdk import Darwin as Navigator, AsyncDarwin as AsyncNavigator

if TYPE_CHECKING:
    from darwin_sdk import *

__all__ = [*getattr(_sdk, "__all__", []), "Navigator", "AsyncNavigator"]

def __getattr__(name: str):
    return getattr(_sdk, name)

def __dir__():
    return sorted(set(__all__))
