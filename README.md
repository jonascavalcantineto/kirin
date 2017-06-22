# kirin
Classe para envio de email

Utilização
=====================

1. Importar para seu projeto
- from kirin import Kirin

2. Estanciar a classe como o exemplo abaixo

obj = Kirin(<servidor_smtp, <porta>)

obj.from_addr = <from>
obj.to_addr = <rcpt>
obj.subject = <subject>

obj.mensage = <mensage>

obj.send_email()

