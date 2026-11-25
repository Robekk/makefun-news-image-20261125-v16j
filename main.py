"""Deliver the front page.

The submission for make.fun's news-image-20261125 bounty is a single
1024x1024 PNG, committed next to this file as entry.png. The harness
runs this module in a sandbox with no network, so the whole job is:
find the output directory, copy the picture there byte for byte, and
report what landed.
"""

from pathlib import Path
import os
import sys

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def find_output_dir() -> Path:
    """The harness names the destination; /output is the fallback."""
    for variable in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        raw = os.environ.get(variable)
        if raw:
            return Path(raw)
    return Path("/output")


def png_dimensions(payload: bytes) -> tuple[int, int]:
    """Width and height live in the IHDR chunk, bytes 16 to 24."""
    width = int.from_bytes(payload[16:20], "big")
    height = int.from_bytes(payload[20:24], "big")
    return width, height


def main() -> int:
    source = Path(__file__).resolve().parent / "entry.png"
    payload = source.read_bytes()
    if not payload.startswith(PNG_SIGNATURE):
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    width, height = png_dimensions(payload)
    destination_dir = find_output_dir()
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / "entry.png"
    destination.write_bytes(payload)
    print(f"wrote {destination} ({len(payload)} bytes, {width}x{height})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
