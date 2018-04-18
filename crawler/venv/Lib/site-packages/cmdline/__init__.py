from __future__ import absolute_import

# setup logging as close to launching the command as possible
from .logconfig import setup_logging

from .command import BaseCommand
from .settings import SettingsParser

settings = SettingsParser.settings

__all__ = ['SettingsParser', 'settings', 'setup_logging']
