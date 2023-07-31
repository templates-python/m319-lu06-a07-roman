from roman import main


def test_lists(capsys):
    num, dec = main()
    assert num == list(('M', 'D', 'C', 'L', 'X', 'V', 'I'))
    assert dec == list((1000, 500, 100, 50, 10, 5, 1))

def test_roman1(capsys, monkeypatch):
    inputs = iter([21])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    captured = capsys.readouterr()
    assert captured.out == 'XXI\n'


def test_roman2(capsys, monkeypatch):
    inputs = iter([2576])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    captured = capsys.readouterr()
    assert captured.out == 'MMDLXXVI\n'