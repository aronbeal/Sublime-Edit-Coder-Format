#CoderFormatOnSave
This Sublime Text plugin is responsible for applying Drupal coder formatting to eligible files (php by default).  It does so leveraging the Coder module for drupal, part of which is bundled with this plugin.  For more information on the latter, see https://drupal.org/project/coder

## Installation
Note: this package must currently be installed manually; I hope to fix this in the future.

### Mac OSX (tested on 10.8)

1. Clone git repo into your packages folder (mine is ~/Library/Application Support/Sublime Text 2/Packages):
<code>
  $ cd ~/Library/Application Support/Sublime Text 2/Packages
  $ git clone https://github.com/aronbeal/Sublime-Edit-Coder-Format
</code>
2. Restart Sublime Text 2

##Usage
Only key binding so far is for OSX, which is set to ctrl+c to invoke coder formatting.  Also available under Tools->Coder Format->Coder Format, or as a quickwindow completion of "Coder Format".  Command is set to work only for .php, .install, and .module file suffixes; this can be changed under the preferences for the module (Preferences->Package Settings->Coder Format on OSX)

##Other notes
If you wish to use the version of coder present in another drupal instance, simply edit the "require" statement at the beginning of the coder_format.php file to point to the coder_format.inc file in your drupal instance.
