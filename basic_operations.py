#!/usr/bin/env python

class basic_operations:
        
    def basic_sum(self, a, b):
        return a + b

    def basic_subb(self, a, b):
        return a - b
        
    def basic_multiplication(self, a, b):
        return a * b
    
    def basic_division(self, a, b):
        if b == 0:
            return "division by zero"
        return a / b
