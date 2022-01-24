
C:\>python
      Python 2.4.2 (#67, Sep 28 2005, 12:41:11) [MSC v.1310 32 bit (Intel)] on win32
      Type "help", "copyright", "credits" or "license" for more information.
(1)   >>> from pywinauto import application
(2)   >>> app = application.Application()
(3)   >>> app.start("Notepad.exe")
      <pywinauto.application.Application object at 0x00AE0990>
(4)   >>> app.UntitledNotepad.draw_outline()
(5)   >>> app.UntitledNotepad.menu_select("Edit -> Replace")
(6)   >>> app.Replace.print_control_identifiers()
        Control Identifiers:

        Dialog - 'Replace'    (L179, T174, R657, B409)
        ['ReplaceDialog', 'Dialog', 'Replace']
        child_window(title="Replace", class_name="#32770")
           |
           | Static - 'Fi&nd what:'    (L196, T230, R292, B246)
           | ['Fi&nd what:Static', 'Fi&nd what:', 'Static', 'Static0', 'Static1']
           | child_window(title="Fi&nd what:", class_name="Static")
           |
           | Edit - ''    (L296, T226, R524, B250)
           | ['Fi&nd what:Edit', 'Edit', 'Edit0', 'Edit1']
           | child_window(class_name="Edit")
           |
           | Static - 'Re&place with:'    (L196, T264, R292, B280)
           | ['Re&place with:', 'Re&place with:Static', 'Static2']
           | child_window(title="Re&place with:", class_name="Static")
           |
           | Edit - ''    (L296, T260, R524, B284)
           | ['Edit2', 'Re&place with:Edit']
           | child_window(class_name="Edit")
           |
           | CheckBox - 'Match &whole word only'    (L198, T304, R406, B328)
           | ['CheckBox', 'Match &whole word onlyCheckBox', 'Match &whole word only', 'CheckBox0', 'CheckBox1']
           | child_window(title="Match &whole word only", class_name="Button")
           |
           | CheckBox - 'Match &case'    (L198, T336, R316, B360)
           | ['CheckBox2', 'Match &case', 'Match &caseCheckBox']
           | child_window(title="Match &case", class_name="Button")
           |
           | Button - '&Find Next'    (L536, T220, R636, B248)
           | ['&Find Next', '&Find NextButton', 'Button', 'Button0', 'Button1']
           | child_window(title="&Find Next", class_name="Button")
           |
           | Button - '&Replace'    (L536, T254, R636, B282)
           | ['&ReplaceButton', '&Replace', 'Button2']
           | child_window(title="&Replace", class_name="Button")
           |
           | Button - 'Replace &All'    (L536, T288, R636, B316)
           | ['Replace &AllButton', 'Replace &All', 'Button3']
           | child_window(title="Replace &All", class_name="Button")
           |
           | Button - 'Cancel'    (L536, T322, R636, B350)
           | ['CancelButton', 'Cancel', 'Button4']
           | child_window(title="Cancel", class_name="Button")
           |
           | Button - '&Help'    (L536, T362, R636, B390)
           | ['&Help', '&HelpButton', 'Button5']
           | child_window(title="&Help", class_name="Button")
           |
           | Static - ''    (L196, T364, R198, B366)
           | ['ReplaceStatic', 'Static3']
           | child_window(class_name="Static")
(7)   >>> app.Replace.Cancel.click()
(8)   >>> app.UntitledNotepad.Edit.type_keys("Hi from Python interactive prompt %s" % str(dir()), with_spaces = True)
      <pywinauto.controls.win32_controls.EditWrapper object at 0x00DDC2D0>
(9)   >>> app.UntitledNotepad.menu_select("File -> Exit")
(10)  >>> app.Notepad.DontSave.click()
      >>>