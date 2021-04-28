# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


"""CREATE TABLE "myapp_base" ("id" integer NOT NULL PRIMARY KEY 
                        AUTOINCREMENT, "Email" varchar(254) NOT NULL)"""
class base(models.Model):
    Email = models.EmailField()
    def __str__(self):
        return self.Email


"""CREATE TABLE "Web" ("id" integer NOT NULL PRIMARY KEY 
                    AUTOINCREMENT, "name" varchar(20) NOT NULL,
                    "password" varchar(20) NOT NULL, 
                    "repassword" varchar(20) NOT NULL, 
                    "Email_id" integer NOT NULL REFERENCES 
                    "myapp_base" ("id") DEFERRABLE INITIALLY 
                    DEFERRED)
"""
class webpage(models.Model):
    name = models.CharField(max_length=20)
    Email = models.ForeignKey(base, on_delete = models.CASCADE)
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)

#make it person
    class Meta:
        db_table = 'Web'


"""CREATE TABLE "contact" ("id" integer NOT NULL PRIMARY KEY 
                        AUTOINCREMENT, "fullname" varchar(20) NOT NULL, 
                        "msg" text NOT NULL, 
                        "Email_id" integer NOT NULL REFERENCES 
                        "myapp_base" ("id") DEFERRABLE INITIALLY 
                        DEFERRED)"""
class contact(models.Model):
    fullname = models.CharField(max_length=20)
    Email = models.ForeignKey(base, on_delete = models.CASCADE)
    msg = models.TextField(max_length=20)

    class Meta:
        db_table = 'contact'


"""CREATE TABLE "myapp_package" ("id" integer NOT NULL PRIMARY KEY 
                            AUTOINCREMENT, "pck_id" integer NOT NULL, 
                            "title" varchar(100) NOT NULL, 
                            "description" varchar(500) NOT NULL, 
                            "price" varchar(50) NOT NULL, 
                            "summary" text NULL)"""
class package(models.Model):
    pck_id = models.IntegerField(default = 101)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=50)
    summary = models.TextField(blank=True,null=True)


"""CREATE TABLE "myapp_payment" ("id" integer NOT NULL PRIMARY KEY 
                            AUTOINCREMENT, "pck_id" integer NOT NULL, 
                            "name" varchar(30) NOT NULL, 
                            "card_num" integer NOT NULL, 
                            "month" varchar(10) NOT NULL, 
                            "year" integer NOT NULL, 
                            "cvv" integer NOT NULL, 
                            "email_id" integer NOT NULL REFERENCES 
                            "myapp_base" ("id") DEFERRABLE INITIALLY 
                            DEFERRED)"""
class payment(models.Model):
    pck_id = models.IntegerField(default = 101)  #consider case for wrong id entered
    email = models.ForeignKey(base, on_delete = models.CASCADE)
    name = models.CharField(max_length = 30)
    card_num = models.IntegerField()
    month = models.CharField(max_length = 10)
    year = models.IntegerField()
    cvv = models.IntegerField()


