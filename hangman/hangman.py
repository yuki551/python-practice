import random

answers = ['peach', 'apple', 'orange', 'grapes']

# answersリストから、答えとなる単語をランダムで選ぶ
ans = random.choice(answers)

# 答えをリスト化して「letters」に代入
letters = list(ans)

# プレイヤーの答えを可視化させる(初期は文字数の数だけ_アンダースコアを表示)
player_ans = ["_"] * len(ans)

# 勝ち負け判定
win = False

# 不正解の数を初期化
wrong = 0

print('\nハングマンやるよーーー')
print('{}文字の果物の英単語をあててね。\n'.format(len(ans)))

print(' '.join(player_ans))

while wrong < 3:
    word = input('\n英小文字を1つ入力してください\n')
    print("\n")
    # @使われたらダメ
    if word == "@":
        print('英小文字を入力してね')
        break
    if word in letters:
        idx = letters.index(word)
        player_ans[idx] = word
        letters[idx] = "@"
        print(' '.join(player_ans))
    else:
        print("違うよ！")
        wrong += 1
        print("     ------")
        print("     |    |")
        print("     |    " + ("O" if wrong > 0 else ""))
        print("     |   " + ("/|\\" if wrong > 1 else ""))
        print("     |   " + ("/ \\" if wrong > 2 else ""))
        print(" --------")
    if "_" not in player_ans:
        print("\nあなたの勝ち！")
        win = True
        break
if win == False:
    print("\nあなたの負け！")
    print('正解は{}でした。'.format(ans))
