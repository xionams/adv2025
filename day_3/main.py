

PATH = "input.txt"


def find_max_of_vector(vector: str) -> int:
    digits = [int(c) for c in vector.strip()]
    n = len(digits)
    highest = 0
    
    for index in range(n - 1):
        a = digits[index]
        b = max(digits[index+1:]) # check only the rights
        candidate = (a * 10) + b
        highest = max(highest, candidate)
    
    return highest
      

def load_file(path: str) -> list[str]:
    with open(path, "r", encoding="utf8") as file:
        return file.readlines()
    
def read_line(chunks: list[str]) -> int:
    result = 0
    for chunk in chunks:
        result += find_max_of_vector(chunk)
    return result

def tests():
    assert find_max_of_vector("888181192") == 92
    assert find_max_of_vector("818181911112111") == 92
    assert find_max_of_vector("811111111111119") == 89
    assert find_max_of_vector("234234234234278") == 78
    assert find_max_of_vector("987654321111111") == 98


if __name__ == '__main__':
    tests()
    chunks: list[str] = load_file(PATH)
    result: int = read_line(chunks)
    print(f"The solution is: {result}")

