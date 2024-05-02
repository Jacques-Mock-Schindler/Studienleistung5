# Computernetzwerke

Computernetzwerke ermöglichen die Kommunikation zwischen verschiedenen
Computern. In der hier beschriebenen Unterrichtseinheit soll für
Schülerinnen und Schüler nachvollziehbar gezeigt werden, wie diese
Kommunikation auf der Ebene des Verbindungsaufbaus funktioniert. Dies
ist eine sehr technische und abstrakte Betrachtungsweise. Deshalb soll
auch auf die gesellschaftlichen Folgen der Kommunikation zwischen
Computern hingewiesen werden.

In gesellschaftlicher Hinsicht ermöglicht die Kommunikation mit Hilfe
von Computernetzwerken einerseits den freien Austausch von Ideen rund um
die ganze Welt. Sie ermöglicht es auch, dass gesellschaftliche
Strömungen politische Wirkung entfalten können. Ein Beispiel für eine
solche politische Wirkung ist der Arabische Frühling, der Ende 2010
begonnen hat. Zwar ist die Bedeutung computergestützter Kommunikation
für den Arabischen Frühling nicht restlos geklärt, sicher ist aber, dass die
politischen Ereignisse durch Social Media begünstigt worden sind[^1].
Umgekehrt erlauben die technischen Eigenheiten computergestützter
Kommunikation auch Zensurmassnahmen in noch nie dagewesenem Ausmass.

Die vorliegende Unterrichtseinheit wird daher mit einem Zeitungsartikel
zur Great Firewall[^2] eingeleitet werden.

Mit diesem Hinweis auf die gesellschaftliche Bedeutung
computergestützter Kommunikation soll die Motivation für die
Auseinandersetzung mit ihrer technischen Umsetzung geschaffen werde. Ich
erhoffe mir so nicht zu Letzt auch SuS abzuholen, die sich nicht
besonders für technische Konzepte interessieren.

## Lernziele

Mit der vorliegenden Unterrichtseinheit soll erreicht werden, dass die SuS

- die Funktion von IP-Adressen erklären;
- die Aufgabe eines DNS-Servers im Zusammenhang mit dem
  Verbindungsaufbau zwischen einem Computer in einem lokalen Netzwerk
  und einer Website im Internet nachvollziehen;
- den Three-Way Handshake beim Aufbau der Verbindung zwischen Server und
  Client erläutern sowie 
- unter Anleitung Wireshark als Werkzeug für einfache Paketanalysen
  einsetzen

können. 

## Vorausgesetzte Vorkenntnisse

Die SuS 

- sind mit dem binären und dem hexadezimalen Zahlensystem vertraut;
- kennen die Grundzüge der Vergabe von Internetdomains sowie
- das OSI- bzw. IP-Layer-Modell.




## Erforderliche Software bzw. Vorbereitung

Die vorliegende Unterrichtseinheit erfordert als spezielle Software nur
die Installation von 
[Wireshark](https://www.wireshark.org/).
Wireshark ist eine Open
Source Software für die Analyse von Computernetzwerken. In dieser
Unterrichtseinheit wird Wireshark dazu verwendet, die DNS-Anfrage und
den Verbindungsaufbau zu einer bestimmten Website (im Beispiel die
Website der NZZ) zu beobachten.  
Wireshark verfügt über
Installationsprogramme für alle gängigen Betriebssysteme.

Darüber hinaus wird ausschliesslich mit Standardsoftware wie einem
(beliebigen) Browser und dem Terminal gearbeitet.


## Unterrichtsmethode

Für diese Lerneinheit eignet sich eine Mischung aus Lehrgespräch und
Gruppenarbeit. Für die mit Hilfe einer
[Präsentation](slides.html)
zu vermittelnden theoretischen Grundlagen ist ein Lehrgespräch zu
führen, die Bearbeitung der Aufgaben kann wahlweise als Gruppen- oder
Einzelarbeit durchgeführt werden.

Im Unterricht wird man von Seiten der SuS gelegentlich mit dem Vorwurf
konfrontiert, dass die im Unterricht zur Anwendung kommenden Methoden im
richtigen Leben nicht verwendet würden. Aus diesem Grund wird mit echten
Werkezeugen wie Wireshark gearbeitet und darauf verzichtet
unterrichtsspezifische Software einzusetzen.  
Dies im vollen Bewusstsein, dass Wireshark für den hier geplanten
Einsatz viel zu viele Funktionen aufweist. Dies wird in den geplanten
Aufgaben allerdings dadurch aufgefangen, dass die SuS beim Einsatz von
Wireshark sehr eng geführt werden.

Die Aufgaben können unterschiedlich detailliert gelöst werden. Der
Detaillierungsgrad der Bearbeitung ermöglicht es, besonders
interessierten SuS oder auch speziell engagierten Klassen die
Gelegenheit zur Vertiefung zu bieten.

Für die vorliegende Unterrichtseinheit werden die folgenden Dokumente
und Dateien verwendet:

- Wie China unter Xi das Internet kontrolliert, NZZ vom 24. Oktober 2022
  (PDF)
- ascii-table.pdf
- ping_nzz.pcapng 
- dns_anfrage_nzz.pcapng
- handshake_nzz.pcapng
- kariertes Notizpapier (vorzugsweise 5mm, von den SuS selber
  mitzubringen)
- Präsentation (slides.html)

## Aufgaben mit Lösungen

### Sensibilisierungsaufgabe

Zum Einstieg ins Thema wird der Artikel 
[«Wie China unter Xi das Internet
kontrolliert»](https://www.nzz.ch/technologie/wie-china-unter-xi-das-internet-kontrolliert-ld.1708411)
aus der NZZ vom 24. Oktober 2022 gelesen (der Text findet sich als PDF
in den Unterlagen).

Bei der Besprechung soll dann insbesondere auf den
Abschnitt 

>Die Regierung kann bestimmte URL sperren, etwa nzz.ch, die wie jene
>praktisch aller grossen westlichen Medien in China verboten ist. Sie
>kann auch den Zugang zu Websites verhindern, indem sie den Datenverkehr
>manipuliert. Wenn man nämlich die Adresse einer Website im Browser
>eintippt, liefern Server des sogenannten Domain Name System (DNS) dazu
>die passende numerische Internetprotokoll-Adresse (IP) – ausser die
>Regierung leitet die Anfrage zu einer anderen IP weiter. Sie kann auch
>einfach die zugrunde liegenden IP-Adressen sperren. 

im letzten Drittel des Artikels hingewiesen werden.

Aus diesem Abschnitt ergibt sich die Frage, wie der Aufbau einer
Verbindung zu einer bestimmten Website im Detail abläuft.

### Experiment 1: ping nzz.ch

*Anweisungen:*

1. Terminal öffnen
2. ping nzz.ch
3. Besprechung der Ausgabe

Die Anzeige im Terminal der SuS sieht nach dem `ping` im Wesentlichen
folgendermassen aus:

```txt
Ping wird ausgeführt für nzz.ch [194.40.217.80] mit 32 Bytes Daten:
Antwort von 194.40.217.80: Bytes=32 Zeit=7ms TTL=55
Antwort von 194.40.217.80: Bytes=32 Zeit=6ms TTL=55
Antwort von 194.40.217.80: Bytes=32 Zeit=9ms TTL=55
Antwort von 194.40.217.80: Bytes=32 Zeit=9ms TTL=55

Ping-Statistik für 194.40.217.80:
    Pakete: Gesendet = 4, Empfangen = 4, Verloren = 0
    (0% Verlust),
Ca. Zeitangaben in Millisek.:
    Minimum = 6ms, Maximum = 9ms, Mittelwert = 7ms
```

*Auswertung (Besprechung):*

Für eine erste Auswertung wird nur Beschrieben, was in der Ausgabe zu
sehen ist.

Dem Server nzz.ch wird ein Datenpaket im Umfang von 32 Bytes geschickt.
Der Server nzz.ch hat offensichtlich eine zahlenbasierte Adresse
`[194.40.217.80]`. Es wurden insgesamt 4 Pakete verschickt und keines
ist verlorengegangen. Die Reaktionszeit lag zwischen 6 und 9ms (7.75ms
im Mittel; die Berechnung wurde trunkiert).

Daraus ergeben sich die folgenden beiden Fragen:

- Was ist eine IP-Adresse?
- Woher kommt die IP-Adresse für nzz.ch?

### IP-Adressen

Wann gehen uns die IP-Adressen aus?  
Berechnen Sie, wie viele IPv4-Adressen grundsätzlich zur
Verfügung stehen.

*Musterlösung*

$$
11111111\ 11111111\ 11111111\ 11111111_B = 2^{32} = 4'294'967'296_D
$$

Berechnen Sie, wie viele IPv6-Adressen grundsätzlich zur Verfügung
stehen. 

*Musterlösung*

$$
2^{128}
$$

Anschliessend an die Berechnung kann kursorisch auf das NAT Protokoll
eingegangen werden. Damit soll nur gezeigt werden, dass auch IPv4 mehr
als $2^{32}$ Adressen ermöglicht.

### Kontrolle der eigenen DNS-Einstellungen

1. Einstellungen öffnen (Windows > Einstellungen)
2. Netzwerk und Internet
3. Eigenschaften der aktuellen Schnittstelle (wahrscheinlich WLAN)
4. Scrollen bis IPv4-DNS-Server

*Auswertung (Besprechung):*

Als erstes ist festzustellen, was für DNS-Server die SuS eingestellt
haben. Gegebenenfalls können die Einstellungen manuell angepasst werden.
Wichtig ist darauf hinzuweisen, dass eine unverschlüsselte DNS-Abfrage
ein Risiko darstellt. Die im Screenshot dargestellte Lösung ist das
Resultat der Verwendung von `Cisco AnyConnect Secure Mobility Client`.
Gewisse Unternehmen (zB. die
UNI Fribourg) verlangen dessen Verwendung als VPN Client.
Dieser führt dazu, dass in der Registry ein Eintrag vorgenommen wird,
welcher die Verwendung von https für die DNS-Anfrage verhindert.

### Installation von Wireshark

1. Herunterladen des Installers
2. Installieren von Wireshark

*Anmerkung:*

Wireshark ist für die kommenden Aufgaben erforderlich. Falls Wireshark
schon installiert ist, entfällt diese Aufgabe.


### Aufzeichnung des Aufrufs von nzz.ch

1. Wireshark öffnen
2. Zutreffende Schnittstelle (wahrscheinlich WLAN) auswählen
3. Aufzeichnung starten
4. Browser öffnen
5. nzz.ch aufrufen
6. Aufzeichnung anhalten 
7. Aufzeichnung speichern

*Anmerkung:*

Eine Besprechung erübrigt sich hier grundsätzlich. Die so erstellte
Datei bildet lediglich die Grundlage für die kommenden Aufgaben.

Falls man sich auf die Analyse der Pakete konzentrieren will, ohne Zeit
für das herausfiltern der relevanten Pakete zu verbrauchen, kann auf die
mitgelieferten bereites gefilterten Wireshark-Dateien abgestellt werden.

### Suche nach der DNS-Anfrage für nzz.ch

(*dns_anfrage_nzz.pcapng*)

1. Anzeigefilter `dns.qry.name == "www.nzz.ch" setzten
2. Anfrage auswählen

Die Zusammenfassung sieht im wesentlichen folgendermassen aus: 

```txt
Frame 1: 70 bytes on wire (560 bits), ...
Ethernet II, ...
Internet Protocol Version 4, Src: 192.168.1.107, Dst: 9.9.9.9
User Datagram Protocol, Src Port: 57802, Dst Port: 53
Domain Name System (query)
```

*Auswertung (Besprechung):*

Die erste Zeile gibt eine Zusammenfassung des ausgewählten Paketes. Aus
darstellerischen Gründen wurde der Inhalt abgeschnitten.

Die zweite Zeile entspricht dem ersten Layer des TCP/IP-Layer Modells.
Der Network Access Layer gibt Auskunft, wie physikalisch die Verbindung
zum Internet hergestellt wird. Dies ist nicht Gegenstand der
vorliegenden Aufgabe.

Die dritte Zeile entspricht dem Network Layer. Auf diesem Layer sieht
man, welche IP-Adressen miteinander kommunizieren.

Die vierte Zeile entspricht dem Transport Layer. Hier werden die
konkreten Dienste über die entsprechenden Ports angesprochen. DNS "hört"
am Port 53. Der Port des Absenders wird willkürlich im Bereich
ausserhalb der sog. 
["well known
ports"](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers#Well-known_ports)
gewählt.

Die letzte Zeile fasst die eigentliche DNS Anfrage zusammen. Die
detaillierte Besprechung erfolgt in der nächsten Aufgabe.

### Die DNS-Anfrage für nzz.ch im Detail

(*dns_anfrage_nzz.pcapng, ascii-table.pdf*)

- maximale Auffaltung der letzten Zeile

Der aufgefaltete Teil der letzten Zeile sieht im Wesentlichen
folgendermassen aus:

```txt
...
Domain Name System (query)
    Transaction ID: 0x3a4c
    Flags: 0x0100 Standard query
        0... .... .... .... = Response: Message is a query
        .000 0... .... .... = Opcode: Standard query (0)
        .... ..0. .... .... = Truncated: Message is not truncated
        .... ...1 .... .... = Recursion desired: Do query recursively
        .... .... .0.. .... = Z: reserved (0)
        .... .... ...0 .... = Non-authenticated data: Unacceptable
    Questions: 1
    Answer RRs: 0
    Authority RRs: 0
    Additional RRs: 0
    Queries
        www.nzz.ch: type A, class IN
            Name: www.nzz.ch
            [Name Length: 10]
            [Label Count: 3]
            Type: A (1) (Host Address)
            Class: IN (0x0001)
    [Response In: 2]
```

beziehungsweise in hexadezimaler Darstellung:

```txt
3a 4c 01 00 00 01 00 00 
00 00 00 00 03 77 77 77 
03 6e 7a 7a 02 63 68 00 
00 01 00 01

```

*Auswertung (Besprechung):*

Die Codierung als Binärcode kann auf kariertem Papier erfolgen. Dies
ermöglicht die Darstellung in einer 16 Spalten breiten Tabelle. Die
Tabelle kann dann Zeile für Zeile kommentiert werden.

Die hexadezimale Darstellung wurde so ausgewählt, dass sie im Umfang der
ausgefalteten Textdarstellung entspricht. Sie wird dazu verwendet,
nachzuvollziehen, wie die Anfrage der schematischen Darstellung aus 
Fall, Kevin R., und W. Richard Stevens, TCP/IP illustrated, volume 1:
The Protocols, 2nd ed., Addison-Wesley professional computing series, 
Upper Saddle River, NJ: Addison-Wesley, 2012, p. 521, entspricht.

Als erstes ist die Transaction ID in eine Binärzahl umzurechnen.

$$
0x3a4c = 0b0011101001001100
$$

Die Transaction ID gibt ergibt nur mit zwei führenden Nullen 16 Stellen.
Das steht jedoch dem Schema nicht entgegen.

Die zweite Zeile sind die verschiedenen Flags:

$$
0x0100 = 0b0000000100000000
$$

Einzelne Bits sind hier nicht gesetzt (zu erkennen an den Punkten in der
Textdarstellung), weshalb eine Null eingesetzt wurde. So sind es genau
16 Bits.

Die Zeile mit dem Fragezähler hat den Wert 1 was

$$
0b0000000000000001
$$ 

entspricht.

Da noch keine Antwort erfolgt ist, ist der Wert der entsprechenden
Zeile(n) 0.

$$
0b0000000000000000
$$

$$
0b0000000000000000
$$

$$
0b0000000000000000
$$

Die Codierung der Adresse erstreckt sich über mehrere Zeilen (für jedes
Zeichen stehen 8 Bit zur Verfügung):

```txt
00000011 01110111
01110111 01110111
00000011 01101110
01111010 01111010
00000010 01100011
01101000 00000000
00000000 00000001 
00000000 00000001

```

Abgeglichen mit der ASCII-Tabelle ergibt sich daraus das folgende Bild:

| Code | Zeichen |
| ---: | :---: |
| 00000011 | ETX |
| 01110111 | w |
| 01110111 | w |
| 01110111 | w |
| 00000011 | ETX |
| 01101110 | n |
| 01111010 | z |
| 01111010 | z |
| 00000010 | STX |
| 01100011 | c |
| 01101000 | h |


Die ganze Anfrage, beginnend bei der Transaction ID in sieht in
Binärcodierung folgendermassen aus:

```txt
00111010 01001100
00000001 00000000
00000000 00000001
00000000 00000000
00000000 00000000
00000000 00000000 
00000011 01110111 
01110111 01110111 
00000011 01101110 
01111010 01111010 
00000010 01100011 
01101000 00000000 
00000000 00000001 
00000000 00000001 
```

### Die DNS-Antwort für nzz.ch

(*dns_anfrage_nzz.pcapng*)

1. Auswahl des Antwortpakets
2. Maximale Ausfaltung der untersten Zeile

Daraus ergibt sich die folgende Ansicht:

```txt
Frame 2: ...
Ethernet II, ...
Internet Protocol Version 4, Src: 9.9.9.9, Dst: 192.168.1.107
User Datagram Protocol, Src Port: 53, Dst Port: 57802
Domain Name System (response)
    Transaction ID: 0x3a4c
    Flags: 0x8180 Standard query response, No error
        1... .... .... .... = Response: Message is a response
        .000 0... .... .... = Opcode: Standard query (0)
        .... .0.. .... .... = Authoritative: Server is not an authority for domain
        .... ..0. .... .... = Truncated: Message is not truncated
        .... ...1 .... .... = Recursion desired: Do query recursively
        .... .... 1... .... = Recursion available: Server can do recursive queries
        .... .... .0.. .... = Z: reserved (0)
        .... .... ..0. .... = Answer authenticated: Answer/authority portion was not authenticated by the server
        .... .... ...0 .... = Non-authenticated data: Unacceptable
        .... .... .... 0000 = Reply code: No error (0)
    Questions: 1
    Answer RRs: 1
    Authority RRs: 0
    Additional RRs: 0
    Queries
        www.nzz.ch: type A, class IN
            Name: www.nzz.ch
            [Name Length: 10]
            [Label Count: 3]
            Type: A (1) (Host Address)
            Class: IN (0x0001)
    Answers
        www.nzz.ch: type A, class IN, addr 194.40.217.80
            Name: www.nzz.ch
            Type: A (1) (Host Address)
            Class: IN (0x0001)
            Time to live: 300 (5 minutes)
            Data length: 4
            Address: 194.40.217.80
    [Request In: 1]
    [Time: 0.005354000 seconds]

```

*Auswertung (Besprechung):*

Die Transaction ID stimmt mit jener der Anfrage überein, also handelt es
sich um das Paket, das zur Anfrage gehört.

Das Bit mit dem Antwort-Flag ist auf 1 gesetzt, es ist die Antwort.

Der Error-Code ist 0, die Antwort ist ohne Fehler erfolgt.

Die Antwort lautet der Server der NZZ hat die IPv4-Adresse
194.40.217.80.

### Three-Way Handshake

1. Filter ip.addr == 194.40.217.80
2. Absolute Sequenznummern einstellen (Einstellungen > Protokolle > TCP
   \> Kontrollkästchen "relative Sequenznummern" deaktivieren)
3. Suche nach Paketen mit dem Flag [SYN] bzw. [ACK]

Reduziert ergibt sich daraus das folgende Bild:

```txt
192.168.1.107	194.40.217.80	TCP	66	55531 → 443 [SYN] Seq=2234328046 ...
194.40.217.80	192.168.1.107	TCP	66	443 → 55531 [SYN, ACK] Seq=657467626 Ack=2234328047 ...
192.168.1.107	194.40.217.80	TCP	54	55531 → 443 [ACK] Seq=2234328047 Ack=657467627 ...
```

*Auswertung (Besprechung):*

Die Sequenznummern werden tatsächlich gemäss dem Schema des Three-Way
Handshake hochgezählt.

Damit ist die Verbindung zur Website www.nzz.ch hergestellt.


---

[^1]: Wikipedia: Social media's role in the Arab Spring,
    https://en.wikipedia.org/wiki/Social_media%27s_role_in_the_Arab_Spring,
    besucht am 2. Mai 2024.

[^2]: Wikipdia: Great Firewall,
    https://en.wikipedia.org/wiki/Great_Firewall, besucht am 2. Mai 2024.