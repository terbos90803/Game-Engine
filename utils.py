# Helpful utilities

# Print a label followed by a comma separated list
def print_list(label, col):
    print(label, end='')
    print(*col, sep=', ')


# Compare two strings in a safe, case-insensitive way
def same_word(first, second):
  return first.casefold() == second.casefold()

# Prints *text* to the screen, 
# with a delay between characters of *typewriter_speed* (zero for no delay),
# a pause between paragraphs of *delay_after_paragraph*,
# wrapping text for the terminal width
def typewriter(text, typewriter_speed, delay_after_paragraph, paragraph_space, after_space):
  import textwrap
  import time
  import random
  import shutil

  columns, rows = shutil.get_terminal_size(fallback=(80, 24))

  first_paragraph = True

  # For each paragraph (list item):
  for paragraph in text:
    if not first_paragraph:
      for i in range(paragraph_space):
        print()

    # For each character
    for char in (textwrap.fill(paragraph, width=columns)):
      print(char, end="", flush=True)
      time.sleep(random.uniform(0.0, typewriter_speed))
    print() # end paragraph

    # Add a new line after each paragraph (list item)
    first_paragraph = False

    # Pause before next parapgraph
    time.sleep(delay_after_paragraph)

  for i in range(after_space):
    print()
    

# Convenience functions for the typewriter effect
def type_quick(text, paragraph_space=1, after_space=0):
  typewriter(text, 0.0, 0.0, paragraph_space, after_space)

def type_slow(text, paragraph_space=1, after_space=0):
  typewriter(text, 0.15, 0.5, paragraph_space, after_space)