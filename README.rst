===============
jEdit IDE HowTo
===============

:jEdit Homepage: http://www.jedit.org/
:Wikipedia: https://en.wikipedia.org/wiki/JEdit

jEdit is a mature programmer's text editor with hundreds (counting the time developing plugins) of person-years of development behind it. 

In less than no time it can be configured into an IDE for almost any language. For this ``HowTo`` we will use the computer algebra system 
``FriCAS``. Hence we assume you have ``fricas`` installed and you are using some Lin(ux) or Windows 10/WSL. The editor ``jEdit`` can be installed by ``apt/deb`` (used below) or by a method described on the jEdit Homepage.

.. image:: docs/pics/jeditIDE.png
  :alt: jeditIDE
 


Install jEdit
=============

::

  $ sudo apt install jedit 
  
  $ apt list jedit 
  Listing... Done
  jedit/bionic,bionic,now 5.5.0+dfsg-1 all [installed]
  
  $ jedit -version
  jEdit 5.5.0
  $ jedit -usage


:Start: jEdit 

::

  $ jedit &


.. image:: docs/pics/jedit1.png
  :width: 200px
  :height: 100px
  :align: center
  :alt: jedit1
 
Install Plugins
===============

:Mark: [x] the plugins in the Plugin Manager. 

.. image:: docs/pics/jedit2.png
  :width: 400
  :alt: jedit2

Mandatory
---------

* Console
* ContextMenu
* ProjectViewer
* Templates
* TextFilter
* GnuRegexp

.. image:: docs/pics/jedit3.png
  :width: 400
  :alt: jedit3
  
Recommended/Optional
--------------------

* BufferList
* CharacterMap
* Code2HTML
* ImageViewer
* InfoViewer
* JDiffPlugin
* MarkdownPlugin
* SpellCheck
  
.. image:: docs/pics/jedit4.png
  :width: 400
  :alt: jedit4


Check the appearance
--------------------

Now you should see some new (docked) windows, ``BufferList``
for instance. 

.. image:: docs/pics/jedit5.png
  :width: 400
  :alt: jedit5
  
:Click: on ``BufferList`` in the right docking area.

It will expand.

.. image:: docs/pics/jedit6.png
  :width: 400
  :alt: jedit6

Same for the ``Console``.

.. image:: docs/pics/jedit7.png
  :width: 400
  :alt: jedit7
  
:Enter: some commands, and check if ``~/.jedit`` is available.

:Warning: This is crucial for the further installation. 

.. image:: docs/pics/jedit8.png
  :width: 400
  :alt: jedit8
  
Install an Edit Mode
--------------------
Copy the ``mode/spad.xml`` file to ``~/.jedit/modes/`` (see below) and
add ::

   <MODE NAME="spad" FILE="spad.xml" FILE_NAME_GLOB="*.{spad,input}" />
   
to the file ``~/.jedit/modes/catalog``. The code below will just perform these steps.

::

  $ cp -v spad.xml ~/.jedit/modes/

  $ export jcat_tmp=~/.jedit/modes/catalog
  $ cat $jcat_tmp add_spad_to_catalog.txt > $jcat_tmp


:NOTE: Now **retart** jEdit, i.e. close and reopen (``jedit &``).

Open a new file
---------------

:Menu: ``File -> New In Mode``

Find ``spad`` (hopefully).

.. image:: docs/pics/jedit9.png
  :width: 400
  :alt: jedit9

**Syntax highlighting**: Enter some keywords.

The color scheme can be adjusted of course.


.. image:: docs/pics/jedit10.png
  :width: 400
  :alt: jedit10
  
  
.. image:: docs/pics/jedit11.png
  :width: 400
  :alt: jedit11



Configure the Console
---------------------
Plugin -> Console -> compile & run

.. image:: docs/pics/jedit12.png
  :width: 400
  :alt: jedit12

Configure the Context Menu
--------------------------
As above, configure the context menu.

.. image:: docs/pics/jedit13.png
  :width: 400
  :alt: jedit13
  
Press the [+] button.
  
.. image:: docs/pics/jedit14.png
  :width: 400
  :alt: jedit14

Look for ``Run current buffer ...``

.. image:: docs/pics/jedit15.png
  :width: 400
  :alt: jedit15

Repeat the above steps in order to add
``Compile current buffer ...``

.. image:: docs/pics/jedit16.png
  :width: 400
  :alt: jedit16
  
Now the menu item ``spad`` (or whatever label you have given) should appear.

.. image:: docs/pics/jedit17.png
  :width: 400
  :alt: jedit17
  
Installing the Templates
------------------------
First, copy the templates to the ``~/.jedit/templates`` folder ::

  $ cp -v templates/spad_* ~/.jedit/templates/
  'templates/spad_category.vm' -> '/home/kfp/.jedit/templates/spad_category.vm'
  'templates/spad_domain.vm' -> '/home/kfp/.jedit/templates/spad_domain.vm'
  'templates/spad_package.vm' -> '/home/kfp/.jedit/templates/spad_package.vm'
  'templates/spad_unittest.vm' -> '/home/kfp/.jedit/templates/spad_unittest.vm'



Plugins -> Templates -> Template Tree 
  
.. image:: docs/pics/jedit18.PNG
  :width: 400
  :alt: jedit18

Dock the floating ``template tree window`` to the **left** docking area_. 

.. image:: docs/pics/jedit19.png
  :width: 400
  :alt: jedit19
  
Choose ``refresh templates``, and you will see the installed templates.

.. image:: docs/pics/jedit20.png
  :width: 400
  :alt: jedit20

.. image:: docs/pics/jedit21.png
  :width: 400
  :alt: jedit21
  
Install the Macros
------------------
In this example only one macro will be installed (lookup FriCAS API).
::

  $ mkdir ~/.jedit/macros/FriCAS
  $ cp -v  macros/fricas_api.bsh ~/.jedit/macros/FriCAS 
  'macros/fricas_api.bsh' -> '/home/kfp/.jedit/macros/FriCAS/fricas_api.bsh'

  Choose ``Macros -> Rescan Macros`` and you should find the folder ``FriCAS`` containing the macro files (bean shell, .bsh)
  ``fricas_api``:
  
.. image:: docs/pics/jedit22.png
  :width: 400
  :alt: jedit22
  
Add it to the ``contex menu`` **spad** ([+] button)  

.. image:: docs/pics/jedit23.png
  :width: 400
  :alt: jedit23

Add a ``separator`` for convenience,

.. image:: docs/pics/jedit24.png
  :width: 400
  :alt: jedit24

find the ``Macros`` menu entry,

.. image:: docs/pics/jedit25.png
  :width: 400
  :alt: jedit25

and look for ``fricas_api``.

.. image:: docs/pics/jedit26.png
  :width: 400
  :alt: jedit26
  
Now press OK.  
  
.. image:: docs/pics/jedit27.png
  :width: 400
  :alt: jedit27

We want to use it. Mouse-Select a FriCAS Type (e.g. Integer), and
::

   Menu: spad -> fricas_api 
 

.. image:: docs/pics/jedit28.png
  :width: 400
  :alt: jedit28
  
should display (in Firefox, otherwise edit the script) the corresponding FriCAS API webpage.

.. image:: docs/pics/jedit29.png
  :width: 400
  :alt: jedit29

Finally, customize jEdit to your needs, e.g. by arranging the dockable windows and so on.

.. image:: docs/pics/jedit30.png
  :width: 400
  :alt: jedit30

































