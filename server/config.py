"""
for now, this is mostly a placeholder.  We are going to want much
more robust configuration management soon.
at the very least, the config dict avoids having us put state in the
wrong place until we figure out where it should live.
"""


from pathlib import Path
import plistlib
import platform
import collections

class Config(dict):
    def __init__(self):
        system = platform.system()
        self.system = system
        if "Darwin" in system:
            self.init_macos()

    def init_macos(self):
        pass


config = Config()
