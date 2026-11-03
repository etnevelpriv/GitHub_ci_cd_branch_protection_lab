def osszeAdas(a: int, b:int):
    return a+b

def udvozles(nev:str):
    print(f"Hellof, {nev}")
    
def main():
    print(osszeAdas(10,5))
    udvozles("Balint")
main()

def test():
    assert osszeAdas(10,5) == 15