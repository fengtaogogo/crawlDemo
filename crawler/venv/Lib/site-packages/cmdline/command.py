import argparse
import sys

from .exceptions import CommandError


class BaseCommand(object):
    def __init__(self, parser=None, args=None, sys_argv=None):
        self.parser = parser or argparse.ArgumentParser()
        self.subparsers = None

        # only set sys_argv to the system argv when it's None
        # otherwise use the kwarg, even if it's an empty list
        self.sys_argv = sys_argv
        if self.sys_argv is None:
            self.sys_argv = sys.argv[1:]

        # already parsed arguments, i.e. do not call self.parser.parse_args()
        self.args = args

        self.setup_parser()

    def parse_args(self):
        if self.args:
            raise CommandError('args are already parsed')

        self.args = self.parser.parse_args(self.sys_argv)

        return self.args

    def run(self):
        if not self.args:
            self.parse_args()

    def setup_parser(self):
        pass

