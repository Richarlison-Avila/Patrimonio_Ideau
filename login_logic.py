import sys
import re
from PyQt5 import QtWidgets
from login_ui import Ui_LoginWindow

class LoginApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        # Conecta o botão "Entrar" à função de verificação
        self.ui.btnEntrar.clicked.connect(self.verificar_login)

    def verificar_login(self):
        usuario = self.ui.txtUsuario.text()
        senha = self.ui.txtSenha.text()

        # --- Validação dos requisitos da senha ---
        tem_maiuscula = re.search(r'[A-Z]', senha)
        tem_numero = re.search(r'\d', senha)
        tem_especial = re.search(r'[!@#$%^&*(),.?":{}|<>]', senha)

        if not (tem_maiuscula and tem_numero and tem_especial):
            QtWidgets.QMessageBox.warning(
                self,
                "Senha inválida",
                "A senha precisa ter:\n"
                "- pelo menos 1 letra maiúscula\n"
                "- pelo menos 1 número\n"
                "- pelo menos 1 caractere especial"
            )
            return  # Para a execução caso os requisitos não sejam atendidos

        # --- Validação de usuário/senha correta ---
        if usuario == "admin" and senha == "Ide@u10":
            QtWidgets.QMessageBox.information(self, "Sucesso", "Login correto!")
        else:
            QtWidgets.QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec_())   