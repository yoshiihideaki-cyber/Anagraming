from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox, QTextEdit
from PyQt5.QtGui import QFont, QGuiApplication
import random
import numpy as np

class AnagramApp(QWidget):
    def __init__(self, titles):
        super().__init__()
        self.titles = titles
        self.initUI()
        self.start_new_game()

    def initUI(self):
        self.setWindowTitle("アナグラミング")
        
        # ウィンドウのサイズ変更
        # self.resize(800, 400)

        # フォント・文字サイズ変更
        font = QFont("Arial", 24)
        self.setFont(font)
        self.layout = QVBoxLayout()
        # self.layout.setSpacing(20)
        self.h_layout = QHBoxLayout()
        self.h_layout_2 = QHBoxLayout()

        self.question_label = QLabel("【問題】")
        self.question_label.setFont(QFont("Arial", 32))
        self.layout.addWidget(self.question_label)
        
        self.answer_entry = QLineEdit()
        self.answer_entry.setPlaceholderText("ここに回答を入力してください")
        self.answer_entry.setFixedSize(1000, 40)
        self.layout.addWidget(self.answer_entry)

        self.check_button = QPushButton("回答をチェック")
        self.check_button.clicked.connect(self.check_answer)
        self.h_layout.addWidget(self.check_button)

        self.new_game_button = QPushButton("次の問題")
        self.new_game_button.clicked.connect(self.start_new_game)
        self.h_layout.addWidget(self.new_game_button)

        self.layout.addLayout(self.h_layout)

        self.hint_button = QPushButton("ヒントを表示")
        self.hint_button.clicked.connect(self.show_hint)
        self.h_layout_2.addWidget(self.hint_button)

        self.ans_button = QPushButton("答えを表示")
        self.ans_button.clicked.connect(self.show_answer)
        self.h_layout_2.addWidget(self.ans_button)        

        self.copy_question_button = QPushButton("問題をコピー")
        self.copy_question_button.clicked.connect(self.copy_question)
        self.h_layout_2.addWidget(self.copy_question_button)

        self.layout.addLayout(self.h_layout_2)

        self.memo_box = QTextEdit()
        self.memo_box.setPlaceholderText("ここにメモを入力してください")
        self.memo_box.setFixedSize(1000, 200)
        self.layout.addWidget(self.memo_box)

        self.setLayout(self.layout)

    def start_new_game(self):
        self.current_answer = random.choice(self.titles).strip()
        numbers = np.arange(len(self.current_answer))
        random.shuffle(numbers)
        self.current_question = "".join([self.current_answer[i] for i in numbers])
        self.question_label.setText(f"【問題】 {self.current_question}")

    def check_answer(self):
        user_input = self.answer_entry.text().strip()
        if user_input == "答え":
            QMessageBox.information(self, "答え", f"答えは: {self.current_answer}")
        elif user_input == self.current_answer:
            QMessageBox.information(self, "正解", "正解！！！！")
        else:
            QMessageBox.warning(self, "不正解", "残念〜不正解")
        self.answer_entry.clear()

    def show_hint(self):
        QMessageBox.information(self, "ヒント", f"最初の文字: {self.current_answer[0]}")

    def show_answer(self):
        QMessageBox.information(self, "答え", f"答え: {self.current_answer}")

    def copy_question(self):
        clipboard = QGuiApplication.clipboard()  # クリップボードを取得
        clipboard.setText(self.current_question)  # 問題文をコピー



def get_titles():
    # with open("title_hardmode", "r") as file:
    with open("title_archive", "r") as file:
        return file.readlines()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    titles = get_titles()
    ex = AnagramApp(titles)
    ex.show()
    sys.exit(app.exec_())
