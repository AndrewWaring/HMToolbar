# -*- coding: UTF-8 -*-\n"
from pyrevit import EXEC_PARAMS
from pyrevit import forms, script

doc = __revit__.ActiveUIDocument.Document
if not doc.IsFamilyDocument:
    res = forms.alert("In place families should be avoided.\n"
                  "Only use if absolutely necessary.\n"
                  "If there is no other option please click password.\n",
                  options=["Enter Password",
                           "Cancel"])
    if res == "Cancel":
        EXEC_PARAMS.event_args.Cancel = True
    if res == "Enter Password":
        password = forms.ask_for_string(default='',
                    prompt='Enter Password to use Model in Place',
                    title='Model In Place Password')
        if password == "P4ssw0rd":
            EXEC_PARAMS.event_args.Cancel = False
        else:
            EXEC_PARAMS.event_args.Cancel = True    
    else:
        EXEC_PARAMS.event_args.Cancel = True
else:
   EXEC_PARAMS.event_args.Cancel = False

