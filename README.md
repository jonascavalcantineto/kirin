# kirin
Classe para envio de email

Utilização
=====================


- Quando o servidor de email esta disponível na porta 25

1. Importar a lib para projeto

- from kirin import Kirin

2. Estanciar a classe como o exemplo abaixo

obj = Kirin(servidor_smtp, porta)

obj.from_addr = 

obj.to_addr = rcpt

obj.subject = subject

obj.mensage = mensage

obj.send_email()

