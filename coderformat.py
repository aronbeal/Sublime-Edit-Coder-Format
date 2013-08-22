import sublime
import sublime_plugin
import re
from os import chdir,curdir,path
from subprocess import Popen, PIPE


class CoderFormat(sublime_plugin.TextCommand):
  def run(self, edit):
    if not path.exists('./coder_format.php'):
      raise Exception("coder_format.php does not exist")
    print("Coder format running")

    settings = sublime.load_settings('Preferences.sublime-settings')
    allowed_suffixes = settings.get('allowed_coder_format_suffixes', ['php','module','inc'])
    regex = []
    regex.append("^.*\.(")
    regex.append(("|".join(allowed_suffixes)))
    regex.append(")$")
    #print "Regex", ''.join(regex)
    regex = re.compile(''.join(regex))
    #deselect all text in preparation.
    if self.view.is_loading():
      return
    #if not current_view.is_dirty():
    #  return
    current_file = self.view.file_name()
    is_interesting = regex.search(current_file)
    #check to see if file suffix is matched.
    if is_interesting is not None:
      if current_file == None:
        print("Please save the file first")
        return
      print("Coder formatting file...")
      sublime.Selection.clear(self.view)
      region = sublime.Region(0, self.view.size())
      #sublime.Selection.add(self.view, alltext)

      try:
        bufferContent = self.view.substr(region)
        p = Popen(['/usr/bin/env', 'php', './coder_format.php'], stdin=PIPE, stdout=PIPE)
        #conversion to bytes necessary for interprocess communication
        bufferContent = p.communicate(bytes(bufferContent, 'UTF-8'))
        #decode reponse for re-insertion
        bufferContent = bufferContent[0].decode()
        self.view.replace(edit,region,bufferContent)
      finally:
        sublime.message_dialog("Coder format applied to file content")
    else:
      print("Not an eligible filetype.  Skipping.")
  def description():
    return "CoderFormats stuff"

