print("==================================== SMARTWEB ==============================")

valor = float(input("Digite o valor do saque: "));

if valor <= 0:
    print("Valor inválido!")
else:
    nota200 = valor // 200;
    resto = valor % 200;
    
    nota100 = valor // 100;
    resto = valor % 100;

    nota50 = valor // 50;
    resto = valor % 50;

    nota20 = valor // 20;
    resto = valor % 20;

    nota10 = valor // 10;
    resto = valor % 10;

    nota5 = valor // 5;
    resto = valor % 5;

    nota2 = valor // 2;
    resto2 = valor % 2;

    ("\nRetire o dinheiro R$: ")
    print("----------------------------------");
    print("Receba notas de R$ 200: : {nota200}");
    print("Receba notas de R$ 100: : {nota100}");
    print("receba notas de R$ 50: : {nota50}");
    print("Retira notas de R$ 20: : {nota20}");
    print("Reitra notas de R$ 10: : {nota10}");
    print("Retira notas de R$ 5: : {nota5}");
    print("Retira notas de R$ 2: : {nota2}");

    if("resto > 0"):
        print("valor restante não disponível é: R$ {resto}");