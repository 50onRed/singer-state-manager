import argparse
import io
import json
import os
import sys

import singer
from singer import utils

LOGGER = singer.get_logger()


@utils.handle_top_exception(LOGGER)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s', '--state',
        help='State file',
        required=True)

    args = parser.parse_args()
    state_file = args.state
    temp_state_file = "{}.tmp".format(state_file)

    text_lines = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

    for line in text_lines:
        try:
            msg = json.loads(line)
        except json.decoder.JSONDecodeError:
            LOGGER.error('Unable to parse:\n%s', line)
            raise

        if 'type' not in msg:
            raise Exception("Line is missing required key 'type': {}".format(line))
        msg_type = msg['type']

        if msg_type == 'STATE':
            with open(temp_state_file, mode='w') as temp:
                temp.write(line)
                temp.flush()

            # Atomically move valid state
            os.rename(temp_state_file, state_file)

        sys.stdout.write("{}\n".format(line))
        sys.stdout.flush()


if __name__ == "__main__":
    main()
