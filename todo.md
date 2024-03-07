#### Features
- [x] Multiple tabs/buffers
    - [x] Make them show up in the status bar (just did it below instead)
- [x] Add file_path error checking
- [x] Set command line to create files passed if they don't exist
- [x] Refactor to remove all the duplicate code in editor.py
- [x] Fix error from saving with no tabs open
    - [x] There is another bug related to the decorator now

#### Most Important
- [x] Remove movable tab on menu 
- [ ] Fix text formatting in general
    - [ ] Copy/pasting doesn't auto change font
    - [ ] Fix tabs in text 
- [ ] Right now crashed when attempting to load certain files
    - Files encoded in certain ways crash the loading,
        such as .wav files
- [ ] Properly implement QTextEdit for text instead of QPlainTextEdit
- [ ] Add a way to open a directory 
- [ ] Add file tree from current directory
- [ ] Don't allow opening same file more than once
    - Just make it switch to the tab if file already open

#### Difficult
- [ ] Syntax highlighting
    - Right now only lints / changes font and size ???
- [ ] Run code in editor

