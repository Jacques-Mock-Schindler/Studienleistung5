# Computernetzwerke

Computernetzwerke ermöglichen die Kommunikation zwischen verschiedenen
Computern. Dies hat neben einem technischen auch einen
gesellschaftlichen Aspekt. Den Gesellschaftlichen Aspekt kann man am
Arabischen Frühling, der Ende 2010 begonnen hat und mit dem Beginn des
Bürgerkrieges in Syrien 2011 mehrheitlich zu einem Stillstand gekommen
ist, zeigen. Das Internet hat mit seinen Kommunikationskanälen die
Organisation der entsprechenden Proteste erst ermöglicht. Ein anderes
Beispiel für die gesellschaftliche Bedeutung von Computernetzwerken ist
aktuell Starlink. Dieses Netzwerk ermöglicht es, in Ländern mit starker
Zensur unter Umgehung von behördlichen Zugangsbeschränkungen
Informationen auszutauschen.

Dies sind meines Erachtens gesellschaftliche Gründe, sich mit den
technischen Aspekten von Computernetzwerken auseinanderzusetzen.  

## Motivation

Zum Einstieg ins Thema wird den Schülerinnen und Schüler ein Artikel mit
dem Titel "Wie China unter Xi das Internet kontrolliert" aus der NZZ vom
24\. Oktober 2022 vorgestellt.  
Daraus ergibt sich die Fragestellung, wie die Verbindungen zwischen
Computern im Internet bewerkstelligt werden. Dies führt zur Besprechung
der IP Adressen und so zum TCP/IP Protokoll.

## Vorausgesetzte Vorkenntnisse

Die SuS 

- sind mit dem binären und dem hexadezimalen Zahlensystem vertraut;
- kennen die Grundzüge der Vergabe von Internetdomains sowie
- das OSI- bzw. IP-Layer-Modell.

## Lernziele

Die SuS können

- die Aufgabe eines DNS-Servers im Zusammenhang mit dem
  Verbindungsaufbau zwischen einem Computer in einem lokalen Netzwerk
  und einer Website im Internet sowie
- den Three-Way Handshake beim Aufbau der Verbindung zwischen Server und
  Client erläutern. Ausserdem können sie
- unter Anleitung Wireshark als Werkzeug für einfache Netzwerkanalysen
  einsetzen. 


## Vorbereitung

Für diese Unterrichtseinheit muss
[Wireshark](https://www.wireshark.org/)
auf den Rechnern der SuS installierst sein. Wireshark ist eine Open
Source Software für die Analyse von Computernetzwerken. In dieser
Unterrichtseinheit wird Wireshark dazu verwendet, die DNS-Anfrage und
den Verbindungsaufbau zu einer bestimmten Website (im Beispiel die
Website der NZZ) zu beobachten.  
Wireshark verfügt über
Installationsprogramme für alle gängigen Betriebssysteme.

## Grobkonzept

- IP Adressen
- OSI Modell / TCP/IP Modell
- NAT Protokoll
- Paketanalyse

## Domain Name System

Wie wird eine Textbasierte `url` in eine IP-Adresse aufgelöst?

Durch DNS-Server. Diese haben fixe IP-Adressen.