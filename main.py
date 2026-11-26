"""Rejected Olympic Sports (round 2): write one funny single-line sport
the Olympics turned down to $MAKEFUN_OUTPUT_DIR/entry.txt.
Output is 1-200 chars, one line, deterministic.
"""
import os
import sys

def main() -> int:
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'entry.txt')
    LINE = 'Tupperware Lid Matching Decathlon — 50 containers, 47 lids, 3 minutes. Scored on seal integrity shake test, stack height, and “I swear this lid belongs to that bottom” penalty appeals.'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(LINE + '\n')
    return 0

if __name__ == '__main__':
    sys.exit(main())
