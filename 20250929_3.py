"""Character counter homework.

Reads a line of input where the first token is a single
character and the rest of the line is the phrase to search.
Prints the number of occurrences and uses the plural form
like "n's" when the count is not exactly 1.

Examples (input -> output):
  n Monday        -> 1 n
  z Today is Monday -> 0 z's
  n It's a sunny day -> 2 n's
  n Nobody         -> 0 n's

Behavior:
  - Case-sensitive ("n" != "N").
  - If the input doesn't contain a phrase, phrase may be empty.
"""

import sys


def format_output(ch: str, count: int) -> str:
	"""Return the correctly formatted output string.

	If count == 1, return "1 <ch>". Otherwise return "<count> <ch>'s".
	"""
	if count == 1:
		return f"{count} {ch}"
	else:
		return f"{count} {ch}'s"


def main() -> None:
	# Read the entire input line from stdin
	raw = sys.stdin.read().strip()

	# If no input was provided, nothing to do
	if not raw:
		return

	# Split into tokens: first token is character, rest is phrase
	parts = raw.split(None, 1)  # split on whitespace at most once

	ch = parts[0]
	phrase = parts[1] if len(parts) > 1 else ""

	# Ensure the character input is exactly one character
	if len(ch) != 1:
		# If user provided something like "n Monday" this won't happen,
		# but guard to avoid misbehavior; take first character.
		ch = ch[0]

	count = phrase.count(ch)

	print(format_output(ch, count))


if __name__ == "__main__":
	main()