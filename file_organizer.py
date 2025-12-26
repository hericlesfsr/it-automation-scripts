import os
import shutil

PASTA = "arquivos_treino"

def organizar():
    if not os.path.exists(PASTA):
        print("Pasta não encontrada.")
        return

    for arquivo in os.listdir(PASTA):
        caminho = os.path.join(PASTA, arquivo)

        if os.path.isfile(caminho):
            extensao = os.path.splitext(arquivo)[1].lower()

            if extensao == ".txt":
                destino = os.path.join(PASTA, "Textos")
            elif extensao == ".pdf":
                destino = os.path.join(PASTA, "PDFs")
            elif extensao == ".png":
                destino = os.path.join(PASTA, "PNG")
            else:
                destino = os.path.join(PASTA, "Outros")

            os.makedirs(destino, exist_ok=True)
            shutil.move(caminho, destino)

            print(f"{arquivo} movido para {destino}")

    print("Organização concluída!")

if __name__ == "__main__":
    organizar()
