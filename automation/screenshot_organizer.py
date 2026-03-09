import os
import shutil
from datetime import datetime

def organize_screenshots():
    import os
    import shutil
    from datetime import datetime

    # Forçamos o caminho exato que vimos na sua imagem
    user_profile = os.environ['USERPROFILE']
    
    # Lista de tentativas de caminhos possíveis no seu OneDrive
    caminhos_possiveis = [
        os.path.join(user_profile, 'OneDrive', 'Imagens', 'Capturas de Tela'),
        os.path.join(user_profile, 'OneDrive', 'Pictures', 'Screenshots'),
        os.path.join(user_profile, 'OneDrive', 'Imagens', 'Screenshots'),
        # Caso o OneDrive tenha um nome diferente na pasta raiz:
        os.path.join(user_profile, 'OneDrive - Personal', 'Imagens', 'Capturas de Tela')
    ]

    src_folder = None
    for caminho in caminhos_possiveis:
        if os.path.exists(caminho):
            src_folder = caminho
            break

    if not src_folder:
        print(f"❌ ERRO: Nenhuma das pastas foi encontrada.")
        print(f"Caminho verificado por último: {caminhos_possiveis[0]}")
        return

    print(f"✅ Pasta localizada: {src_folder}")

    files = [f for f in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, f))]
    moved_count = 0

    print("=== ORGANIZADOR DE CAPTURAS DE TELA ===")
    
    for file in files:
        # Filtra por nomes comuns de print do Windows
        if file.lower().startswith(("screenshot", "captura de tela")):
            file_path = os.path.join(src_folder, file)
            
            # Obtém a data de criação do arquivo
            m_time = os.path.getmtime(file_path)
            date_folder = datetime.fromtimestamp(m_time).strftime('%Y-%m (Prints)')
            
            dest_folder = os.path.join(src_folder, date_folder)
            
            # Cria a pasta do mês se não existir
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            
            # Move o arquivo
            shutil.move(file_path, os.path.join(dest_folder, file))
            print(f"Movido: {file} -> {date_folder}")
            moved_count += 1

    print(f"\nSucesso: {moved_count} capturas organizadas.")
    input("\nPressione Enter para sair...")

if __name__ == "__main__":
    organize_screenshots()