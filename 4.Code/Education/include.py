#!/usr/local/bin/python
#-*- coding:utf-8 -*-

import httplib
import urllib
import datetime
import threading
import md5
import random
import os
import inspect
import hashlib
import base64
import pickle
import socket
import sys
import platform
import time
import json
import uuid
import re
import qrcode
import urllib2
import requests
import urlparse


from HsPlatform.Sms.HsSmsHelp import *
from HsPlatform.Sms.MobileRecord import *

# DJANGO 引用
from django.shortcuts import render,render_to_response
from django.http import  HttpResponse
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
from django.template import Template, Context
from HsEdu.models import *
from HsEdu.Api.PublicService import *
from HsShareData import *
