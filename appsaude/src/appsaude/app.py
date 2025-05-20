import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER, ROW
from .func import calulcar


class AppSaude(toga.App):
    def startup(self):
        # Estilo base
        main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=30, background_color="#f4f4f4"))

        # Título
        title_label = toga.Label(
            "💙 Bem-vindo ao App Saúde!",
            style=Pack(font_size=24, font_weight="bold", color="#2c3e50", padding_bottom=20)
        )

        # Campo de entrada
        hello_input = toga.TextInput(
            placeholder="Digite um número...",
            style=Pack(width=250, padding_bottom=15, font_size=14)
        )

        # Label de resultado
        resultado_label = toga.Label(
            "",
            style=Pack(padding=(10, 0, 10, 0), font_size=16, color="#34495e")
        )

        # Função ao clicar em calcular
        def on_calcular(widget):
            try:
                numero = float(hello_input.value)
                resultado = calulcar(numero)
                resultado_label.text = f"✅ Resultado: {resultado}"
            except ValueError:
                resultado_label.text = "❌ Por favor, digite um número válido."

        # Botão de cálculo
        calcular_button = toga.Button(
            "🔍 Calcular",
            on_press=on_calcular,
            style=Pack(padding_bottom=20, background_color="#2980b9", color="white", font_size=16, width=150)
        )

        # Adiciona os componentes
        main_box.add(title_label)
        main_box.add(hello_input)
        main_box.add(calcular_button)
        main_box.add(resultado_label)

        # Janela principal
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return AppSaude()
