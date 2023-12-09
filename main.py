from re import sub
from pprint import pprint
from csv import reader, writer


def fio(list_name, cycle):
    if len(list_name) == 3:
        for j in range(len(list_name)):
            row.pop(j)
            row.insert(j, name[j])
    if len(name) == 2:
        for j in range(len(list_name)):
            row.pop(j + cycle)
            row.insert(j + cycle, name[j])


def phone_num(li, fin_li):
    li = ','.join(li)
    pattern = r'(\+7|8)\s*\(*(\d{3})\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s*\(*([а-яё]*\.*(\s*)\d*)\)*'
    substitute = r'+7(\2)\3-\4-\5\7\6'
    result = sub(pattern, substitute, li)
    li = result.split(',')
    fin_li.append(li)


with open('phonebook_raw.csv', 'r', encoding='utf-8') as f1, open('phonebook.csv', 'w') as f2:
    rows = reader(f1, delimiter=',')
    contacts_list = list(rows)

    contacts_list1 = []
    for row in contacts_list:
        cyc = 0
        for i in range(3):
            name = row[i].split(' ')
            if len(name) == 1:
                cyc += 1
                continue
            fio(name, cyc)
            cyc += 1

        phone_num(row, contacts_list1)

    del_list = []
    for i in range(len(contacts_list1)):
        for j in range(len(contacts_list1)):
            if j <= i:
                continue
            a = set(contacts_list1[i][:3]) & set(contacts_list1[j][:3])
            if len(a) != 0:
                print(a, i, j)
                del_list.append(j)
                # print(contacts_list1[i])
                for n in range(len(contacts_list1[i])):
                    if contacts_list1[i][n] == '':
                        contacts_list1[i][n] = contacts_list1[j][n]
    [contacts_list1.pop(i) for i in sorted(del_list, reverse=True)]

    datawriter = writer(f2, delimiter=',')
    datawriter.writerows(contacts_list1)


