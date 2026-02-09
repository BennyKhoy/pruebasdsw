# Casos de Prueba: Ejercicios 1 a 5

## Ejercicio 1: Identificación de Números
**Caso 1:** Número 5 -> Resultado esperado: Positive.
**Caso 2:** Número -4 -> Resultado esperado: Negative.
**Caso 3:** Número 0 -> Resultado esperado: Zero.

## Ejercicio 2: Validación de Contraseñas
**Caso 1:** Entrada "Prueba1232!" -> Resultado esperado: Válido.
**Caso 2:** Entrada "P1$r" -> Resultado esperado: Inválido (Longitud insuficiente).
**Caso 3:** Entrada "prueba1232$" -> Resultado esperado: Inválido (Falta mayúscula).
**Caso 4:** Entrada "PRUEBA1232$" -> Resultado esperado: Inválido (Falta minúscula).
**Caso 5:** Entrada "Pruebaaa$" -> Resultado esperado: Inválido (Falta dígito).
**Caso 6:** Entrada "Prueba12321" -> Resultado esperado: Inválido (Falta carácter especial).

## Ejercicio 3: Cálculo de Descuento por Monto
**Caso 1:** Monto 50 -> Resultado esperado: 0% de descuento.
**Caso 2:** Monto 100 -> Resultado esperado: 10% de descuento.
**Caso 3:** Monto 200 -> Resultado esperado: 10% de descuento.
**Caso 4:** Monto 500 -> Resultado esperado: 10% de descuento.
**Caso 5:** Monto 1000 -> Resultado esperado: 20% de descuento.

## Ejercicio 4: Procesamiento de Órdenes
**Caso 1:** Cantidad 1 (Rango 1-5) -> Resultado esperado: 0% de descuento.
**Caso 2:** Cantidad 5 (Rango 1-5) -> Resultado esperado: 0% de descuento.
**Caso 3:** Cantidad 6 (Rango 6-10) -> Resultado esperado: 5% de descuento.
**Caso 4:** Cantidad 10 (Rango 6-10) -> Resultado esperado: 5% de descuento.
**Caso 5:** Cantidad 20 (Rango > 10) -> Resultado esperado: 10% de descuento.

## Ejercicio 5: Costos de Envío
**Caso 1:** Envío Estándar, Peso 3kg -> Resultado esperado: $10.
**Caso 2:** Envío Estándar, Peso 5kg -> Resultado esperado: $10.
**Caso 3:** Envío Estándar, Peso 8kg -> Resultado esperado: $15.
**Caso 4:** Envío Estándar, Peso 10kg -> Resultado esperado: $15.
**Caso 5:** Envío Estándar, Peso 15kg -> Resultado esperado: $20.
**Caso 6:** Envío Express, Peso 3kg -> Resultado esperado: $20.
**Caso 7:** Envío Express, Peso 5kg -> Resultado esperado: $20.
**Caso 8:** Envío Express, Peso 8kg -> Resultado esperado: $30.
**Caso 9:** Envío Express, Peso 10kg -> Resultado esperado: $30.
**Caso 10:** Envío Express, Peso 15kg -> Resultado esperado: $40.