#!/usr/bin/env python
# -*- coding: utf8 -*-

__author__ = 'thuytn'

import csv


class LoginDto:
    def __init__(self, id, username, password):
        self.password = password
        self.username = username
        self.id = id


def get_csv_data(csv_path):
    """
    read test data from csv and return as list

    @type csv_path: string
    @param csv_path: some csv path string
    @return list
    """
    rows = []
    csv_data = open(str(csv_path))
    content = csv.reader(csv_data)

    # skip header line
    next(content, None)

    # add rows to list
    for row in content:
        rows.append(row)
    objs = []
    for r in rows:
        objs.append(LoginDto(r[0], r[1], r[2]))

    return objs
