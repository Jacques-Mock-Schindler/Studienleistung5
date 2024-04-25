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
in den Unterlagen). Bei der Besprechung soll dann insbesondere auf den
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

### Aufzeichnung der DNS-Abfrage

1. Terminal öffnen
2. Wireshark öffnen
3. Aufzeichnung starten
4. nzz.ch pingen
5. Aufzeichnung anhalten 
6. Anzeigefilter dns setzten

Das ergibt die folgende Zusammenfassung:

```txt
No.  Time      Source           Destination      Protocol  Length  Info
13   6.313849  10.134.61.184    193.135.142.246  DNS       56      Standard query 0x9e0b A www.nzz.ch
14   6.371778  193.135.142.246  10.134.61.184    DNS       72      Standard query response 0x9e0b A www.nzz.ch A 194.40.217.80
```

Basierend auf dieser Zusammenfassung kann das Mapping von URL nach der
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
Die SuS sollen Ausrechnen, wie viele IPv4-Adressen grundsätzlich zur
Verfügung stehen.

$$
11111111\ 11111111\ 11111111\ 11111111_B = 2^{32} = 4'294'967'296_D
$$

Als zweite Aufgabe können die SuS den Adressraum der IPv6 Adressen
berechnen.

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

Das Listing kann dazu verwendet werden, das OSI-Layer-Modell zu
repetieren und dem TCP/IP-Layer Modell gegenüberzustellen.  

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

*Aufgabe:* Ordnen Sie dieses Listing dem Prinzipschema einer DNS-Anfrage zu.

## Grobkonzept

- IP Adressen
- OSI Modell / TCP/IP Modell
- NAT Protokoll
- Paketanalyse

## Domain Name System

Wie wird eine Textbasierte `url` in eine IP-Adresse aufgelöst?

Durch DNS-Server. Diese haben fixe IP-Adressen.