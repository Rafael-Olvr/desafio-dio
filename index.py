nome_heroi = "Dragon Slayer"
xp_heroi = 8963

match xp_heroi:
    case xp_heroi if xp_heroi <= 1000:
        xp_heroi = "Ferro"
    case xp_heroi if xp_heroi <= 2000:
        xp_heroi = "Bronze"
    case xp_heroi if xp_heroi <= 5000:
        xp_heroi = "Prata"
    case xp_heroi if xp_heroi <=7000:
        xp_heroi = "Ouro"
    case xp_heroi if xp_heroi <= 8000:
        xp_heroi = "Platina"
    case xp_heroi if xp_heroi <= 9000:
        xp_heroi = "Ascendente"
    case xp_heroi if xp_heroi <= 10000:
        xp_heroi = "Imortal"
    case xp_heroi if xp_heroi >= 10001:
        xp_heroi = "Radiante"
    

print(f"O heroi de nome {nome_heroi} está no nível {xp_heroi}")