from django.db import models

class inforLogin(models.Model):
    usg_id = models.CharField(max_length=255)
    usg_network_ip = models.CharField(max_length=255)
    subscriber_mac = models.CharField(max_length=255)
    port_mapping = models.CharField(max_length=255)
    origin_server_url = models.CharField(max_length=255)

class inforLoginUser(models.Model):
    username = models.CharField(max_length=255)
    passwork = models.CharField(max_length=255)
