[Deutsch](index)

# The poemenia extension for OpenOffice with a German language pack for Pepito Cleaner

![Screenshot: poemenia menu](Screenshots/menu-en.png)


[Pepito Cleaner](https://pepitoweb.altervista.org/pepito_cleaner/index.php) is an extremely handy extension that can be used to detect and correct common errors, such as those that occur with scanning or when extracting text from PDF documents. This is done mainly with configurable search patterns, so-called regular expressions. 

The default regular expressions in Pepito Cleaner recognize quotation marks as they are common in the USA, also  _guillemets_  as used for example in Italy and Switzerland. In order for Pepito Cleaner to recognize the in Germany and Austria commonly used inverted commas („…“) and chevrons (»…«) as opening and closing quotation marks, the user has to change the regular expressions himself. However, such changes require expertise and are not easy to transfer to other installations. Moreover, they will be lost again when Pepito Cleaner is updated or reinstalled.

The  _poemenia_  extension helps this problem by copying ready-made configuration files into the installation directory of Pepito Cleaner and thus localizing it. Existing configuration files are saved so that the localization can be undone.

The "de-DE" language package of poemenia translates the user interface of Pepito Cleaner (as far as possible) and adapts the behavior to the punctuation rules common in Germany and Austria. Poemenia's verification rules contain some additions, e.g. for the correct placement of apostrophes, dashes and different quotation marks.

## Other languages

Although there is currently only a German language pack available,  _poemenia_  can also add further language packs thanks to its modular structure.

## System requirements

* __OpenOffice.org 3.x__  or  __Apache OpenOffice 4.x__
* __Pepito Cleaner__  must be installed.
* __Java__ (OpenOffice needs it to execute macros.)

## Download an d install

* [Download (poemenia-0.99.0.oxt)](https://raw.githubusercontent.com/peter88213/poemenia/main/poemenia-0.99.0.oxt)

* Installation right at download, by double-clicking on the downloaded file, or via the OpenOffice/LibreOffice Extension Manager.

* After installation (and Office restart) you find a new submenu in the  __Tools/Add-Ons__  menu.

[Changelog](changelog)

## Usage

See the [instructions for use (German)](help-de)

## CREDITS

[Pepito Cleaner](https://pepitoweb.altervista.org/pepito_cleaner/index.php) by the Guys From Italy

[OpenOffice Extension Compiler](https://wiki.openoffice.org/wiki/Extensions_Packager#Extension_Compiler) by Bernard Marcelly.


## License

This extension is distributed under the [MIT License](http://www.opensource.org/licenses/mit-license.php).
