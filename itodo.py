import sublime, sublime_plugin
from datetime import datetime 

class ItodoBase(sublime_plugin.TextCommand):
  def run(self, edit):
    filename = self.view.file_name()
    # list of allowed filetypes
    # (added this because some people, like me, tend to use .txt files because they're more universal)
    # (this means that i have to manually set syntax for such file, but it's no sweat ;)
    allowed_filetypes = ('.todo', '.txt')
    if filename is None or not filename.endswith(allowed_filetypes):
      return False  
    self.runCommand(edit)

class NewCommand(ItodoBase):
  def runCommand(self, edit):
    for region in self.view.sel():
      line = self.view.line(region)
      # don't add a newline when creating new item with cursor is at an empty line
      if not line:
        line_contents = '- '
        self.view.insert(edit, line.begin(), line_contents)
      # add a newline when creating new item when cursor is at another line
      else:
        line_contents = self.view.substr(line) + '\n- '
        self.view.replace(edit, line, line_contents)

class CompleteCommand(ItodoBase):
  def runCommand(self, edit):    
    for region in self.view.sel():
      line = self.view.line(region)
      line_contents = self.view.substr(line).strip()
      # prepend @done if item is ongoing
      if line_contents.startswith('-'):
        self.view.insert(edit, line.end(), " @done (%s)" % datetime.now().strftime("%Y-%m-%d %H:%M"))
        self.view.replace(edit, self.view.word(line.begin()), "+ ")
      # undo @todo
      elif line_contents.startswith('+'):
        subfix = self.view.find('(\s)*@done(.)+\)$', line.begin())
        self.view.erase(edit, subfix)
        self.view.replace(edit, self.view.word(line.begin()), "- ")
      