# Python: Variablen und Datentypen

## Python Grundlagen
Ausgaben wir in der letzten Aufgabe können recht kompliziert in der Syntax sein. Daher gibt es einen einfacheren Weg, Ausgaben mit Variablen zu erzeugen, den sogenannten f-String:

```
zahl1 = float(input("Zahl 1: "))
zahl2 = float(input("Zahl 2: "))
print(f"Das Ergebnis der Addition von {zahl1} + {zahl2} ergibt {zahl1+zahl2}")
```

## Aufgabe
Ändere das Python Skript in der Datei *printText.py* so, dass Variablen mit 4 verschiedenen Datentyen (string, bool, integer, float) vom User eingelsen werden. Anschließend wird zu jeder Variable ein Informationssatz ausgegeben:  
*Die Variable 'ganzzahl' ist vom Datentyp '<class 'int'>' und hat gespeichert: 42  
Die Variable 'kommazahl' ist vom Datentyp '<class 'float'>' und hat gespeichert: 3.14  
Die Variable 'istPythonDoof' ist vom Datentyp '<class 'bool'> und hat gespeichert: False  
Die Variable 'text' ist vom Datentyp '<class 'str'>' und hat gespeichert: Python ist toll.*

Oder bei der Eingabe der Werte -23, 1.234, True und "Python ist leicht." wird ausgegeben:  
*Die Variable 'ganzzahl' ist vom Datentyp '<class 'int'>' und hat gespeichert: -23  
Die Variable 'kommazahl' ist vom Datentyp '<class 'float'>' und hat gespeichert: 1.234  
Die Variable 'istPythonDoof' ist vom Datentyp '<class 'bool'> und hat gespeichert: True  
Die Variable 'text' ist vom Datentyp '<class 'str'>' und hat gespeichert: Python ist leicht.*

**Erinnerung**
Denken Sie daran, dass Sie den Datentyp einer Variable mit dem Kommando `type` ermitteln können:  
```
zahl = 12
print(f"Datentyp von 'zahl' ist: '{type(zahl)}")
```

**WICHTIG:** Ändere **NICHT** die anderen Dateien
