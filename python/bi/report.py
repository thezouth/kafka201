from datetime import date
from typing import Tuple
import sqlite3
import sys


def fecth_data(report_date: str):
    conn = sqlite3.connect('order-bi.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT product_id, SUM(amount) as total_amount,
               SUM(total_price) AS total_price
        FROM orders WHERE date = ? GROUP BY product_id
    ''', (report_date,))
    return cursor.fetchall()


def show_report(data: Tuple, report_date: str):
    print(f'Sales Report of `{report_date}`')
    print('=================================')
    
    print('Product'.ljust(10) + ' ' + 
          'Amount'.ljust(10) + ' ' +
          'Revenue'.ljust(10))
    
    for row in data:
        print(str(row[0]).ljust(10) + ' ' +
              '{:10.0f}'.format(row[1]) + ' ' +
              '{:10.2f}'.format(row[2])
        )


if __name__ == '__main__':
    report_date = sys.argv[1] if len(sys.argv) >= 2 else date.today().strftime('%Y-%m-%d')
    data = fecth_data(report_date)
    show_report(data,report_date)