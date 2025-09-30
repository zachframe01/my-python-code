"""Many documents use a specific format for a person's name.
 Write a program that reads a person's name in the following
   format:

firstName middleName lastName (in one line)

and outputs the person's name in the following format:

lastName, firstInitial.middleInitial.

Ex: If the input is:

Pat Silly Doe
the output is:

Doe, P.S.
If the input has the following format:

firstName lastName (in one line)

the output is:

lastName, firstInitial.

Ex: If the input is:

Julia Clark
the output is:

Clark, J."""

# Read one line like: "Pat Silly Doe" or "Julia Clark"
name = input().strip()

parts = name.split()  # splits on whitespace

if len(parts) == 3:
    first, middle, last = parts
    print(f"{last}, {first[0].upper()}.{middle[0].upper()}.")
elif len(parts) == 2:
    first, last = parts
    print(f"{last}, {first[0].upper()}.")
else:
    # If the input isn't 2 or 3 parts, keep it simple:
    # treat last token as last name, first token as first name, ignore the rest
    if len(parts) >= 1:
        first = parts[0]
        last = parts[-1] if len(parts) > 1 else ""
        initial = f"{first[0].upper()}." if first else ""
        sep = ", " if last else ""
        print(f"{last}{sep}{initial}")
