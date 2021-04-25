md ..\..\oxt\help
md ..\..\oxt\help\Screenshots

xcopy /s ..\..\docs\Screenshots\*.png ..\..\oxt\help\Screenshots\

pandoc.exe -o body.html ..\..\docs\help-de.md
copy /B header.txt+body.html+footer.txt ..\..\oxt\help\help.html

del body.html
