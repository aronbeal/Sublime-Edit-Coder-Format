from sublime import *
from sublime_plugin import *
from re import compile
from os import chdir
from subprocess import Popen, PIPE


class CoderFormat(sublime_plugin.TextCommand):

    def run(self, edit):
        if self.view.settings().get('coder_format') == 1:
            p = compile('^.*(module|php|.install)$')
            myfile = self.view.file_name()
            is_interesting = p.search(myfile)

            if is_interesting.start() != is_interesting.end():
                #buffer is non-empty
                original_directory = os.curdir
                chdir(sublime.packages_path())
                chdir('CoderFormat')
                try:
                    print "Applying coder format to selection in file : ", myfile

                    edit = self.view.begin_edit('coder_format')
                    bufferRegion = sublime.Region(0, self.view.size())
                    bufferContent = self.view.substr(bufferRegion)
                    if not os.path.exists('./coder_format.php'):
                        raise Exception("coder_format.php does not exist")
                    p = Popen(['/usr/bin/php', './coder_format.php'], stdin=PIPE, stdout=PIPE)

                    bufferContent = p.communicate(bufferContent)[0]
                    self.view.replace(edit, bufferRegion, bufferContent)
                    self.view.end_edit(edit)
                finally:
                    os.chdir(original_directory)
