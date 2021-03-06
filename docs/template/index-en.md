[Deutsch](index)

--------------------------

![Screenshot: poemenia menu](Screenshots/menu-en.png)

# The poemenia extension for OpenOffice and LibreOffice with a German language pack for Pepito Cleaner

[Pepito Cleaner](https://pepitoweb.altervista.org/pepito_cleaner/index.php) is an extremely handy extension that can be used to detect and correct common errors, such as those that occur with scanning or when extracting text from PDF documents. This is done mainly with configurable search patterns, so-called regular expressions. 

The default regular expressions in Pepito Cleaner recognize quotation marks as they are common in the USA, also *guillemets* as used for example in Italy and Switzerland. In order for Pepito Cleaner to recognize the in Germany and Austria commonly used inverted commas („…“) and chevrons (»…«) as opening and closing quotation marks, the user has to change the regular expressions himself. However, such changes require expertise and are not easy to transfer to other installations. Moreover, they will be lost again when Pepito Cleaner is updated or reinstalled.

The *poemenia* extension helps this problem by copying ready-made configuration files into the installation directory of Pepito Cleaner and thus localizing it. Existing configuration files are saved so that the localization can be undone.

The "de-DE" language package of poemenia translates the user interface of Pepito Cleaner (as far as possible) and adapts the behavior to the punctuation rules common in Germany and Austria. Poemenia's verification rules contain some additions, e.g. for the correct placement of apostrophes, dashes and different quotation marks.

## Other languages

Although currently only a German language pack is available, you can add more language packs to *poemenia* thanks to its modular structure. You can find instructions on how to do this on the [project page](https://github.com/peter88213/poemenia).

## System requirements

* **OpenOffice.org 3.x** or **Apache OpenOffice 4.x** or **LibreOffice 6+**
* **Pepito Cleaner** must be installed.
* **Java** (OpenOffice needs it to execute macros.)

## Download and install

* [Download (poemenia-0.99.0.oxt)](https://raw.githubusercontent.com/peter88213/poemenia/main/poemenia-0.99.0.oxt)

* Installation right at download, by double-clicking on the downloaded file, or via the OpenOffice/LibreOffice Extension Manager.

* After installation (and Office restart) you find a new submenu in the **Tools/Add-Ons** menu.

[Changelog](changelog)

## Usage

See the [instructions for use (German)](help-de)

## Get updates

This extension supports the update mechanism of OpenOffice/LibreOffice. You can let the Extension Manager check for updates from time to time to get the latest release.

## Credits

[Pepito Cleaner](https://pepitoweb.altervista.org/pepito_cleaner/index.php) by the Guys From Italy

[OpenOffice Extension Compiler](https://wiki.openoffice.org/wiki/Extensions_Packager#Extension_Compiler) by Bernard Marcelly.


## License

This extension is distributed under the [MIT License](http://www.opensource.org/licenses/mit-license.php).
