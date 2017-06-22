# kirin
Classe python para envio de email 

Welcome Python
==============
Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly brackets or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than might be used in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale.

Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library.

Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation.

Getting Started
===============

1. Importar lib para projeto
	from kirin import Kirin

2. Example 
	obj = Kirin(servidor_smtp, porta)   
	obj.from_addr = from@
	obj.to_addr = rcpt@
	obj.subject = subject
	obj.mensage = mensage
	obj.send_email()

