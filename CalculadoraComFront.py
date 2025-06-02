import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        capital = float(entry_capital.get())
        aporte = float(entry_aporte.get())
        taxa = float(entry_juros.get()) / 100
        tempo = int(entry_tempo.get())
        periodo = var_periodo.get()

        if periodo == "A":
            tempo *= 12
            taxa = (1 + taxa)**(1/12) - 1  # taxa equivalente mensal

        montante = capital
        resultado = "Mês\tMontante (R$)\n"

        for i in range(tempo + 1):
            if i == 0:
                resultado += f"{i}\t{montante:.2f}\n"
            else:
                montante = (montante + aporte) * (1 + taxa)
                resultado += f"{i}\t{montante:.2f}\n"

        resultado += f"\n💰 Montante final: R$ {montante:.2f}"

        text_resultado.delete("1.0", tk.END)
        text_resultado.insert(tk.END, resultado)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro nos dados inseridos:\n{e}")

# Interface
janela = tk.Tk()
janela.title("Simulador de Juros Compostos")
janela.geometry("400x550")
janela.resizable(False, False)

# Entrada de dados
tk.Label(janela, text="Capital Inicial (R$):").pack()
entry_capital = tk.Entry(janela)
entry_capital.pack()

tk.Label(janela, text="Aporte Mensal (R$):").pack()
entry_aporte = tk.Entry(janela)
entry_aporte.pack()

tk.Label(janela, text="Taxa de Juros (%):").pack()
entry_juros = tk.Entry(janela)
entry_juros.pack()

tk.Label(janela, text="Tempo (número):").pack()
entry_tempo = tk.Entry(janela)
entry_tempo.pack()

tk.Label(janela, text="Período da taxa e do tempo:").pack()
var_periodo = tk.StringVar(value="M")
tk.Radiobutton(janela, text="Mensal", variable=var_periodo, value="M").pack()
tk.Radiobutton(janela, text="Anual", variable=var_periodo, value="A").pack()

tk.Button(janela, text="Calcular", command=calcular).pack(pady=10)

# Saída de resultados
text_resultado = tk.Text(janela, height=20, width=45)
text_resultado.pack(pady=10)

janela.mainloop()