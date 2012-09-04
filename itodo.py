import sublime, sublime_plugin
from datetime import datetime 

class ItodoBase(sublime_plugin.TextCommand):
  COMPLETED_MARK = "@done"

  def run(self, edit):
    filename = self.view.file_name()
    # list of allowed filetypes
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
      line_head = self.view.find("[-\+]", line.begin())
      line_contents = self.view.substr(line).strip()
      # prepend @done if item is ongoing
      if line_contents.startswith('-'):
        self.view.insert(edit, line.end(), " "+ ItodoBase.COMPLETED_MARK +" (%s)" % datetime.now().strftime("%Y-%m-%d %H:%M"))
        self.view.replace(edit, line_head, "+")
      # undo @todo
      elif line_contents.startswith('+'):
        subfix = self.view.find('(\s)*'+ ItodoBase.COMPLETED_MARK +'(.)+\)$', line.begin())
        self.view.erase(edit, subfix)
        self.view.replace(edit, line_head, "-")
      
class ClearCommand(ItodoBase):
  def runCommand(self, edit):    
    if not sublime.ok_cancel_dialog("Are you sure to clear all completed items?"):
      return False
    for region in self.view.find_all(ItodoBase.COMPLETED_MARK):
      self.view.erase(edit, self.view.full_line(region))
      