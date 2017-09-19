#!/usr/bin/env python
# -*- coding: utf-8 -*-


def remove(folder):
    print('start remove')
    import os
    dirs = os.listdir(folder)
    print('folder ', folder, ', dirs: ', dirs)
    for d in dirs:
        import re

        # rename @2x
        m = re.compile('(.*?)@2x(\..*)$').match(d)
        if m:
            gs = m.groups()
            print('found @2x ', d)
            os.rename(folder + os.path.sep + d, folder + os.path.sep + gs[0] + gs[1])
        else:
            # move @3x
            m = re.compile('(.*?)@3x(\..*)$').match(d)
            if m:
                # check 3x folder
                folder_3x = folder + os.path.sep + '@3x'
                if not os.path.exists(folder_3x):
                    os.mkdir(folder_3x)
                # move to @3x
                gs = m.groups()
                print('found @3x ', d)
                os.rename(folder + os.path.sep + d, folder_3x + os.path.sep + gs[0] + gs[1])
    print('end remove')


def pick_file(command):
    import tkinter
    import tk_file_dialog

    root = tkinter.Tk()

    tfd = tk_file_dialog.TkFileDialog(root, '.')
    tfd.pack()

    start_btn = tkinter.Button(root,
                               text='start',
                               command=lambda: command(tfd.text_src))
    start_btn.pack()

    st = tk_file_dialog.Display()
    st.pack()

    root.wm_minsize(400, 400)
    root.mainloop()


if __name__ == '__main__':
    pick_file(remove)
else:
    pick_file(remove)
