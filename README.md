# The poemenia extension for OpenOffice and LibreOffice

Localize the OpenOffice [Pepito Cleaner](https://pepitoweb.altervista.org/pepito_cleaner/index.php) extension. 

Pepito Cleaner is a handy extension that can be used to detect and correct common errors, such as those that occur with scanning or when extracting text from PDF documents. This is done mainly with configurable search patterns, so-called regular expressions. 

The regular expressions that come with Pepito cleaner are closely related to country-specific punctuation rules and are not suitable for all languages. They have to be adapted for Germany and Austria, for example. This has to be done by the user himself. However, such changes require expertise and are not easy to transfer to other installations. Moreover, they will be lost when Pepito Cleaner is updated or reinstalled.

Since Pepito Cleaner seems to be no longer maintained, the developers are not identifiable, and the license terms of the software are unknown, I have programmed the extension *poemenia*, which helps to localize a Pepito Cleaner installation from the outside. 


## Visit the project's home page

For more information, see the [project home page (English)](https://peter88213.github.io/poemenia/index-en) with description and download instructions.

For a German translation, see the [project home page (German)](https://peter88213.github.io/poemenia/).


## How to add a language pack

Currently the *de-DE* option is available, suitable for Germany and Austria. However, *poemenia* can also add further language packs thanks to its modular structure.

### Customize Pepito Cleaner

1. Reset the *Pepito Cleaner* language if you want to start with English user interface and regex descriptions.
2. Use Pepito Cleaner's built-in RegEx editor to customize and extend the regular expressions. Translate the existing descriptions into your language.
3. Open Pepito Cleaner's **Language** window and create your own language file, e.g. **language_xx-YY**. Translate the user interface text entries.
4. Set Pepito Cleaner to your language, and test your customizazions and RegEx thoroughly.

Your customized files are located in the *extension directory*, visible by clicking on **Show extension path** in the **Options**. They all have the extension `.txt`.  

### Export the customized files

Let's assume you have cloned the *poemenia* project from GitHub, and your language variant is called **xx-YY**. 

Your customized files are:
* preference.txt
* language_xx-YY.txt
* RegEx_general.txt
* RegEx_hyphenation.txt
* RegEx_warning.txt
* RegEx_header.txt

### Add a macro module

Now export these files to your *poemenia* project.

1. Make a subdirectory **xx-YY** in the project's **oxt** folder.
2. Copy the files listed above from the *Pepito Cleaner* extension directory to the *poemenia* **xx-YY** subdirectory.
3. Open the **poemenia** subdirectory in the project's **oxt** folder.

Now create a language module file named `xx_YY.xba`: 

#### xx_YY.xba

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE script:module PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "module.dtd">
<script:module xmlns:script="http://openoffice.org/2000/script" script:name="xx_YY" script:language="StarBasic">REM  *****  BASIC  *****

&apos; Copy xx-YY localized configuration files to the Pepito Cleaner location

Sub localize_pepito

	common.localize_pepito(&quot;xx-YY&quot;)

End Sub
</script:module>
```

Now add your language module to the library. You do this by adding a line to `script.xlb`:

#### script.xlb

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE library:library PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "library.dtd">
<library:library xmlns:library="http://openoffice.org/2000/library" library:name="poemenia" library:readonly="false" library:passwordprotected="false">
 <library:element library:name="common"/>
 <library:element library:name="de_DE"/>
 <library:element library:name="xx_YY"/>
 <library:element library:name="help"/>
</library:library>
```

### Add a menu entry to poemenia

This is done by opening the **poemenia.odt** extension compiler located in the project's **oxt** folder. It is strongly advised to learn how to use it by reading the document carefully. 

1. Start OpenOffice with **poemenia.odt**. Allow macro execution.
2. Edit the Document's **Standard/Module 1/myExtension** macro.

Append a menu entry to the existing language entries:

```
  beginAddonMenu

    beginMenu
    
      beginTitles
        setTitle("poemenia - Set Pepito Cleaner language", "en")
        setTitle("poemenia - Sprache für Pepito Cleaner einstellen", "de")
      endTitles

      beginMenuItems

        beginCommand
            beginTitles()
              setTitle("Set Pepito Cleaner language to de-DE", "en")
              setTitle("Sprache für Pepito Cleaner zu de-DE setzen", "de")
            endTitles
            setURL("Basic", "poemenia", "de_DE", "localize_pepito")

        endCommand

        beginCommand
            beginTitles()
              setTitle("Set Pepito Cleaner language to xx-YY", "en")
              setTitle("Sprache für Pepito Cleaner zu xx-YY setzen", "de")
              setTitle("Agordu la lingvon por Pepito Cleaner al xx-YY", "xx")
            endTitles
            setURL("Basic", "poemenia", "xx_YY", "localize_pepito")

        endCommand
        
        addSeparator

```

You might wish to add *xx* translation lines to the other menu entries according to the example above.

### Build the extension

Now, change the version number in the `beginDescription` line and save the macro.

Compile the extension and install it on OpenOffice for testing. 



## Credits

[Pepito Cleaner](https://pepitoweb.altervista.org/pepito_cleaner/index.php) by the Guys From Italy

[OpenOffice Extension Compiler](https://wiki.openoffice.org/wiki/Extensions_Packager#Extension_Compiler) by Bernard Marcelly.


## License

This extension is distributed under the [MIT License](http://www.opensource.org/licenses/mit-license.php).
