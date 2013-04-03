import sublime
import sublime_plugin
import re
from os import chdir,curdir,path
from subprocess import Popen, PIPE
from UserString import MutableString


class CoderFormat(sublime_plugin.TextCommand):

    def run(self, edit):
        print "Coder format running"
        current_view = sublime.active_window().active_view()
        current_file = current_view.file_name()
        if current_file == None:
            print "Please save the file first"
            return
        settings = sublime.load_settings('Preferences.sublime-settings')
        allowed_suffixes = settings.get('allowed_coder_format_suffixes', ['php','module','inc'])
        regex = []
        regex.append("^.*\.(")
        regex.append(("|".join(allowed_suffixes)))
        regex.append(")$")
        #print "Regex", ''.join(regex)
        regex = re.compile(''.join(regex))
        print "Coder Format request for file: ", current_file

        is_interesting = regex.search(current_file)
        #check to see if file suffix is matched.
        if is_interesting is not None:
            print "Coder formatting file..."
            #buffer is non-empty
            original_directory = curdir
            chdir(sublime.packages_path())
            chdir('Sublime-Edit-Coder-Format')
            try:
                print "Applying coder format to file : ", current_file

                edit = self.view.begin_edit('coder_format')
                bufferRegion = sublime.Region(0, self.view.size())
                bufferContent = self.view.substr(bufferRegion)
                if not path.exists('./coder_format.php'):
                    raise Exception("coder_format.php does not exist")
                p = Popen(['/usr/bin/env', 'php', './coder_format.php'], stdin=PIPE, stdout=PIPE)

                bufferContent = p.communicate(bufferContent)[0]
                self.view.replace(edit, bufferRegion, bufferContent)
                self.view.end_edit(edit)
            finally:
                chdir(original_directory)
        else:
            print "Not an eligible filetype.  Skipping."

