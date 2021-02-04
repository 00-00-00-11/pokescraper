import pyperclip
from pynput import keyboard
from pynput.keyboard import Listener

COMBINATION = {keyboard.Key.cmd, keyboard.Key.ctrl}

HEB_TO_ENG = {'ש': 'a',
              'נ': 'b',
              'ב': 'c',
              'ג': 'd',
              'ק': 'e',
              'כ': 'f',
              'ע': 'g',
              'י': 'h',
              'ן': 'i',
              'ח': 'j',
              'ל': 'k',
              'ך': 'l',
              'צ': 'm',
              'מ': 'n',
              'ם': 'o',
              'פ': 'p',
              '/': 'q',
              'ר': 'r',
              'ד': 's',
              'א': 't',
              'ו': 'u',
              'ה': 'v',
              '׳': 'w',
              'ס': 'x',
              'ט': 'y',
              'ז': 'z', }
ENG_TO_HEB = {'a': 'ש',
              'b': 'נ',
              'c': 'ב',
              'd': 'ג',
              'e': 'ק',
              'f': 'כ',
              'g': 'ע',
              'h': 'י',
              'i': 'ן',
              'j': 'ח',
              'k': 'ל',
              'l': 'ך',
              'm': 'צ',
              'n': 'מ',
              'o': 'ם',
              'p': 'פ',
              'q': '/',
              'r': 'ר',
              's': 'ד',
              't': 'א',
              'u': 'ו',
              'v': 'ה',
              'w': '׳',
              'x': 'ס',
              'y': 'ט',
              'z': 'ז'}

# The currently active modifiers
current = set()


def convertGibrish(text):
  converted = ''

  for l in text.lower():
    if l.lower() in ENG_TO_HEB.keys():
      converted += ENG_TO_HEB.get(l)

    elif l in HEB_TO_ENG.keys():
      converted += HEB_TO_ENG.get(l)

    else:
      converted += l

  return converted


def on_press(key):
  if key in COMBINATION:
    current.add(key)
    if all(k in current for k in COMBINATION):
      text = pyperclip.paste()
      text = convertGibrish(text)
      pyperclip.copy(text)
      pyperclip.paste()
  if key == keyboard.Key.esc:
    listener.stop()


def on_release(key):
  try:
    current.remove(key)
  except KeyError:
    pass


with Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()
