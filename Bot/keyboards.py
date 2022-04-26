import telebot
from telebot import *
Keyboard_First = types.InlineKeyboardMarkup(row_width = 1)
btn_f1 = types.InlineKeyboardButton('Извлечь информацию', callback_data='extract')
btn_f2 = types.InlineKeyboardButton('Изменить информацию', callback_data='change')
btn_f3 = types.InlineKeyboardButton('Настройки бота', callback_data='settings')
Keyboard_First.add(btn_f1, btn_f2, btn_f3)

Keyboard_Extract = types.InlineKeyboardMarkup(row_width = 1)
btn_e1 = types.InlineKeyboardButton('По иону', callback_data='eon')
btn_e2 = types.InlineKeyboardButton('По серии', callback_data='series')
btn_e3 = types.InlineKeyboardButton('По объекту', callback_data='object')
Keyboard_Extract.add(btn_e1, btn_e2, btn_e3)

Keyboard_Lists = types.InlineKeyboardMarkup(row_width = 1)
btn_l1 = types.InlineKeyboardButton('Data', callback_data='list_1')
btn_l2 = types.InlineKeyboardButton('Timing', callback_data='list_2')
btn_l3 = types.InlineKeyboardButton('Информация по иону', callback_data='list_3')
Keyboard_Lists.add(btn_l1, btn_l2, btn_l3)

Keyboard_Action_with_list = types.InlineKeyboardMarkup(row_width = 1)
btn_a1 = types.InlineKeyboardButton('Добавить', callback_data='add')
btn_a2 = types.InlineKeyboardButton('Изменить', callback_data='replace')
Keyboard_Action_with_list.add(btn_a1, btn_a2)

Keyboard_Sure = types.InlineKeyboardMarkup(row_width = 1)
btn_s1 = types.InlineKeyboardButton('Да', callback_data='yes')
btn_s2 = types.InlineKeyboardButton('Нет', callback_data='no')
Keyboard_Sure.add(btn_s1, btn_s2)

Keyboard_Column = types.InlineKeyboardMarkup(row_width = 1)
btn_c1 = types.InlineKeyboardButton('Столбец 1', callback_data='column_1')
btn_c2 = types.InlineKeyboardButton('Столбец 2', callback_data='column_2')
Keyboard_Column.add(btn_c1, btn_c2)

Keyboard_Eon = types.InlineKeyboardMarkup(row_width = 1)
btn_eo1 = types.InlineKeyboardButton('1', callback_data='eon_1')
btn_eo2 = types.InlineKeyboardButton('2', callback_data='eon_2')
btn_eo3 = types.InlineKeyboardButton('3', callback_data='eon_3')
btn_eo4 = types.InlineKeyboardButton('4', callback_data='eon_4')
Keyboard_Eon.add(btn_eo1, btn_eo2, btn_eo3, btn_eo4)

Keyboard_Prot = types.InlineKeyboardMarkup(row_width = 1)
btn_p1 = types.InlineKeyboardButton('Нестандартный протокол', callback_data='prot_1')
btn_p2 = types.InlineKeyboardButton('Протокол допуска', callback_data='prot_2')
btn_p3 = types.InlineKeyboardButton('Протокол мониторинга', callback_data='prot_3')
Keyboard_Prot.add(btn_p1, btn_p2, btn_p3)

Keyboard_Extension = types.InlineKeyboardMarkup(row_width = 1)
btn_ex1 = types.InlineKeyboardButton('В zip', callback_data='to_zip')
btn_ex2 = types.InlineKeyboardButton('В rar', callback_data='to_rar')
btn_ex3 = types.InlineKeyboardButton('Без архива', callback_data='to_file')
Keyboard_Extension.add(btn_ex1, btn_ex2, btn_ex3)

Keyboard_Send = types.InlineKeyboardMarkup(row_width = 1)
btn_se1 = types.InlineKeyboardButton('В этот чат', callback_data='ins_chat')
btn_se2 = types.InlineKeyboardButton('На почту', callback_data='ins_mail')
Keyboard_Send.add(btn_se1, btn_se2)

Keyboard_Settings = types.InlineKeyboardMarkup(row_width = 1)
btn_se1 = types.InlineKeyboardButton('Отправка файлов', callback_data='sending_files')
btn_se2 = types.InlineKeyboardButton('Код доступа', callback_data='password')
btn_se3 = types.InlineKeyboardButton('Ссылка на таблицу', callback_data='link_to_table')
Keyboard_Settings.add(btn_se1, btn_se2, btn_se3)