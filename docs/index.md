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
- unter Anleitung Wireshark als Werkzeug für einfache Paketanalysen
  einsetzen. 


## Erforderliche Software bzw. Vorbereitung

Für diese Unterrichtseinheit muss
[Wireshark](https://www.wireshark.org/)
auf den Rechnern der SuS installierst sein. Wireshark ist eine Open
Source Software für die Analyse von Computernetzwerken. In dieser
Unterrichtseinheit wird Wireshark dazu verwendet, die DNS-Anfrage und
den Verbindungsaufbau zu einer bestimmten Website (im Beispiel die
Website der NZZ) zu beobachten.  
Wireshark verfügt über
Installationsprogramme für alle gängigen Betriebssysteme.

## Aufgaben

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


### Aufzeichnung ping nzz.ch

1. Terminal öffnen
2. Wireshark öffnen
3. Zutreffende Schnittstelle (wahrscheinlich WLAN) auswählen
4. Aufzeichnung starten
5. nzz.ch pingen
6. Aufzeichnung anhalten 
7. Anzeigefilter dns setzten

Das ergibt eine Zusammenfassung, die im Wesentlichen folgendermassen
aussieht (die entsprechend gefilterte 
[Wireshark-Datei](../data/wireshark/ping_nzz.pcapng)
sich in der Dateiablage):

```txt
Source           Destination      Protocol  Length  Info
10.134.61.184    193.135.142.246  DNS       56      Standard query 0x9e0b A www.nzz.ch
193.135.142.246  10.134.61.184    DNS       72      Standard query response 0x9e0b A www.nzz.ch A 194.40.217.80
```

*Auswertung (Besprechung):*

Für die Darstellung wurde die Paketnummer und die Zeit abgeschnitten.  

Für eine erste Auswertung wird nur besprochen, was hier zu sehen ist.

Das erste Paket wurde von einem Computer mit der IP-Adresse
10.134.61.184 an einen Computer mit der IP-Adresse 193.135.142.246
verschickt. Das verwendete Protokoll ist *DNS* und das Paket beinhaltet
eine Anfrage. Basierend auf dieser Zusammenfassung kann das Mapping von
URL nach der
IP-Adresse besprochen werden.  
Gleichzeitig bietet die Zusammenfassung die Möglichkeit, auf die
verschiedenen DNS-Server einzugehen und Charakteristika verschiedener
Anbieter zu besprechen. In der vorliegenden Beispielzusammenfassung
wurde die Verbindung zum Internet mit einem Mobilfunk Modem hergestellt.
Der DNS-Server ist deshalb der voreingestellte Server der Swisscom.  
Man kann an dieser Stelle allerdings auch auf die Netzwerkeinstellungen
im allgemeinen eingehen und den SuS zeigen, wie diese gegebenenfalls
anzupassen wären.

### IP-Adressen

Wann gehen uns die IP-Adressen aus?  
Berechnen Sie, wie viele IPv4-Adressen grundsätzlich zur
Verfügung stehen.

$$
11111111\ 11111111\ 11111111\ 11111111_B = 2^{32} = 4'294'967'296_D
$$

Berechnen Sie, wie viele IPv6-Adressen grundsätzlich zur Verfügung
stehen. 

$$
2^{128}
$$

Anschliessend an die Berechnung kann kursorisch auf das NAT Protkoll
eingegangen werden. Damit soll nur gezeigt werden, dass auch IPv4 mehr
als $2^{32}$ Adressen ermöglicht.

### Analyse der DNS-Anfrage (Überblick)

Als Vorbereitung des nächsten Analyseschrittes öffnen die SuS die
Anfrage an den DNS-Server. Dies folgt zu einer Ansicht, welche im
Wesentlichen wie das folgende Listing aussieht.

```txt
Frame 13: 56 bytes on wire (448 bits), 56 bytes captured (448 bits) on interface \Device\NPF_{F7C8A86C-E9D7-4080-B7F6-EB45CD1446B6}, id 0
Raw packet data
Internet Protocol Version 4, Src: 10.134.61.184, Dst: 193.135.142.246
User Datagram Protocol, Src Port: 54631, Dst Port: 53
Domain Name System (query)
```

Als erstes wird Anhand des obigen Listings das OSI-Layer-Modell 
repetiert und dem TCP/IP-Layer Modell gegenübergestellt.  

![Gegenüberstellung OSI- bzw.
TCP/IP-Modell](../data/images/layer_modell.png)

Quelle: https://www.geeksforgeeks.org/tcp-ip-model/; zugegriffen am 25.
April 2024.

### Analyse der DNS-Anfrage (Details)

Die SuS sollen die DNS-Anfrage so weit wie möglich Auffalten.

```txt
Domain Name System (query)
    Transaction ID: 0x9e0b
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
    [Response In: 14]

```

```hex
41 f8 01 00 00 01 00 00
00 00 00 00 03 77 77 77
03 6e 7a 7a 02 63 68 00
00 01 00 01
```

Für die Auswertung der DNS-Anfrage steht ein Arbeitsblatt als
Hilfsmittel zur Verfügung. Das Arbeitsblatt entspricht in seinem Aufbau
der Darstellung aus Fall, Kevin R., und W. Richard Stevens. TCP/IP
illustrated, volume 1:The Protocols. 2nd ed. Addison-Wesley professional
computing series. Upper Saddle River, NJ: Addison-Wesley, 2012, page
521. 

Die konkrete Aufgabe für die SuS lautet "Übertragen Sie die DNS-Antrage
als Bitfolge in die Tabelle auf dem Arbeitsblatt."

Die Interpretation der Anfrage auf Stufe einzelner Bit ist eine mögliche
Differenzierung. 


*Aufgabe:* Ordnen Sie dieses Listing dem Prinzipschema einer DNS-Anfrage zu.

## Grobkonzept

- IP Adressen
- OSI Modell / TCP/IP Modell
- NAT Protokoll
- Paketanalyse

## Domain Name System

Wie wird eine Textbasierte `url` in eine IP-Adresse aufgelöst?

Durch DNS-Server. Diese haben fixe IP-Adressen.