from random import shuffle

suits = ["spades", "hearts", "diamonds", "clubs"]
values = [None, None,"2", "3", "4", "5", "6", "7",
          "8", "9", "10","Jack", "Queen", "King", "Ace"]

def play_game():
    cards = []

    for i in range(2, 15):
        for j in range(4):
            cards.append([i, j])

    shuffle(cards)

    p1_wins = 0
    p2_wins = 0
    p1_card = None
    p2_card = None
    winner = None

    p1_name = input("プレーヤー1の名前：")
    p2_name = input("プレーヤー2の名前：")
    print("戦争を始めます")

    while len(cards) >=2:
        m = "qで終了、それ以外のキーでPlay:"
        response = input(m)
        if response == "q":
            break
        p1_card = cards.pop()
        p2_card = cards.pop()
        p1_card_name = values[p1_card[0]] + " of " + suits[p1_card[1]]
        p2_card_name = values[p2_card[0]] + " of " + suits[p2_card[1]]
        d = "{} は{},{}は{}を引きました。"
        d = d.format(p1_name,p1_card_name,p2_name,p2_card_name)
        print(d)

        if p1_card[0] > p2_card[0]:
            p1_wins += 1
            print("このラウンドは{}が勝ちました。".format(p1_name))
        elif p1_card[0] == p2_card[0]:
            if p1_card[1] < p2_card[1]:
                p1_wins += 1
                print("このラウンドは{}が勝ちました。".format(p1_name))
            else:
                p2_wins += 1
                print("このラウンドは{}が勝ちました。".format(p2_name))
        else:
            p2_wins += 1
            print("このラウンドは{}が勝ちました。".format(p2_name))

    if p1_wins > p2_wins:
        winner = p1_name
    elif p1_wins < p2_wins:
        winner = p2_name
    else:
        winner = "引き分け!"

    print("ゲーム終了! {}の勝利です!".format(winner))
    print("p1_wins:{} vs. p2_wins:{}".format(p1_wins,p2_wins))

play_game()