# Helpful utilities

# Print a label followed by a comma separated list
# Result looks like: label item1, item2, item3
#
# label: string
# collection: list or set of printable things
def print_list(label, collection):
    print(label, end='')
    print(*collection, sep=', ')


# Compare two strings in a safe, case-insensitive way
# Returns True if the strings are the same word(s), regardless of case.
# Thus: same_word('bob', 'Bob') == True
def same_word(first, second):
  return first.casefold() == second.casefold()


# Prints *text* to the screen, 
# with a randomized delay between characters of *typewriter_speed* (zero for no delay),
# a pause between paragraphs of *delay_after_paragraph*,
# wrapping text for the terminal width
#
# text: list of strings.  Each string is a complete paragraph.
# typewriter_speed: maximum delay between characters, in seconds.  Actual delay is randomized
# delay_after_paragraph: delay between paragraphs, in seconds.
# paragraph_space: how many blank lines to insert between paragraphs.
# after_space: how many blank lines to insert after last paragraph.
def typewriter(text, typewriter_speed, delay_after_paragraph, paragraph_space, after_space):
  import textwrap
  import time
  import random
  import shutil

  maxwidth = 80
  columns, rows = shutil.get_terminal_size(fallback=(maxwidth, 24))
  if columns > maxwidth:
    columns = maxwidth

  first_paragraph = True

  # For each paragraph (list item):
  for paragraph in text:
    if not first_paragraph:
      # Add blank line(s) after each paragraph (list item)
      first_paragraph = False
      for i in range(paragraph_space):
        print()

    # Print one charater at a time, breaking lines only between words.
    # Randomly vary the delay between characters to give a live-typed appearance.
    for char in (textwrap.fill(paragraph, width=columns)):
      print(char, end="", flush=True)
      time.sleep(random.uniform(0.0, typewriter_speed))
    print() # end paragraph

    # Pause between parapgraphs
    time.sleep(delay_after_paragraph)

  # add blank lines after entire block of text.
  for i in range(after_space):
    print()
    

# Convenience functions for the typewriter effect
# type_quick removes all delay
def type_quick(text, paragraph_space=1, after_space=0):
  typewriter(text, 0.0, 0.0, paragraph_space, after_space)

def type_slow(text, paragraph_space=1, after_space=0):
  typewriter(text, 0.10, 0.5, paragraph_space, after_space)