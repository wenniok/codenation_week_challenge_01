from datetime import datetime, timedelta

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

TAXA_PERMANENTE = 0.36
TAXA_MINUTO = 0.09


def calcula_valor(start, end):
    start = datetime.fromtimestamp(start)
    end = datetime.fromtimestamp(end)
    total = TAXA_PERMANENTE

    while start < end and (end - start).total_seconds() >= 60:
        if start.hour < 22 and start.hour >= 6:
            total = total + TAXA_MINUTO
        start = start + timedelta(minutes=1)
    return round(total, 2)


def classify_by_phone_number(records):
    lista_saida = []
    for i in records:
        indice = None
        existe = False
        valor = calcula_valor(i["start"], i["end"])      
        
        for j in range(len(lista_saida)):
            if lista_saida[j]["source"] == i["source"]:
                existe = True
                indice = j

        if existe:
            lista_saida[indice]["total"] = round(lista_saida[indice]["total"] + valor, 2)

        else:
            aux = {"source": i["source"], "total": round(valor, 2)}
            lista_saida.append(dict(aux))
    return sorted(lista_saida, key=lambda k : k['total'], reverse=True)

print(classify_by_phone_number(records))