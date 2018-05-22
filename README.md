# sassvars
> Sass variable parsing for Python

## Usage
> To use it:

    from sassvars import get_sass_variables

    doc = """
    $color: red;
    $color_two: green;
    $background_color: #81ecec;
    $width: 640px;
    $height: 640px;     $background_other: white;
    """

    variables = get_sass_variables(doc)

> `variables` will now contain a dictionary:

    assert variables['color'] == 'red' # true

> That's it!

## Install
> To install, clone down this repository and run:

    python setup.py install

## Unit tests
> To run unit tests, first install `pytest`:

    pip install pytest

> Then run:

    py.test
