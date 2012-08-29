import sublime, sublime_plugin, re, os
from subprocess import Popen, PIPE
from tempfile import NamedTemporaryFile


class CoderFormatOnSave(sublime_plugin.EventListener):

    def on_pre_save(self, view):
        print "***************** BEGIN ********************"
        should_build = view.settings().get('coder_format_on_save')
        if should_build == 1:
            p = re.compile('^.*(module|php)$|')
            myfile = view.window().active_view().file_name()
            project_folder = view.window().folders()[0]
            is_interesting = p.search(myfile)
            if is_interesting.start() != is_interesting.end():

                original_directory = os.curdir
                os.chdir(sublime.packages_path())
                os.chdir('CoderFormatOnSave')
                try:
                    print "Running coder format on file : " , myfile
                    edit = view.begin_edit()
                    buffer = view.window().active_view().visible_region()
                    code = view.substr(buffer).strip()

                    if not os.path.exists('./coder_format.php'):
                        raise Exception("coder_format.php does not exist")
                    p = Popen(['/usr/bin/php', './coder_format.php'], stdin=PIPE, stdout=PIPE)

                    code = p.communicate(code)[0]
                    view.replace(edit, buffer, code)
                    view.end_edit(edit)
                finally:  
                    os.chdir(original_directory)