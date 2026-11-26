import os
import sys

"""
# Entry validated: output is 1-200 chars, one line, deterministic.
Writes a single rejected Olympic sport entry to the output directory.
The sport: Synchronised Meeting Muting — a painfully relatable corporate event.
"""

LINE = "Synchronised Meeting Muting — teams of four join one Zoom from adjacent cubicles, scored on mute-toggle latency, toddler scream suppression, and the \"sorry, you go first\" dance"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    content = LINE + "\n"
    
    # Validate
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError(f"Content length {len(content)} invalid or only whitespace")
    if content.count("\n") != 1 or content.endswith("\n\n"):
        raise ValueError("Content must contain exactly one line")
    
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    # Also write to /output/entry.txt if different directory
    if os.path.normpath(output_dir) != os.path.normpath("/output"):
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass  # Best effort, ignore errors
    
    print(f"Wrote {len(content)} chars to {output_path}")


if __name__ == "__main__":
    main()
