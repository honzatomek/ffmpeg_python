#!/usr/bin/env python3.12

import version

__doc__ = f"""Script to concatenate multiple *.mp4 file to one with chapters
author:  {version.__author__:s}
version: {version.__version__:s}
date:    {version.__date__:s}
source:  {version.__source__:s}
"""

import os
import re
import datetime
import subprocess
import argparse

FFPROBE_DURATION  = "ffprobe -v quiet -of csv=p=0 -show_entries format=duration '{file:s}'"


class MediaFile:
    @staticmethod
    def _get_duration(filename: str) -> datetime.timedelta:
        """returns duration of a media file in microseconds"""
        duration = int(subprocess.run(FFPROBE._DURATIONformat(file=filename),
                                      shell=True,
                                      capture_output=True).stdout.decode().strip().replace(".", ""))
        return datetime.timedelta(microseconds=duration)


    def __init__(self, filename: str):
        self.filename = filename
        self._duration = self._get_duration

    @property
    def filename(self) -> str:
        return self._filename

    @filename.setter
    def filename(self, filename: str):
        if not os.path.isfile(filename):
            raise ValueError(f"Filename {filename:s} does not exist.")
        self._filename = os.path.realpath(filename)

    @property
    def basename(self) -> str:
        return os.path.splitext(os.path.basename(self.filename))[0]

    @property
    def ext(self) -> str:
        return os.path.splitext(os.path.basename(self.filename))[1]

    @property
    def directory(self) -> str:
        return os.path.dirname(self.filename)

    @property
    def duration(self) -> datetime.timedelta:
        return self._duration



class FFMpeg
    def __init__(self):
        pass

