iTodo for Sublime Text
------------------

iTodo is a GTD tool for managing todo list in Sublime Text editor.
This plugin contains a few text commands and syntax definition for ".todo" files.


Installation
------------------

To install this plugin, you have two options:

* Clone source code to Sublime Text 2 app folder, eg. ~/Library/Application Support/Sublime Text 2/iTodo.
* If you have [Package Control](http://wbond.net/sublime_packages/package_control) installed, simply search for iTodo to install.


Usage 
------------------

"⌘ + i": new task

"⌘ + d": toggle task completed


Samples 
------------------

Suppose we have a following todo file:

	Project A:
		- call mum tomorrow at 8 am.

Highlight this item line and press "⌘ + d", it marks a tag "@done" and also appends timestamp.

	Project A:
		+ call mum tomorrow at 8 am. @done (2012-01-08 18:12)

[iTodo - Sublime Text 2上的GTD插件](http://gchen.cn/2012/01/gtd-with-itodo-in-sublime-text/)

Contribution
------------------

Thanks Taskmate for TextMate (https://github.com/svenfuchs/taskmate).


Source code and support 
------------------

https://github.com/chagel/itodo