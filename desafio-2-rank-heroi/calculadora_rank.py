#CALCULADORA DE RANK

def calcular_rank(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas
   
    if saldo_vitorias  <= 10:
        rank = "Ferro"
    elif saldo_vitorias <= 20:
        rank = "Bronze"
    elif saldo_vitorias <= 50:
        rank = "Prata"
    elif saldo_vitorias <= 80:
        rank = "Ouro"
    elif saldo_vitorias <= 90:
        rank = "Diamante"
    elif saldo_vitorias <= 100:
        rank = "Lendário"
    else: 
        rank = "Imortal"

    return(f"O herói tem saldo de {saldo_vitorias} e está no nível de {rank}. ")
