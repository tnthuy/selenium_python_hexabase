import csv
import json
import xlrd
import xlwt


class ExcelFieldDto:
    def __init__(self, header_name, field_name):
        self.header_name = header_name
        self.field_name = field_name


# ---------------------------------------- Excel ----------------------------------------#
def get_column_index_dict_for_excel(first_row_in_excel, excel_field_dto_list):
    column_index_dict = {}
    for index, header_name in enumerate(first_row_in_excel):
        for column in excel_field_dto_list:
            if header_name.value == column.header_name:
                column_index_dict[index] = column.field_name
    return column_index_dict


def get_json_array_from_excel(sheet, num_row, column_index_dict):
    json_array = []
    for index_row in range(1, num_row):
        json_object = {}
        for column_index in column_index_dict:
            json_object[column_index_dict[column_index]] = sheet.cell_value(index_row, column_index)
        json_array.append(json_object)
    json_array = json.dumps(json_array)
    return json_array


def get_data_from_excel(file_path_excel, sheet_name, excel_field_dto_list, test_dto_class):
    print("get_data_from_excel: " + sheet_name + " working...")
    wb = xlrd.open_workbook(file_path_excel)
    sheet = wb.sheet_by_name(sheet_name)
    first_row_in_excel = sheet.row(0)
    num_row = sheet.nrows

    column_index_dict = get_column_index_dict_for_excel(first_row_in_excel, excel_field_dto_list)
    json_array = get_json_array_from_excel(sheet, num_row, column_index_dict)

    dto_list = json.loads(json_array, object_hook=test_dto_class.custom_dto_decoder)
    print("get_data_from_excel: from sheet " + sheet_name + " finished...")
    return dto_list


# ---------------------------------------- CSV ----------------------------------------#
def get_column_index_dict_for_csv(first_row_in_excel, excel_field_dto_list):
    column_index_dict = {}
    for index, header_name in enumerate(first_row_in_excel):
        for column in excel_field_dto_list:
            if header_name == column.header_name:
                column_index_dict[index] = column.field_name
    return column_index_dict


def get_json_array_from_csv(file_path_csv, excel_field_dto_list):
    f = open(file_path_csv)
    csv_reader_object = csv.reader(f)

    first_row_in_csv = next(csv_reader_object)
    column_index_dict = get_column_index_dict_for_csv(first_row_in_csv, excel_field_dto_list)

    json_array = []
    for index_row, line in enumerate(csv_reader_object):
        json_object = {}
        for column_index in column_index_dict:
            json_object[column_index_dict[column_index]] = line[column_index]
        json_array.append(json_object)
    json_array = json.dumps(json_array)
    f.close()
    return json_array


def get_data_from_csv(file_path_csv, excel_field_dto_list, test_dto_class):
    json_array = get_json_array_from_csv(file_path_csv, excel_field_dto_list)

    dto_list = json.loads(json_array, object_hook=test_dto_class.custom_dto_decoder)
    return dto_list


# ---------------------------------------- Convert data for API testing ----------------------------------------#
def next_line_for_convert_two_to_one(maxs, at):
    maxs_lenght = len(maxs) - 1
    for i in range(maxs_lenght, -1, -1):
        if at[i] < (maxs[i] - 1):
            t = at[i]
            t += 1
            at[i] = t
            break
        else:
            at[i] = 0
    return at


def convert_two_dimensional_to_one_dimensional(list_list_input):
    tests_data_dto = []
    sizes_per_sheet = []
    for sheet in list_list_input:
        sizes_per_sheet.append(len(sheet))

    total = 1
    for i in range(0, len(sizes_per_sheet)):
        total *= sizes_per_sheet[i]

    at = []
    for integers in list_list_input:
        at.append(0)

    for i in range(0, total):
        test_data_dto = []
        x = len(list_list_input)
        for index in range(0, len(list_list_input)):
            dto = list_list_input[index][at[index]]
            test_data_dto.append(dto)
        tests_data_dto.append(test_data_dto)
        at = next_line_for_convert_two_to_one(sizes_per_sheet, at)
    return tests_data_dto


# ---------------------------------------- Report ----------------------------------------#
def export_report(results, file_path, sheet_name, header):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheet_name)

    row_header = 0
    for column_index, column in enumerate(header):
        sheet.write(row_header, column_index, column)

    for row_index, row in enumerate(results):
        for column_index, column in enumerate(row):
            sheet.write(row_index + 1, column_index, str(column))
    workbook.save(file_path)

# if __name__ == '__main__':
