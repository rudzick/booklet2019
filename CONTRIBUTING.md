# Mithelfen

Da es sich um ein Programmheft für eine deutsche Konferenz handelt, schreiben wir im Bugtracker auf Deutsch und sparen uns das Englisch.

## Was getan werden muss

Das Programmheft muss am 25. Februar 2019 im Druck sein. Falls Du mithelfen möchtest und Fragen hast, ist es am Besten, Nakaner via IRC (bei OFTC) zu kontaktieren. Die Liste der zu erledigenden Tätigkeiten findest du im Issue-Tracker.

Die Erstellung eines Programmhefts besteht aus den folgenden Schritten:

* Code vom Vorjahr kopieren
  * Einbindung der Quellcodedateien für die Wochentage und ihre Tagestabellen in master.tex auskommentieren
  * Jahreszahl anpassen
  * Makros für Räume an die Namen der Räume anpassen
  * Konferenzlogo aktualisieren
  * Logo des alten durch den neuen Gastgeber ersetzen
  * Vorwort aktualisieren
  * Inhaltsverzeichnis ggf. aktualisieren
  * Impressum aktualisieren
* mit pretalx2tex.py die Vortragskurzbeschreibungen in LaTeX konvertieren
* Die folgenden Schritte können parallel erfolgen:
  * mittwoch.tex, donnerstag.tex, freitag.tex einbinden und schauen, dass es kompiliert
  * Sponsorenlogos auf Druckbarkeit prüfen, sonst nach druckbarer Alternative googlen. Lieber selber vektorisieren als eine E-Mail zu schreiben und zu warten. ;-)
  * Sponsorentexte auf Länge prüfen, ansonsten E-Mail mit Kürzungsvorschlag (die ersten n Zeichen + nächtes Wort + `\dots`) und nächsten Arbeitstag als Frist.
* Die folgenden Schritte können parallel erfolgen:
  * Workshopseiten setzen (das ist eine Fummelarbeit, damit das auf 4 Seiten passt)
  * Tagestabellen setzen (nochmal Fummelarbeit, um Platz zu sparen)
  * Kurzbeschreibungen setzen, Lightning Talks nicht vergessen
  * ggf. Sonderseiten setzen (Social Event, OSM-Samstag, …)
  * Sponsorenboxen für die Einbindung vorbereiten (TeXen, aber noch nicht auf überlange Zeilen prüfen)
  * Kartenseiten und Rückseiten
  * ggf. Gebäudeplan
* Lücken mit Sponsorenboxen füllen, den Rest an das Ende stellen. Silbersponsoren bevorzugt nach vorne, Mediasponsoren bevorzugt nach an den Schluss. Übrige Boxen auf "Werbungsseiten" nach den Vortragsbeschreibungen. Durch Anpassung der Größe der Sponsorenlogos, geschickten Zeilenumbruch und `\enlargethispage` etwas Platz schinden/sparen.
* Nochmal über alles schauen.
* kontrollieren, dass alle Vorträge und alle Sponsoren enthalten sind
* Liste der Mitwirkenden im Impressum aktualisieren
* Auf der Konferenz-Mailingliste zum Lektorat aufrufen (Frist max. 24 h), falls weniger als zwei bislang unbeteiligte Freiwillige zur Hand sind. 


## TeXnisches

Unsere Dateien sind in UTF-8 kodiert. Hier noch ein paar Konventionen bzw. Dinge, die während des Setzens der Vortragsbeschreibungen und Sponsorentexte getan werden müssen:

* In zusammengesetzte Abkürzungen gehört ein halbes geschütztes Leerzeichen, `z.\,B.`
* Akronyme (Abkürzungen mit mindestens zwei aufeinanderfolgenden Großbuchstaben) werden mit \acro{QGIS} gesetzt. (umstritten)
* Anführungszeichen "` und "'
* Hervorhebungen sparsam und nur als `\emph{}`
* zusammengesetzte Substantive mit Bindestrichen dazwischen als `OpenStreetMap"=Daten` schreiben, damit LaTeX auch an anderen Stellen als dem Bindestrich trennen kann. Unsere Zeilen sind nämlich recht kurz.
* Bei den Kurzbeschreibungen bitte auf Leute Rücksicht nehmen, die meinen, dass man in Markdown (in Pretalx) Absätze mit einem Zeilenumbruch macht (zwei wären richtig und sind es auch in LaTeX).

Und sonst:

* Zeilen sollten im Quellcode max. 100 Zeichen lang sein.
