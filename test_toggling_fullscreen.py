#!/usr/bin/env python

# test gtk application for toggling fullscreen or windowed mode
# Raspberry Pi OS (32-bit)
# Python 2.7.16

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="toggling fullscreen or windowed mode")
        self.connect("delete-event", Gtk.main_quit)
        self.connect("key-press-event",self.on_key_press_event)
        self.connect("realize", self.on_realize)
        # set window position
        self.set_position(Gtk.WindowPosition.CENTER)
        # set base window background color
        self.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse("#000000"))
        # set default window size
        self.set_default_size(640, 480)
        # fullscreen toggling variable
        self.fullscreen_toggler = True
        # hide mouse pointer toggling variable
        self.mousePointer_toggler = False

    def on_realize(self, widget, data=None):
        # must be called after the realization of the display
        self.updateDisplay()

    def on_key_press_event(self, widget, event):
        if event.keyval == Gdk.KEY_F11:
            self.fullscreen_toggler = not self.fullscreen_toggler
            self.updateDisplay()
        else:
            pass

    def updateDisplay(self):
        self.fulscreenMode()
        self.hideShowMousePointer()

    # function to show app in fullscreen
    def fulscreenMode(self):
        # show in fullscreen and hide mouse pointer
        if self.fullscreen_toggler == True:
            self.fullscreen()
            self.mousePointer_toggler = True
        # show in windowed mode and show mouse pinter
        elif self.fullscreen_toggler == False:
            self.unfullscreen()
            self.mousePointer_toggler = False
        else:
            pass

    # function to hide or show mouse pointer
    # must be called after the realization of the display
    def hideShowMousePointer(self):
        # hide mouse pointer
        if self.mousePointer_toggler == True:
            display = self.get_display()
            cursor = Gdk.Cursor.new_for_display(display, Gdk.CursorType.BLANK_CURSOR)
            self.get_window().set_cursor(cursor)
        # show mouse pointer
        elif self.mousePointer_toggler == False:
            display = self.get_display()
            cursor = Gdk.Cursor.new_for_display(display, Gdk.CursorType.TOP_LEFT_ARROW)
            self.get_window().set_cursor(cursor)
        else:
            pass

if __name__ == "__main__":
    win = MyWindow()
    win.show_all()
    Gtk.main()