def osszeAdas(a: int, b:int):
    return a+b+1

def udvozles(nev:str):
    print(f"Hellofghf, {nev}")
    
def main():
    print(osszeAdas(10,5))
    udvozles("Balint")
main()

def test():
    assert osszeAdas(10,5) == 15