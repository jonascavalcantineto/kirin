# -*- coding: utf-8 -*-
import smtplib

class Kirin(object):


    def __init__(self, server, con_port):
  	     self._server = server
  	     self._con_port = con_port


    def getFromAddr(self):
        return self._from_addr

    def setFromAddr(self, valor):
        self._from_addr = valor

    from_addr = property(
                fget = getFromAddr,
                fset = setFromAddr)

    def getToAddr(self):
        return self._to_addr

    def setToAddr(self, valor):
        self._to_addr = valor
        
    to_addr = property(
              fget = getToAddr,
              fset = setToAddr)

    
    def getSubject(self):
        return self._subject

    def setSubject(self, valor):
        self._subject = valor
        
    subject = property(
              fget = getSubject,
              fset = setSubject)

    def getMensage(self):
        return self._mensage

    def setMensage(self, valor):
        self._mensage = valor
        
    mensage = property(
              fget = getMensage,
              fset = setMensage)

    def send_email(self):

        if self._con_port == "":
            self._con_port = 25

        try:
            server = smtplib.SMTP(self._server, self._con_port)

            msg = 'Subject: {}\n\n{}'.format(self.subject, self.mensage)

            server.sendmail(self.from_addr, self.to_addr, msg)
            server.quit()
            print("Successfully sent email")

        except smtplib.SMTPException as e:
            raise e
            print(e + " sent email")
        
