import sublime, sublime_plugin, re, os
from subprocess import Popen, PIPE
from tempfile import NamedTemporaryFile


class CoderFormat(sublime_plugin.TextCommand):

    def run(self, edit):
        if self.view.settings().get('coder_format') == 1:
            p = re.compile('^.*(module|php|.install)$')
            myfile = self.view.file_name()
            project_folder = self.view.window().folders()[0]
            is_interesting = p.search(myfile)
            
            if is_interesting.start() != is_interesting.end():
                #buffer is non-empty
                original_directory = os.curdir
                os.chdir(sublime.packages_path())
                os.chdir('CoderFormat')
                try:
                    print "Applying coder format to selection in file : " , myfile

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
    def description(self):
        return "CoderFormatOnText Description";