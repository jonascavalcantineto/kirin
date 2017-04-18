# -*- coding: utf-8 -*-
class Kirin(object):

    def __init__(self,server, con_port):
  		self._server = server
  		self._con_port = con_port


    @property
    def from_addr(self):
        return self.from_addr

    @from_addr.setter
    def from_addr(self,value):
		self.from_addr = value

    @property
    def to_addr(self):
        return self.to_addr

    @to_addr.setter
    def to_addr(self,value):
		self.to_addr = value

    @property
    def subject(self):
        return self.subject

    @subject.setter
    def Subject(self,value):
    	self.subject = value

    @property
    def message(self):
        return self.msg

    @message.setter
    def message(self,value):
        self.msg = value

    def send_email(self):
        print self._con_port
        if self._con_port == 587:
            return "587";
        else:
            return "25";
