"""
MIRAGE Console
mgargparse.py

Created by Shota Shimazu on 2018/09/06

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the Apache License, see LICENSE for detail.
https://github.com/shotastage/mirageframework/blob/master/LICENSE
"""

import sys
import enum
import functools

from typing import List
from mirageconsole import system
from mirageconsole.core import *


class CommandActionStore(object):

    def __init__(self, cmd: str, subcmd: str, target: str, option: str, flow: callable = None) -> Void:
        # Default action is below.
        # mgc no-action:void test --detail [empty list]
        # ex. mgc new:react proj_name --typescript

        self._command = cmd
        self._subcommand = subcmd
        self._target_name = target
        self._command_option = option
        self._flow = flow

        # Status
        self.is_assessmented = False



class ArgumentsParser(object):

    def __init__(self) -> Void:
        self._action_stack: List[CommandActionStore] = []
        self._arguments: List[str] = []

        self._given_action = CommandActionStore(
            cmd = self._command_parser(sys.argv[1]),
            subcmd = self._subcommand_parser(sys.argv[1]),
            target = sys.argv[2],
            option = sys.argv[3]
        )

    
    def add_argument(self, command: str, subcommand: str, target: str, detail: str, flow) -> Void:
        self._action_stack.append(
            CommandActionStore(
                cmd = command,
                subcmd = subcommand,
                target = target,
                option = detail,
                flow = flow
            )
        )


    def parse(self) -> Void:

        for action in self._action_stack:
            if self._given_action == action:
                action._flow()
                return
        
        print("Your command is not found.")



    def _command_parser(self, cmd: str) -> str:

        if ":" in cmd:
            return cmd.split(":")[0]
        else:
            return cmd

    
    def _subcommand_parser(self, cmd: str) -> str:

        if ":" in cmd:
            return cmd.split(":")[1]
        else:
            return ""

    def _parse_detail_option(self, option: str) -> str:
        return ""
