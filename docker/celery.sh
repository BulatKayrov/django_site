#!/bin/bash

celery -A app_site worker -B --loglevel=info