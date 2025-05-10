import os
import shutil



######################################## ATENÇÃO LEIA OS COMENTÁRIOS ################################
# Quando você roda o código que está em nesse caminho external/ImageNet-C/create_c/make_imagenet_c.py

# Vai criar uma estrutura de pastas semelhante a essa descrita na imagem: ./estruturaDePastaPos-make_imagenet_py.PNG

# E ai para os notebooks rodarem o pipeline com êxito é necessário executar esse código chamado reorganizarPasta.py

# Ele vai sair da estrutura mencionada acima para a estrutrua de pastas demonstrada no artigo

# OBSERVAÇÃO!!!!! Esse código vai mover os arquivos então uma vez movido a estrutura de saída do make_imagenet_c.py irá existir, no entanto, ficará sem os arquivos dentro da estrutura.
##########################################


# Verificar diretório atual
print(f"Executando em: {os.getcwd()}")


# Diretórios (use caminho absoluto)
origin = r"..\BANCOSCORROMPIDOS"  # ATUALIZE ESTE CAMINHO COM A PASTA GERADA PELO make_imagenet_c.py
destination = r"..\BancosCorrompidaNovaEstrutura" # ATUALIZE ESTE CAMINHO COM O CAMINHO QUE VOCÊ QUER DEIXAR O MangoLeafDB-C estruturado para o pipeline

# # Diretórios de origin e destination
# origin = 'BANCOSCORROMPIDOS'
# destination = 'BancosCorrompidaNovaEstrutura'

# Verificar se a pasta de origin existe
if not os.path.exists(origin):
    print(f"ERRO: Pasta '{origin}' não encontrada!")
    print(f"Path completo: {os.path.abspath(origin)}")
    exit()

# Lista de corrupções (pastas principais)
corrupcoes = [
    'brightness', 'contrast', 'defocus_blur', 'elastic_transform', 'fog', 'frost', 'gaussian_blur',
    'gaussian_noise', 'glass_blur', 'impulse_noise', 'jpeg_compression', 'motion_blur', 'pixelate', 'saturate',
    'shot_noise', 'snow', 'speckle_noise', 'zoom_blur', 'spatter'
]

# Pastas de doenças (subpastas)
doencas = [
    'Anthracnose', 'Bacterial Canker', 'Cutting Weevil', 'Die Back', 'Gall Midge',
    'Healthy', 'Powdery Mildew', 'Sooty Mould'
]



# Criar pasta de destination se não existir
if not os.path.exists(destination):
    os.makedirs(destination)

# Processar cada corrupção
for corrupcao in corrupcoes:
    caminho_corrupcao = os.path.join(origin, corrupcao)
    
    # Verificar se a pasta de corrupção existe
    if not os.path.exists(caminho_corrupcao):
        print(f"Aviso: Pasta '{corrupcao}' não encontrada em {origin}")
        continue
    
    # Processar cada nível (1 a 5)
    for nivel in range(1, 6):
        nivel_str = str(nivel)
        caminho_nivel = os.path.join(caminho_corrupcao, nivel_str)
        
        # Verificar se a pasta de nível existe
        if not os.path.exists(caminho_nivel):
            print(f"Aviso: Pasta '{nivel_str}' não encontrada em {caminho_corrupcao}")
            continue
        
        # Criar nome da nova pasta (corrupção_nível)
        nova_pasta = f"{corrupcao}_{nivel}"
        caminho_nova_pasta = os.path.join(destination, nova_pasta)
        
        # Criar a nova pasta se não existir
        if not os.path.exists(caminho_nova_pasta):
            os.makedirs(caminho_nova_pasta)
        
        # Mover cada pasta de doença para a nova pasta
        for doenca in doencas:
            caminho_doenca_origin = os.path.join(caminho_nivel, doenca)
            caminho_doenca_destination = os.path.join(caminho_nova_pasta, doenca)
            
            # Verificar se a pasta de doença existe na origin
            if os.path.exists(caminho_doenca_origin):
                # Se já existe no destination, mesclar os conteúdos
                if os.path.exists(caminho_doenca_destination):
                    # Copiar arquivos individuais para evitar sobrescrever pastas inteiras
                    for arquivo in os.listdir(caminho_doenca_origin):
                        origin_arquivo = os.path.join(caminho_doenca_origin, arquivo)
                        destination_arquivo = os.path.join(caminho_doenca_destination, arquivo)
                        
                        # Se o arquivo já existe no destination, pular ou renomear
                        if os.path.exists(destination_arquivo):
                            base, ext = os.path.splitext(arquivo)
                            i = 1
                            while True:
                                novo_nome = f"{base}_{i}{ext}"
                                novo_destination = os.path.join(caminho_doenca_destination, novo_nome)
                                if not os.path.exists(novo_destination):
                                    destination_arquivo = novo_destination
                                    break
                                i += 1
                        
                        shutil.move(origin_arquivo, destination_arquivo)
                    
                    # Remover pasta de origin vazia
                    try:
                        os.rmdir(caminho_doenca_origin)
                    except OSError:
                        pass
                else:
                    # Mover a pasta inteira
                    shutil.move(caminho_doenca_origin, caminho_doenca_destination)
            else:
                print(f"Aviso: Pasta '{doenca}' não encontrada em {caminho_nivel}")

print("Reorganização concluída!")


print("Vá para o código renomeandoPastaParaAvaliacao.py")