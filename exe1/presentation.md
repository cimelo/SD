%title: Exercício Complementar 1
%author: Caio Ian Rozendo Silva de Melo
%date: 2021-12-06

-> Questão 2.a <-
=========

Quando os polinômios a(x) e b(x) tem graus deg(a) e deg(b), respectivamente, o polinômio c(x) tem necessariamente grau deg(c) = deg(a) + deg(b)? Justifique.

-------------------------------------------------

-> Resposta <-
=========

Não. Pois, seja r*x^deg(a) e s*x^deg(b), como as operações são feitas módulo n, caso (r*s)(mod n) == 0, então, deg(c) < deg(a)+deg(b).

-------------------------------------------------

-> Questão 2.b <-
=========

Realize um paralelo entre o produto implementado pelo programa e a operação de convolução linear também avaliada módulo n.

-------------------------------------------------


-> Resposta <-
=========

A definição de uma operação de convolução linear é dada por: f(n)*g(n) = Sum(k=-inf, inf) f(k)*g(n-k). Logo, tanto a multiplicação de polinômios quanto a convolução são multiplicação de funções, que são bem definidas em seus respectivos domínios.
