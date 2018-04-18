import datetime

from argparse import ArgumentTypeError


def date(input):
    try:
        return datetime.datetime.strptime(input, "%Y-%m-%d").date()
    except ValueError:
        msg = "Not a valid datetime: '{0}'.".format(input)
        raise ArgumentTypeError(msg)


def listify(input):
    result = [x.strip() for x in input.split(',')]

    # print('listify, input={}, result={}'.format(input, result))

    return result
