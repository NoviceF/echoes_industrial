import json
import os

import cv2
import pytest

from ResourcesImageProcessor.NumbersDetection.NumberParser import get_number
from ResourcesImageProcessor.Processor import process_image, ResourceDuplication


def test_parseOre():
    main_image = cv2.imread('images/all_ore_template.png')
    resourcesList = process_image(main_image)

    expected = {
        'veldspar': 1,
        'scordite': 2,
        'pyroxeres': 3,
        'plagioclase': 4,
        'omber': 5,
        'kernite': 6,
        'jaspet': 7,
        'hemorphite': 8,
        'hedbergite': 9,
        'spodumain': 10,
        'dark_ochre': 11,
        'gneiss': 12,
        'crokite': 13,
        'bistot': 14,
        'arkonor': 15,
        'mercoxit': 16
    }

    dictA_str = json.dumps(expected, sort_keys=True)
    dictB_str = json.dumps(resourcesList, sort_keys=True)

    assert dictA_str == dictB_str


def test_parseNotExistingOre(monkeypatch):
    path_to_image = '../samples/tritanium.png'
    samples = dict()
    samples[os.path.basename(path_to_image)] = cv2.imread(path_to_image, 0)
    monkeypatch.setattr('ResourcesImageProcessor.Processor.g_samples', samples)
    main_image = cv2.imread('images/ore_list_example_no_tritanium.png')
    # main_image = cv2.imread('ore_list_example.png')
    resourcesList = process_image(main_image)

    assert not resourcesList


def test_parseDoubleTritanium(monkeypatch):
    path_to_image = '../samples/tritanium.png'
    samples = dict()
    samples[os.path.basename(path_to_image)] = cv2.imread(path_to_image, 0)
    monkeypatch.setattr('ResourcesImageProcessor.Processor.g_samples', samples)

    main_image = cv2.imread('images/ore_list_example_double_tritanium_vert.png')

    with pytest.raises(ResourceDuplication):
        process_image(main_image)


def test_parseNumber():
    image = cv2.imread('images/number_example.png')
    assert get_number(image) == 1234567890
