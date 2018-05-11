#!/usr/bin/env python3

import fire
from cmd_interface import CommandlineInterface


def main():
    fire.Fire(CommandlineInterface)


if __name__ == '__main__':
    main()
