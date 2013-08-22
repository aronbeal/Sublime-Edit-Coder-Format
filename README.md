#Coder Format
This Sublime Text plugin is responsible for applying Drupal coder formatting to eligible files.  It does so leveraging the [Coder](https://drupal.org/project/coder) module for Drupal, part of which is bundled with this plugin.

## Installation
The recommended install is via the Package Control:
- Press ctrl+shift+p (Windows, Linux) or cmd+shift+p (OS X), start typing “Package” to access Package Manager commands
- When the list of packages is presented, search for "Coder Format", press enter to install

##Usage
The only key binding set so far is for OSX, which is set to ctrl+c to invoke coder formatting.  Also available under Tools->Coder Format->Coder Format, or as a quickwindow completion of "Coder Format".

##Notes:
- This plugin requires that php be installed on your system.
- "Eligible Files" currently consists of files suffixed in 'php','module', or 'inc'.  This setting can be modified by setting the preference 'allowed_coder_format_suffixes' in the module package settings (Preferences->Package Settings->Coder Format on OSX).  See the file "Preferences.sublime-settings" for an example of what this would look like.
- Current included version is coder_format.inc 7.x-2.0


