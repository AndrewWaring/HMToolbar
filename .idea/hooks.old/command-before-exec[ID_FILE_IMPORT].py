 # -*- coding: UTF-8 -*-\n"
    from pyrevit import EXEC_PARAMS
    from pyrevit import forms, script

    doc = __revit__.ActiveUIDocument.Document

    res = forms.alert("ATTENTION!\n\n"
                      "Les familles insitu sont globalement une mauvaise pratique, "
                      "contrairement aux familles chargeables, elles ont des inconvénients: \n"
                      " - Problèmes d'affichage,\n"
                      " - Pas possible d'identifier son niveau adéquatement,\n"
                      " - La copie va créer un double de l'original,\n"
                      " - Impossible de modéliser de manière paramétrique\n\n"
                      "Voulez-vous vraiment créer une famille in situ?",
                      options=["Valider",
                               "Annuler",
                               "Plus d'information sur les familles in situ"],
                      title="Familles In Situ",
                      footer="BIMONE Hooks")
    if res  == "Valider":
       EXEC_PARAMS.event_args.Cancel = False
       # logging to server
       from hooksScripts import hooksLogger
       hooksLogger("Inplace Component", doc)

    elif res  == "Annuler":
       EXEC_PARAMS.event_args.Cancel = True
    elif res  == "Plus d'information sur les familles in situ":
       EXEC_PARAMS.event_args.Cancel = True
       url = 'https://knowledge.autodesk.com/support/revit-products/learn-explore/caas/CloudHelp/cloudhelp/2016/ENU/Revit-Model/files/GUID-B63B71A6-E8F2-40C9-9CAC-FFB738C431E4-htm.html'
       script.open_url(url)
    else:
       EXEC_PARAMS.event_args.Cancel = True