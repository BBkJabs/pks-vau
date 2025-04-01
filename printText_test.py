from pytest import MonkeyPatch
import printText
import io

def test_firstInput(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('42\n3.14\nFalse\nPython ist toll.'))
    printText.main()
    captured = capsys.readouterr()
    expected_output = (
        "Gebe Ganzzahl ein: Gebe Kommazahl ein: Ist Python doof? (True/False): Gebe Text ein: "
        "Die Variable 'ganzzahl' ist vom Datentyp '<class 'int'>' und hat gespeichert: 42\n" 
        "Die Variable 'kommazahl' ist vom Datentyp '<class 'float'>' und hat gespeichert: 3.14\n"  
        "Die Variable 'istPythonDoof' ist vom Datentyp '<class 'bool'> und hat gespeichert: False\n"
        "Die Variable 'text' ist vom Datentyp '<class 'str'>' und hat gespeichert: Python ist toll."
    )
    expected_output = expected_output.replace('\r\n', '\n').strip()
    output = '\n'.join(line.strip() for line in captured.out.splitlines()).replace('\r\n', '\n').strip()
    print("Captured output:", repr(output))
    assert output == expected_output

def test_secondInput(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('-23\n1.234\nTrue\nPython ist einfach.'))
    printText.main()
    captured = capsys.readouterr()
    expected_output = (
        "Gebe Ganzzahl ein: Gebe Kommazahl ein: Ist Python doof? (True/False): Gebe Text ein: "
        "Die Variable 'ganzzahl' ist vom Datentyp '<class 'int'>' und hat gespeichert: -23\n" 
        "Die Variable 'kommazahl' ist vom Datentyp '<class 'float'>' und hat gespeichert: 1.234\n"  
        "Die Variable 'istPythonDoof' ist vom Datentyp '<class 'bool'> und hat gespeichert: True\n"
        "Die Variable 'text' ist vom Datentyp '<class 'str'>' und hat gespeichert: Python ist einfach."
    )
    expected_output = expected_output.replace('\r\n', '\n').strip()
    output = '\n'.join(line.strip() for line in captured.out.splitlines()).replace('\r\n', '\n').strip()
    print("Captured output:", repr(output))
    assert output == expected_output

def test_thirdInput(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('0\n0.0\nFalse\nPython'))
    printText.main()
    captured = capsys.readouterr()
    expected_output = (
        "Gebe Ganzzahl ein: Gebe Kommazahl ein: Ist Python doof? (True/False): Gebe Text ein: "
        "Die Variable 'ganzzahl' ist vom Datentyp '<class 'int'>' und hat gespeichert: 0\n"
        "Die Variable 'kommazahl' ist vom Datentyp '<class 'float'>' und hat gespeichert: 0.0\n"
        "Die Variable 'istPythonDoof' ist vom Datentyp '<class 'bool'> und hat gespeichert: False\n"
        "Die Variable 'text' ist vom Datentyp '<class 'str'>' und hat gespeichert: Python"
    )
    expected_output = expected_output.replace('\r\n', '\n').strip()
    output = '\n'.join(line.strip() for line in captured.out.splitlines()).replace('\r\n', '\n').strip()
    print("Captured output:", repr(output))
    assert output == expected_output