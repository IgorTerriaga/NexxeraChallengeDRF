from rest_framework import serializers


def validate_transaction(data):
    """Check data"""
    # global saldo_em_conta
    print("olha a data...", data)
    
    # print("--------------", saldo_em_conta)
    
    # aqui precisa testar se for maior que o valor em conta tbm
    if data["tipo"] == "D" and data["valor"]:  # > saldo_em_conta

        raise serializers.ValidationError(
            {
                "messagem": "Não é possível debitar um valor superior ao que a conta possui."
            }
        )
    if data["tipo"] == "D":
        # aqui eu pego o valor da transacao e subtraio do valor da conta
        # saldo_em_conta = saldo_em_conta - data["valor"]
        pass
    elif data["tipo"] == "C":
        # aqui eu pego o valor da transacao e adicione ao valor da conta
        # saldo_em_conta = saldo_em_conta + data["valor"]
        pass
    return data
