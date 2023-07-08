#Documentatie DRIP

Mijn doel met dit project is om een database op te zetten gebaseerd op mijn kledingkast/garderobe.
De database heeft een aantal variabelen;

De database server is Microsoft SQL en word beheerd door SMSS.

De items in de database zullen via een lokale HTML website te zien zijn (wellicht online na eerste prototype)
De website zal gerunt worden met HTML en CSS, met een Python (?) script om de database te bereiken. Om de data daadwerkelijk te laten zien op de website zal JavaScript gebruikt worden (denk ik)

Log
MYSQL geeft problemen, MSSQL had herinstallatie nodig i.v.m User Login problemen.
Node JS had problemen met het verbinden met de server met gegeven inloggegevens, tevens stond TCP/IP uit. Nu een fresh install om te kijken of dat zal werken.
Javascript brengt teveel problemen (ODBC Error), verder met Python + Flask
8 Juli 2023: Doorgegaan met lokale applicatie, Database via SMSS, voor python communicator gebruik ik PYODBC. Nu nog een klein basis programma om ALLE data op te halen, en netjes in de CLI te tonen.
8 juli 2023: Ik heb de Jinja2 Module gebruikt om de data die uit de database word gehaald te verwerken en the injecteren in een HTML File (rendered_content, die de HTML template haalt van Index.html) De hoofdpagina van de webpagina is nu Main.htnk.
