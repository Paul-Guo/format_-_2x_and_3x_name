#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter
from tkinter import filedialog
import sys


class Display(tkinter.Frame):
    """ Demonstrate python interpreter output in Tkinter Text widget

type python expression in the entry, hit DoIt and see the results
in the text pane."""

    def __init__(self, parent=0):
        tkinter.Frame.__init__(self, parent)
        # self.entry = tkinter.Entry(self)
        # self.entry.pack()
        # self.doIt = tkinter.Button(self, text="DoIt", command=self.onEnter)
        # self.doIt.pack()
        self.output = tkinter.Text(self)
        self.output.pack()
        sys.stdout = self
        self.pack()

    # def onEnter(self):
    #     print eval(self.entry.get())

    def write(self, txt):
        self.output.insert(tkinter.END, str(txt))
        self.output.see(tkinter.END)


class TkFileDialog(tkinter.Frame):
    def __init__(self, root_frame, text_src):

        tkinter.Frame.__init__(self, root_frame)

        # options for buttons
        button_opt = {'fill': tkinter.BOTH, 'padx': 5, 'pady': 5}

        # define buttons
        # tkinter.Button(self, text='askopenfile', command=self.askopenfile).pack(**button_opt)
        # tkinter.Button(self, text='askopenfilename', command=self.askopenfilename).pack(**button_opt)
        # tkinter.Button(self, text='asksaveasfile', command=self.asksaveasfile).pack(**button_opt)
        # tkinter.Button(self, text='asksaveasfilename', command=self.asksaveasfilename).pack(**button_opt)
        self.text_src = text_src
        self.choose_text_variable = tkinter.StringVar()
        self.choose_text_variable.set(self.text_src)
        tkinter.Label(self, textvariable=self.choose_text_variable).pack(**button_opt)
        tkinter.Button(self, text='choose directory', command=self.askdirectory).pack(**button_opt)

        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'myfile.txt'
        options['parent'] = root_frame
        options['title'] = 'This is a title'

        # This is only available on the Macintosh, and only when Navigation Services are installed.
        # options['message'] = 'message'

        # if you use the multiple file version of the module functions this option is set automatically.
        # options['multiple'] = 1

        # defining options for opening a directory
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = root_frame
        options['title'] = 'This is a title'

    def askopenfile(self):

        """Returns an opened file in read mode."""

        return filedialog.askopenfile(mode='r', **self.file_opt)

    def askopenfilename(self):

        """Returns an opened file in read mode.
        This time the dialog just returns a filename and the file is opened by your own code.
        """

        # get filename
        filename = filedialog.askopenfilename(**self.file_opt)

        # open file on your own
        if filename:
            return open(filename, 'r')

    def asksaveasfile(self):

        """Returns an opened file in write mode."""

        return filedialog.asksaveasfile(mode='w', **self.file_opt)

    def asksaveasfilename(self):

        """Returns an opened file in write mode.
        This time the dialog just returns a filename and the file is opened by your own code.
        """

        # get filename
        filename = filedialog.asksaveasfilename(**self.file_opt)

        # open file on your own
        if filename:
            return open(filename, 'w')

    def askdirectory(self):

        """Returns a selected directoryname."""

        self.dir_opt['initialdir'] = self.text_src
        filedialog_askdirectory = filedialog.askdirectory(**self.dir_opt)
        if len(filedialog_askdirectory) > 0:
            self.text_src = filedialog_askdirectory
            self.choose_text_variable.set(self.text_src)
        return self.text_src


if __name__ == '__main__':
    pass
