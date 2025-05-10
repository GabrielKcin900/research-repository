import os
import shutil

############################## ATENÇÃO #########################
# Para executar os notebooks 


# Defina o caminho da pasta onde estão as pastas originais
base_path = r"../BancosCorrompidaNovaEstrutura"


# Defina o caminho da nova estrutura de pastas
new_base_path = r"../estruturaParaMceERelative_VALIDADO"

# Mapeamento das pastas antigas para as novas categorias e nomes
mapping = {
    'blur': {
        'Defocus Blur': 'defocus_blur',
        'Gaussian Blur': 'gaussian_blur',
        'Glass Blur': 'glass_blur',
        'Motion Blur': 'motion_blur',
        'Zoom Blur': 'zoom_blur'
    },
    'digital': {
        'Contrast': 'contrast',
        'Elastic': 'elastic_transform',
        'JPEG': 'jpeg_compression',
        'Pixelate': 'pixelate',
        'Saturate': 'saturate'
    },
    'noise': {
        'Gaussian Noise': 'gaussian_noise',
        'Impulse Noise': 'impulse_noise',
        'Shot Noise': 'shot_noise',
        'Speckle Noise': 'speckle_noise'
    },
    'weather': {
        'Brightness': 'brightness',
        'Fog': 'fog',
        'Frost': 'frost',
        'Snow': 'snow',
        'Spatter': 'spatter'
    }
}

# Função para criar a nova estrutura de pastas e copiar os arquivos
def reorganize_folders(base_path, new_base_path, mapping):
    for category, corruptions in mapping.items():
        print(f"Processando categoria: {category}")
        for old_name, new_name in corruptions.items():
            for severity in range(1, 6):
                # Caminho da pasta antiga (severidade)
                old_severity_folder = os.path.join(base_path, f'{old_name}_severity_{severity}')
                
                # Caminho da nova pasta (severidade)
                new_severity_folder = os.path.join(new_base_path, category, new_name, str(severity))
                
                # Verifica se a pasta de severidade existe
                if os.path.exists(old_severity_folder):
                    # Itera sobre as subpastas (Anthracnose, Bacterial Canker, etc.)
                    for subfolder in os.listdir(old_severity_folder):
                        old_subfolder_path = os.path.join(old_severity_folder, subfolder)
                        new_subfolder_path = os.path.join(new_severity_folder, subfolder)
                        
                        # Cria a nova subpasta
                        os.makedirs(new_subfolder_path, exist_ok=True)
                        
                        # Copia as imagens da subpasta antiga para a nova subpasta
                        if os.path.isdir(old_subfolder_path):
                            for file_name in os.listdir(old_subfolder_path):
                                try:
                                    shutil.copy2(
                                        os.path.join(old_subfolder_path, file_name),
                                        os.path.join(new_subfolder_path, file_name))
                                    print(f'Copiado: {os.path.join(old_subfolder_path, file_name)} -> {os.path.join(new_subfolder_path, file_name)}')
                                except PermissionError:
                                    print(f'Erro de permissão: {os.path.join(old_subfolder_path, file_name)} (ignorado)')
                                except Exception as e:
                                    print(f'Erro ao copiar {os.path.join(old_subfolder_path, file_name)}: {e} (ignorado)')
                        else:
                            print(f'Item não é uma pasta: {old_subfolder_path}')
                else:
                    print(f'Pasta de severidade não encontrada: {old_severity_folder}')

# Executa a reorganização
reorganize_folders(base_path, new_base_path, mapping)

print("Reorganização concluída!")