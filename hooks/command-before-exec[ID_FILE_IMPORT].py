# -*- coding: UTF-8 -*-\n"
from pyrevit import EXEC_PARAMS
from pyrevit import forms, script

doc = __revit__.ActiveUIDocument.Document
if not doc.IsFamilyDocument:
    res = forms.alert("Importing DWG will bring in so much mess.\n"
                  "It is highly reccommended you use link DWG.\n"
                  "If there is no other option but to insert please click password.\n",
                  options=["Enter Password",
                           "Cancel"]
                  )
    if res == "Cancel":
        EXEC_PARAMS.event_args.Cancel = True
    if res == "Enter Password":
        password = forms.ask_for_string(default='',
                    prompt='Enter Password to insert DWG',
                    title='DWG Password')
        if password == "P4ssw0rd":
            EXEC_PARAMS.event_args.Cancel = False
        else:
            EXEC_PARAMS.event_args.Cancel = True    
    else:
        EXEC_PARAMS.event_args.Cancel = True
else:
   EXEC_PARAMS.event_args.Cancel = False

