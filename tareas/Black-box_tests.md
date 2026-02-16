Equivalence Partitioning
1. Function that validates credit card numbers.
| Entrada            | Resultado esperado              |
|--------------------|---------------------------------|
| 874392049320345    | Válido – Longitud entre 13 y 16 |
| 7890323473923      | Válido – Longitud igual a 13    |
| 9837873627384930   | Válido – Longitud igual a 16    |
| 876548987632       | Inválido – Longitud menor a 13  |
| 83749384900034800  | Inválido – Longitud mayor a 16  |
| 975438439483U7     | Inválido – Caracteres no numéricos |

2. Function that validates dates.
| Entrada      | Resultado esperado                 |
|--------------|------------------------------------|
| 4/5/2000     | Válido – Fecha entre 1900 y 2100   |
| 1/1/1900     | Válido – Primer fecha de 1900      |
| 12/31/2100   | Válido – Última fecha del 2100     |
| 7/20/1854    | Inválido – Fecha por debajo del rango |
| 1/1/2120     | Inválido – Fecha por arriba del rango |


3. Function that checks the eligibility of a passenger to book a flight.
| Edad | Frequent flyer | Resultado esperado              |
|------|----------------|---------------------------------|
| 20   | True           | Válido – Edad dentro del rango  |
| 30   | False          | Válido – Edad dentro del rango  |
| 17   | True           | Inválido – Edad por debajo del rango |
| 70   | False          | Inválido – Edad por arriba del rango |


4. Function that validates URLs.
| Entrada                               | Resultado esperado                                      |
|---------------------------------------|-----------------------------------------------------------|
| http://iteso.com                      | Válido – Inicia con http:// y dentro del rango de caracteres |
| https://instagram.com                 | Válido – Inicia con https:// y dentro del rango de caracteres |
| htp://starbucks.com                   | Inválido – El prefijo está mal                          |
| http://dejdededmkmkdnedi+255.com      | Inválido – Más de 255 caracteres                        |


Boundary Value Analysis

1. Function that calculates the eligibility of a person for a loan based on their income and credit score.
| Income       | Credit score | Resultado esperado |
|--------------|--------------|--------------------|
| $29,999.00   | 700          | No elegible        |
| $30,000.00   | 700          | secured loan       |
| $60,000.00   | 701          | standard loan      |
| $60,001.00   | 751          | premium loan       |
| $60,001.00   | 700          | standard loan      |
| $60,001.00   | 750          | standard loan      |


2. Function that determines the category of a product in an e-commerce system based on its price.
| Product price | Categoría |
|---------------|-----------|
| $9.00         | Ninguna   |
| $10.00        | A         |
| $30.00        | A         |
| $50.00        | A         |
| $51.00        | B         |
| $70.00        | B         |
| $100.00       | B         |
| $101.00       | C         |
| $150.00       | C         |
| $200.00       | C         |
| $201.00       | D         |


3. Function that calculates the cost of shipping for packages based on their weight and dimensions.
| Weight | Dimensions | Price |
|--------|------------|-------|
| 0.7 kg | 9 cm       | $5    |
| 1 kg   | 10 cm      | $5    |
| 1 kg   | 11 cm      | $10   |
| 5 kg   | 30 cm      | $10   |
| 3 kg   | 31 cm      | $20   |
| 6 kg   | 20 cm      | $20   |


Decision Table
1. Create the decision table for a system that provides weather advisories based on temperature and humidity.
| Temperatura | Humedad | Recomendación                                   |
|-------------|---------|-------------------------------------------------|
| 31          | 71      | High temperature and humidity. Stay hydrated.   |
| -1          | 71      | Low temperature. Don't forget your jacket!      |
| 15          | 71      | Sin recomendación                               |


2. Create the decision table for a system that authenticates users based on their username and password.
| Username | Password      | Resultado |
|----------|---------------|-----------|
| admin    | admin123      | Admin     |
| pedro    | contraseña77  | User      |
| juan     | password123   | Inválido  |
| carlos   | 123           | Inválido  |
