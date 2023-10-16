#!/usr/bin/python3
"""Managing storage of files and reloading"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
