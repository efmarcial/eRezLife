from problem_2 import format_html


def test_format():
    string = '<html><body><div><a></a></div></body></html>'
    string2 = '<html><body><div></a></body></html>'
    string3 = '<html><body><div><a></div></a>'

    assert format_html(string) == 0
    assert format_html(string2) == 1
    assert format_html(string3) == 1
