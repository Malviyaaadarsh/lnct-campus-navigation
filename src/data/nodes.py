node_mapping = {
    1: 'LNCT Main Gate', 2: 'Hanuman Temple', 3: 'Bus Stand', 4: 'Lakshmi Narain Block', 5: 'Tripuri Hostel',
    6: 'LNCT New Building', 7: 'Kalyani Hostel', 8: 'Mahismati Hostel', 9: 'Saryu Boys Hostel', 10: 'LNCTE Building',
    11: 'Oxygen Plant', 12: 'Charles Babbage Block', 13: 'Vishwanathan Anand Block', 14: 'ICICI ATM', 15: 'Canteen',
    16: 'Jagdish Chandra Bose Block (LNCTS New)', 17: 'Ramnath Guha Block (MCA)',
    18: 'MS Swaminathan Block (LNCTU School of Agri.Sci)', 19: 'Ground 1', 20: 'Sir Vishveshwaraya Block (LNCTS Old)',
    21: 'LNCP', 22: 'Newton Block (Science)', 23: 'Vishwakarma Block (CME)', 24: 'Newton Block',
    25: 'Aryabhatta Auditorium', 26: 'Central Library', 27: 'Ground 2', 28: 'Ratnapura Hostel',
    29: 'Ground 3', 30: 'LNCTE Canteen'
}

node_positions = {
   1: (0.8, -5.6), 2: (-1.6, -5), 3: (4.5, -5.3), 4: (-8.9, -3.9), 5: (0, 0), 6: (-5.7, 0.6),
    7: (-0.3, 2.5), 8: (-0.1, 4.5), 9: (5.1, 5.1), 10: (11.9, 0.4), 11: (11.4, -5.4),
    12: (-15.4, 1), 13: (-24.3, 0.2), 14: (-26.1, 0.3), 15: (-27.8, 0.8), 16: (-29.8, 4.3),
    17: (-36.6, 4.3), 18: (-42.8, 4.3), 19: (-24.1, 3.9), 20: (-29.8, 6.3), 21: (-28.7, 6.2),
    22: (-29.8, 7.9), 23: (-7.3, 5.2), 24: (-8.5, 2.2), 25: (4.5, -3.5), 26: (-15.4, 1.9),
    27: (4.4, 2.4), 28: (4.5, 0), 29: (9.6, 2.6), 30: (12, 5)
}
reverse_mapping = {name: num for num, name in node_mapping.items()}
# print(reverse_mapping)