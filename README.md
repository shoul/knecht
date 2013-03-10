# KNECHT #

Möglicher Programmname, Vorschläge willkommen.

## KURZFASSUNG ##

Knecht ist ein micro Content Management System (CMS) für
statische Blog Generatoren (SBG) wie zum Beispiel [Acrylamid].
Er soll begrenzt das Bearbeiten und Verwalten von
Blog-Beiträgen durch ein einfache Web-Oberfläche ermöglichen.

## FUNKTIONEN - KISS ##

* ein Knecht verwaltet eine Blog-Instanz
* Liste aller Beiträge anzeigen (drafts oben, order by date ASC)
* einen neuen Beitrag anlegen (MD, RST) (mit Metadaten als Vorlage)
* einen bestehenden Beitrag bearbeiten
* Assets hochladen
* render des Generators triggern (preview, cleancache)
* Änderungen persistieren (commit, push, deploy)

## BESONDERHEITEN / PROBLEME ##

* Blog Sourcen werden im Repo gehalten (git, hg, ...)
** initiales auschecken beim eröffnen einer Session
** ggf. wiederaufnehmen einer Session (pull, merge ...)
** jede zu bearbeitende Datei wir in einem user branch gehalten
** jede Änderung lößt einen commit aus
** finales Abspeichen squashed änderungen
** Änderungen commiten && pushen, ggf bei problemen patches per email verschicken ?
* Pfade (content, static, output) auslesbar (config.py)
* Feedback vom Generator
* Authentifizierung: HTTP Basic Auth?

## LIZENZ ##

BSD 2 clauses

## INSTALL ###

* Eine virtuelle Umgebung anlegen [virutalenv](http://www.virtualenv.org/)
* pip installieren
* `pip install -r requirements.txt`
* `mkdir repos && acrylamid init repos/foo`
* python runserver.py


[Acrylamid]:        https://github.com/posativ/acrylamid/

<!-- vim: set spelllang=de:ft=markdown: -->
