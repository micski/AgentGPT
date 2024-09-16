from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget
from models.models import AIModel  # Import klasy modelu AI


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AgentGPT - Virtual Game Master")
        self.setGeometry(100, 100, 600, 400)

        # Inicjalizacja modelu AI
        self.ai_model = AIModel()

        self.text_edit = QTextEdit(self)
        self.send_button = QPushButton("Send", self)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.send_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.send_button.clicked.connect(self.send_command)
    
    # Funkcja obsługująca przycisk "Send"
    def send_command(self):
        user_input = self.text_edit.toPlainText()
        self.text_edit.append(f"User: {user_input}")

        # Generowanie odpowiedzi z modelu AI
        response = self.ai_model.generate_response(user_input)
        self.text_edit.append(f"AI: {response}\n")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
