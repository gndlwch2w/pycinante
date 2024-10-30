from pycinante import export

@export
def f():
    pass

@export
def g(a, b, c):
    pass

@export
class A:
    pass

@export
class B:
    def __init__(self):
        pass

c = "123"
d = [4, 5, 6]

export("c")
export("d")

def test_export():
    print()
    print(globals()["__all__"])
    print(f, g, A, B, c, d)
