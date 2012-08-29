#CoderFormatOnSave
This Sublime Text plugin is responsible for applying Drupal coder formatting to *.php and *.module (as of this version) files.  It does so leveraging the coder module for drupal, part of which is bundled with this plugin.  For more information on the latter, see https://drupal.org/project/coder

## Installation

### Mac OSX (Lion)

1. Clone git repo into your packages folder (mine is ~/Library/Application Support/Sublime Text 2/Packages):

<code>
  $ cd ~/Library/Application Support/Sublime Text 2/Packages
  $ git clone https://github.com/sublimator/ZenCoding.git
</code>

2. Restart Sublime Text 2

##Usage
This plugin requires that you tell Sublime Text that you wish to use it explicitly. To do so, you need to have defined a project (more info: http://www.sublimetext.com/docs/2/projects.html) for the code you're working on.  Edit your project to include the following line to the "settings" block: 

<code>
  "coder_format_on_save": 1
</code>

Once the module sees this, it will apply coder formatting to the contents of the window in the forefront immediately prior to any save event.  Note that it will ignore anything that does not have the correct file suffix (currently *.php or *.module, may expand in the future).


##Other notes
If you wish to use the version of coder present in another drupal instance, simply edit the "require" statement at the beginning of the coder_format.php file to point to the coder_format.inc file in your drupal instance.