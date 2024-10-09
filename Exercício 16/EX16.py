def celsius_para_fahrenheit(celsius):
    """
    Converte uma temperatura em graus Celsius para Fahrenheit.

    :param celsius: Temperatura em graus Celsius (float)
    :return: Temperatura convertida em graus Fahrenheit (float)
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# Exemplo de uso da função
if __name__ == "__main__":
    # Testando a função com alguns valores
    temperaturas_celsius = [0, 100, 37, -40]

    for temp_c in temperaturas_celsius:
        temp_f = celsius_para_fahrenheit(temp_c)
        print(f"{temp_c}°C é igual a {temp_f:.1f}°F")