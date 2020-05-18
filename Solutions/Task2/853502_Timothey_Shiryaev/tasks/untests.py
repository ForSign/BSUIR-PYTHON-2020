import unittest
from decorator import *
from singlt import *
from vecmod import Vector
from fpythtojson import to_json
from fpythonjson import from_json
import filecmp
import json
from mergesorting import external_merge


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass


    def test_fib(self):
        print('\n\n---Test fibonacci---')
        f1 = fibonacci(5)
        self.assertEqual(f1, 5)
        f2 = fibonacci(10)
        self.assertEqual(f2, 55)
        f3 = fibonacci(3)
        self.assertEqual(f3, 2)


    def test_failfib(self):
        f4 = fibonacci(5)
        print('\n\n---Test FAIL_fibonacci---')
        self.assertEqual(f4, 4)


    def test_vector(self):
        v1 = [12, -5]
        v2 = [13, 8]
        v3 = [12, -5]
        objv = Vector(v1, v2)
        print('\n\n---Test vector---')
        self.assertEqual(objv.sum_vec(), [25, 3])
        self.assertEqual(objv.mul_vec(), 116)
        self.assertEqual(objv.sub_vec(), [-1, -13])
        self.assertEqual(objv.mul_const(8), ([96, -40], [104, 64]))
        self.assertEqual(objv.comparison(), False)
        self.assertEqual(Vector(v1,v3).comparison(), True)
        self.assertEqual(objv.length(), (13.0, 15.264337522473747))
        self.assertEqual(objv.get_index(0), (12, 13))


    def test_FAil_mulvec(self):
        objv3 = Vector([12, -5], [13, 8])
        print('\n\n---Test FAIL_vector multiplication---')
        self.assertEqual(objv3.mul_vec(), [25, 3] )


    def test_singleton(self):
        @singleton
        class Person:
            def __init__(self, name, age, weight):
                self.name = name
                self.age = age
                self.weight = weight

        p = Person('Tom', 17, 80)
        d = Person('Delted', 17, 80)
        print('\n\n---Test singleton---')
        self.assertEqual(d, p)
        

    def test_success_to_json(self):   
        jdict  = {"Number1": 1, "Number2": 2, "Number3": 3, "Number4": 4, "Number5": 5, "Number6": 6, "Number7": 7, "Number8": 8, "Number9": 9}
        jlist  = ["Text1", "Text2", 1234, False, None]
        jtuple = ("String bool bool float None", True, False, 3.14, None)
        jint   = 123456
        jfloat = 1234.56
        jboolean_t = True
        jnone  = None
        jstring = "Pen pinapple apple pen"
        
        complex_data = {
        "glossary": {
            "title": "example glossary",
            "GlossDiv": {
                "title": "S",
                "GlossList": {
                    "GlossEntry": {
                        "ID": "SGML",
                        "SortAs": "SGML",
                        "GlossTerm": "Standard Generalized Markup Language",
                        "Acronym": "SGML",
                        "Abbrev": "ISO 8879:1986",
                        "GlossDef": {
                            "para": "A meta-markup language, used to create markup languages such as DocBook.",
                            "GlossSeeAlso": ["GML", "XML"]
                        },
                        "GlossSee": "markup"
                        }
                    }
                }
            }
        }

        print('\n\n---Test success_to_json---')

        @singleton
        class Person:
            def __init__(self, name, age, weight):
                self.name = name
                self.age = age
                self.weight = weight

        p = Person('Tom', 17, 80)

        self.assertEqual(to_json(p), {'age': 17, 'name': 'Tom', 'weight': 80})

        assert to_json(jint) == json.dumps(jint)
        assert to_json(jfloat) == json.dumps(jfloat)
        assert to_json(jboolean_t) == json.dumps(jboolean_t)
        assert to_json(jnone) == json.dumps(jnone)
        assert to_json(jstring) == json.dumps(jstring)
        assert to_json(jtuple) == json.dumps(jtuple)
        assert to_json(jdict) == json.dumps(jdict)
        assert to_json(jlist) == json.dumps(jlist)

        assert to_json(complex_data) == json.dumps(complex_data)


    def test_from_json(self):
        print('\n\n---Test from_json---')
        obj1 = from_json('"powers": ["Immortality", "Heat Immunity", "Inferno", "Teleportation", "Interdimensional travel"]')
        fint   = "123456"
        ffloat = "1234.56"
        fboolean_t = "true"
        fboolean_f = "false"
        fnone  = 'null'
        fstring = '"Pen pinapple apple pen"'
        noble = '{"James": 9001, "Jo": 3474, "Jess": 11926 }'
        self.assertEqual(obj1, 'powers: [Immortality, Heat Immunity, Inferno, Teleportation, Interdimensional travel]')
        assert from_json(fint) == json.loads(fint)
        assert from_json(ffloat) == json.loads(ffloat)
        assert from_json(fboolean_t) == json.loads(fboolean_t)
        assert from_json(fboolean_f) == json.loads(fboolean_f)
        assert from_json(fnone) == json.loads(fnone)
        assert from_json(fstring) == json.loads(fstring)
        assert from_json(noble) == json.loads(noble)


    def test_fail_to_json(self):
        print('\n\n---Test FAIL_to_json---')
        self.assertEqual(to_json({"name": "John", "age": 30}), 456)


    def test_merge_sort(self):
        print('\n\n---Test merge-sort\'а---')
        external_merge('numbers.txt')
        self.assertEqual(filecmp.cmp('out.txt', 'outtest.txt'), True)


if __name__ == '__main__':
    unittest.main()
