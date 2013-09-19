import sublime
import sublime_plugin
import re
from os import chdir,curdir,path,access,X_OK
from subprocess import Popen, PIPE, STDOUT


class CoderFormat(sublime_plugin.TextCommand):
  def run(self, edit):
    if self.view.is_loading():
      return
    package_dir = sublime.packages_path() + '/Sublime-Text-Coder-Format'
    coder_format_php = package_dir + '/coder_format.php'
    if not path.isfile(coder_format_php) or not access(coder_format_php, X_OK):
      raise Exception("coder_format library '"+coder_format_php+"' does not exist")
    print("Coder format running")

    settings = sublime.load_settings('Preferences.sublime-settings')
    allowed_suffixes = settings.get('allowed_coder_format_suffixes', ['php'])
    regex = re.compile(''.join(["^.*\.(", "|".join(allowed_suffixes), ")$"]))
    #deselect all text in preparation.

    #if not current_view.is_dirty():
    #  return
    current_file = self.view.file_name()
    is_interesting = regex.search(current_file)
    #check to see if file suffix is matched.
    if is_interesting is not None:
      if current_file == None:
        #Necessary for file suffix check
        sublime.message_dialog("The current file must be saved before coder formatting can be applied")
        return
      sublime.Selection.clear(self.view)
      region = sublime.Region(0, self.view.size())
      #sublime.Selection.add(self.view, alltext)

      try:
        bufferContent = self.view.substr(region)
        if bufferContent == '':
          return;

        p = Popen(['/usr/bin/env', 'php', coder_format_php], cwd=package_dir, stdin=PIPE, stdout=PIPE, stderr=STDOUT, shell=False)
        #conversion to bytes necessary for interprocess communication
        bufferContent = p.communicate(bytes(bufferContent, 'UTF-8'))

        #decode reponse for re-insertion
        bufferContent = bufferContent[0].decode()
        #Yprint(bufferContent)
        if p.returncode != 0 or bufferContent == '':
          raise Exception("Interprocess communication fail.")
        self.view.replace(edit,region, bufferContent)
      finally:
        print("Coder format applied to content")
        #sublime.message_dialog("Coder format applied to file content")
    else:
      print(current_file + " is not an eligible filetype.  Eligible files must end with any of: " + ','.join(allowed_suffixes));
      print("To modify eligible filetypes, set the preference 'allowed_coder_format_suffixes' to be an array of allowed file suffixes.")
  def description():
    return "Applies Drupal Coder Format to content in active window"

