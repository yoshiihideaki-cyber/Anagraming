import random
import numpy as np

def anagram_generator(title):
    ans = title
    num = len(title)

    numbers = np.arange(num)
    random.shuffle(numbers)
    question = title[numbers[0]]

    for i in range(num - 1):
        question += title[numbers[i+1]]

    # 結果を表示
    print("【問題】\n", question)
    print("==============================")

    while True:
        tmp = input("「ヒント」or「答え」\n")
        if tmp == "ヒント":
            print("最初の文字は：", ans[0])
            print("==============================")
        elif tmp == "答え":
            print(ans)
            print("==============================")
            break
        elif tmp == ans:
            print("正解！！！！")
            print("==============================")
            break
        elif tmp == "":
            break
        else:
            print("残念〜不正解")

def get_titles():
    file_data = open("title_data", "r")
    titles = file_data.readlines()

    # 開いたファイルを閉じる
    file_data.close()
    return titles

def random_select_title(titles):
    num = len(titles)
    q_num = random.randrange(num)
    title = titles[q_num]
    title = titles[q_num].strip()
    return title

def main():
    titles = get_titles()
    while True:
        title = random_select_title(titles)
        anagram_generator(title)
        flag = input("終わる場合は「End」、続ける場合はEnter key\n")
        if flag == "End":
            break

if __name__ == "__main__":
    main()
