import os

os.system("cls")

def calcular_inss(salario_base):
    if salario_base <= 1518.00:
        desconto = salario_base * 0.075
    elif salario_base <= 2793.88:
        desconto = salario_base * 0.09
    elif salario_base <= 4190.83:
        desconto = salario_base * 0.12
    elif salario_base <= 8157.41:
        desconto = salario_base * 0.14
    else:
        desconto = 951.62  
    return round(desconto, 2)

def calcular_irrf(salario_base):
    if salario_base <= 2428.80:
        desconto = 0
    elif salario_base <= 2826.65:
        desconto = salario_base * 0.075
    elif salario_base <= 3751.05:
        desconto = salario_base * 0.15
    elif salario_base <= 4664.68:
        desconto = salario_base * 0.225
    else:
        desconto = salario_base * 0.275
    return round(desconto, 2)

def calcular_vt(salario_base, optou_vt):
    if optou_vt.lower() == 's':
        return round(salario_base * 0.06, 2)
    return 0.0

def calcular_vr(valor_beneficio):
    return round(valor_beneficio * 0.20, 2)

def calcular_plano_saude(num_dependentes):
    return num_dependentes * 150.00

def processar_folha():
    print("--- Acesso ao Sistema ---")
    matricula = input("Matrícula: ")
    senha = input("Senha: ")
    
    print("\n--- Dados Financeiros ---")
    salario_base = float(input("Salário Base (R$): "))
    optou_vt = input("Deseja receber Vale Transporte? (s/n): ")
    valor_vr_empresa = float(input("Valor do Vale Refeição fornecido (R$): "))
    dependentes = int(input("Quantidade de dependentes: "))

    
    desc_inss = calcular_inss(salario_base)
    desc_irrf = calcular_irrf(salario_base)
    desc_vt = calcular_vt(salario_base, optou_vt)
    desc_vr = calcular_vr(valor_vr_empresa)
    desc_saude = calcular_plano_saude(dependentes)

    total_descontos = desc_inss + desc_irrf + desc_vt + desc_vr + desc_saude
    salario_liquido = salario_base - total_descontos

    print("\n" + "="*30)
    print(f"RESUMO DA FOLHA - Matrícula: {matricula}")
    print(f"Salário Bruto:   R$ {salario_base:>.2f}")
    print("-" * 30)
    print(f"(-) INSS:        R$ {desc_inss:>.2f}")
    print(f"(-) IRRF:        R$ {desc_irrf:>.2f}")
    print(f"(-) Vale Transporte: R$ {desc_vt:>.2f}")
    print(f"(-) Vale Refeição:  R$ {desc_vr:>.2f}")
    print(f"(-) Plano Saúde: R$ {desc_saude:>.2f}")
    print("-" * 30)
    print(f"SALÁRIO LÍQUIDO: R$ {salario_liquido:>.2f}")
    print("="*30)


if __name__ == "__main__":
    processar_folha()