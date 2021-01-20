# -*- coding: utf8 -*-

__author__ = 'thuytn'

import csv


class ForgotPasswordDto:
    def __init__(self, id, email):
        self.email = email
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
        objs.append(ForgotPasswordDto(r[0], r[1]))

    return objs
