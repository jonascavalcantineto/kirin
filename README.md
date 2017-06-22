# kirin
Classe para envio de email

Utilização
=====================


- Quando o servidor de email estiver disponível na porta 25

1. Importar lib para projeto

- from kirin import Kirin

2. Estanciar classe, segue exemplo 

obj = Kirin(servidor_smtp, porta)

obj.from_addr = 

obj.to_addr = rcpt

obj.subject = subject

obj.mensage = mensage

obj.send_email()

