#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, Text

from .BaseModel import BaseModel

class ProductType(BaseModel):
    __tablename__ = 'product_type'

    name = Column(Text(30), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

    def __iter__(self):
        yield 'id', self.id
        yield 'name', selt.name
