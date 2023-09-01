#!/bin/bash

# Start Gunicorn server
gunicorn core.wsgi:application