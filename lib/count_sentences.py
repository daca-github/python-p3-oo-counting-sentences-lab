#!/usr/bin/env python3
import re

class MyString:

  def __init__(self,value=""):
    self._value = None
    self.value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):
    if not isinstance(value, str):
      print("The value must be a string.")
    else:
      self._value = value

  def is_sentence(self):
    return self.value.endswith('.')
  
  def is_question(self):
    return self.value.endswith('?')
  
  def is_exclamation(self):
    return self.value.endswith('!')

  def count_sentences(self):
    sentences = re.split('[.!?]+', self.value)
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)
