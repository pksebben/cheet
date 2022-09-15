import pytest

from core.cheet import Cheet

class TestCheetFunctions:
    def test_equality():
         cheet1 = Cheet(
            'name',
            'key',
            'context',
            'description',
            'note',
            ['tag'],
            'id'
         )
         cheet2 = Cheet(
            'name',
            'key',
            'context',
            'description',
            'note',
            ['tag'],
            'id'
         )
         assert cheet1 == cheet2



class TestSerde:
    def test_empty_tag_list():
        cheet_dict =   {
            "note": "note",
            "context": "context",
            "description": "description",
            "id": "id",
            "name": "name",
            "key": "key",
            "tags": []
        }
        good_cheet = Cheet(
            'name',
            'key',
            'context',
            'description',
            'note',
            [],
            'id'
        )
