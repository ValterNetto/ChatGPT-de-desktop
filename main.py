from senha import API_KEY
import requests
import json
import tkinter as tk

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/models"
link2 = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

def enviar_request():
    informacao = entrada_texto.get()
    texto_saida.config(state=tk.NORMAL)
    texto_saida.delete(1.0, tk.END)
    #Mensagem à ser passada
    body_mensagem = {
            "model": id_modelo,
        "messages": [{"role": "user", "content": f"{informacao}"}]
    }

    body_mensagem = json.dumps(body_mensagem)
    requisicao = requests.post(link2, headers=headers, data=body_mensagem)
    resposta = requisicao.json()
    mensagem = resposta["choices"][0]["message"]["content"]
    texto_saida.insert(tk.END, mensagem)
    texto_saida.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Falando com o GPT")

largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
root.geometry(f"{largura_tela}x{altura_tela}")

tamanho_texto = 20
rotulo_entrada = tk.Label(root, text="Faça sua pergunta:", font=("Arial", tamanho_texto))
rotulo_entrada.pack(pady=10)
entrada_texto = tk.Entry(root, width=160, font=("Arial", int(tamanho_texto / 2)))
entrada_texto.pack(pady=10)
botao_exibir = tk.Button(root, text="Enviar", command=enviar_request, font=("Arial", tamanho_texto))
botao_exibir.pack(pady=10)
texto_saida = tk.Text(root, height=30, width=160, state=tk.DISABLED, font=("Arial", int (tamanho_texto / 2)))
texto_saida.pack(pady=10)

root.mainloop()