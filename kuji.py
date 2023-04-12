import random
kuji = ["大吉", "中吉", "末吉", "吉", "凶", "大吉"]
print(random.choice(kuji))

import random
def kuji():
    kuji = ["大吉", "中吉", "末吉", "吉", "凶", "大吉"]
    return random.choice(kuji)
kekka = kuji()
print("結果は、" + kekka + "です。")