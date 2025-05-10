import os

# Caminho para a pasta principal
pasta_principal = "..\BancosCorrompidaNovaEstrutura"

# Mapeamento de nomes para o novo formato
mapa_corrupcoes = {
    "brightness": "Brightness",
    "contrast": "Contrast",
    "defocus_blur": "Defocus Blur",
    "elastic_transform": "Elastic",
    "fog": "Fog",
    "frost": "Frost",
    "gaussian_blur": "Gaussian Blur",
    "gaussian_noise": "Gaussian Noise",
    "glass_blur": "Glass Blur",
    "impulse_noise": "Impulse Noise",
    "jpeg_compression": "JPEG",
    "motion_blur": "Motion Blur",
    "pixelate": "Pixelate",
    "saturate": "Saturate",
    "shot_noise": "Shot Noise",
    "snow": "Snow",
    "spatter": "Spatter",
    "speckle_noise": "Speckle Noise",
    "zoom_blur": "Zoom Blur"
}

# Renomear apenas as pastas principais
for pasta in os.listdir(pasta_principal):
    pasta_caminho = os.path.join(pasta_principal, pasta)
    if os.path.isdir(pasta_caminho):
        # Dividir o nome da pasta para identificar a corrupção e severidade
        partes = pasta.rsplit("_", 1)
        if len(partes) == 2:
            corrupcao, severidade = partes
            novo_nome_corrupcao = mapa_corrupcoes.get(corrupcao, corrupcao)
            novo_nome = f"{novo_nome_corrupcao}_severity_{severidade}"

            # Renomear a pasta
            novo_caminho = os.path.join(pasta_principal, novo_nome)
            os.rename(pasta_caminho, novo_caminho)

print("Pastas principais renomeadas com sucesso!")
