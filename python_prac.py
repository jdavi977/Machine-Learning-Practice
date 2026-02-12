def process_list(num: list) -> list:
    new_list = []
    for n in num:
        var = n ** 2
        if var % 2 == 0:
            new_list.append(var)
    return new_list

list = [1,2,3,4,5,6,7,8,9,10]
print(process_list(list))

def analyze_text(sentence: str) -> tuple:
    words = sentence.split()
    print(words)

print(analyze_text("hello, my name is Peter, I am 26 years old"))