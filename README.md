# KNECHT #

Möglicher Programmname, Vorschläge willkommen.

## KURZFASSUNG ##

Knecht ist ein einfaches Content Management System (CMS) für
statische Blog Generatoren (SBG) wie [Acrylamid].
Er soll begrenzt das Bearbeiten und Verwalten von
Blog-Beiträgen durch ein einfache Web-Oberfläche ermöglichen.

## FUNKTIONEN - KISS ##

* ein Knecht verwaltet eine Blog-Instanz
* Liste aller Beiträge anzeigen (drafts oben, order by date ASC)
* einen neuen Beitrag anlegen (MD, RST) (+Metadaten als Vorlage)
* einen bestehenden Beitrag bearbeiten
* Assets hochladen
* render des Generators triggern (preview, cleancache)
* Änderungen persistieren (commit, push, deploy)

## BESONDERHEITEN / PROBLEME ##

* Blog Sourcen werden im Repo gehalten (git, hg, ...) (auf gleichem Server)
** initiales auschecken beim eröffnen einer Session
** ggf. wiederaufnehmen einer Session (pull, merge ...) ?
** Änderungen commiten && pushen, ggf bei problemen patches per email verschicken ?
* Pfade (content, static, output) auslesbar (config.py)
* Feedback vom Generator
* Authentifizierung: HTTP Basic Auth?

## LIZENZ ##

BSD 2 clauses


[Acrylamid]:        https://github.com/posativ/acrylamid/

<!-- vim: set spelllang=de:ft=markdown: -->
