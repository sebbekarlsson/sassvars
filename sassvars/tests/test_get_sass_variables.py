from sassvars import get_sass_variables


def test_get_sass_variables():
    doc = """
    $color: red;
    $color_two: green;
    $background_color: #81ecec;
    $width: 640px;
    $height: 640px;     $background_other: white;
    """

    variables = get_sass_variables(doc)

    assert 'color' in variables
    assert 'color_two' in variables
    assert 'background_color' in variables
    assert 'width' in variables
    assert 'height' in variables
    assert 'background_other' in variables

    assert variables['color'] == 'red'
    assert variables['color_two'] == "green"
    assert variables['background_color'] == '#81ecec'
    assert variables['width'] == '640px'
    assert variables['height'] == '640px'
    assert variables['background_other'] == 'white'
