# -*- coding: utf-8 -*-
class Kirin(object):

    def __init__(self,server, con_port):
  		self._server = server
  		self._con_port = con_port
        self._from = None
        self._to = None
        self._subject = None
        self._msg = None

    @property
    def getFrom():
        return self._from

    @set.property
    def setFrom(value):
		self._from = value

    @property
    def getTo():
        return self._to

    @set.property
    def setTo(value):
		self._to = value

    @property
    def getSubject():
        return self._subject

    @set.property
    def setSubject(value):
    	self._subject = value

    @property
    def getMessage():
        return self._msg

    @set.property
    def setMessage(value):
        self._msg = value

    def send():
        pass
