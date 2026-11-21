#!/usr/bin/env python3
"""World News — 21 November 2026 (make.fun bounty entry).

Copies the shipped front-page image (assets/entry.png, next to this script)
into the output directory as entry.png, byte-for-byte identical.

The output directory defaults to /output and can be overridden with the
MAKEFUN_OUTPUT_DIR environment variable or the --output-dir flag. After
copying, the script verifies the output's SHA-256 against the shipped
image, so a truncated or corrupted copy fails loudly instead of passing
silently. Standard library only, no network, no randomness — the same
bytes come out every run.
"""

import argparse
import hashlib
import os
import shutil
import sys

DEFAULT_OUTPUT_DIR = "/output"
IMAGE_NAME = "entry.png"


def shipped_image_path():
    """Path to the image shipped with this repo, resolved from this file."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "assets", IMAGE_NAME)


def sha256_of(path):
    """SHA-256 hex digest of a file, read in chunks."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="Copy the shipped front-page image to the output directory.")
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Output directory (overrides MAKEFUN_OUTPUT_DIR and /output).")
    return parser.parse_args(argv)


def output_dir(args):
    """Output directory: --output-dir flag, else MAKEFUN_OUTPUT_DIR, else default."""
    if args.output_dir:
        return args.output_dir
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR


def main(argv=None):
    args = parse_args(argv)
    src = shipped_image_path()
    if not os.path.isfile(src):
        print("error: shipped image not found: %s" % src, file=sys.stderr)
        return 1

    dest_dir = output_dir(args)
    try:
        os.makedirs(dest_dir, exist_ok=True)
    except OSError as exc:
        print("error: cannot create output directory %s: %s" % (dest_dir, exc),
              file=sys.stderr)
        return 1

    dest = os.path.join(dest_dir, IMAGE_NAME)
    try:
        shutil.copyfile(src, dest)
    except OSError as exc:
        print("error: cannot copy image to %s: %s" % (dest, exc),
              file=sys.stderr)
        return 1

    # Verify the copy is byte-for-byte identical to the shipped image.
    if sha256_of(src) != sha256_of(dest):
        print("error: verification failed, %s does not match %s"
              % (dest, src), file=sys.stderr)
        return 1

    print("wrote %s (%s)" % (dest, sha256_of(dest)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
