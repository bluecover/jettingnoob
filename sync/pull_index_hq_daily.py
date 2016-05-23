# coding: utf8

from datetime import date, time
from crawler.sina_finance.hq_last import hq_last
from models import HQ, Session, HSIndex
from indicator.basic import change_percent

index_code_to_sync = [
    '000001',
    '000003',
    '000016',
    '000300',
    '399001',
    '399006',
    '399102'
]


def pull_index_last_hq(index):
    hq = hq_last(index.market, index.code)
    from_date = to_date = date.today()
    change = hq['price'] - hq['pre_close']
    change_pct = change_percent(hq['price'], hq['pre_close'])

    hq_today = HQ(
        market=index.market,
        code=index.code,
        from_date=from_date,
        to_date=to_date,
        from_time=time(hour=9, minute=15),
        to_time=time(hour=15),
        period='day_1',
        name=index.short_name,
        open=hq['open'],
        close=hq['price'],
        low=hq['low'],
        high=hq['high'],
        pre_close=hq['pre_close'],
        change=change,
        change_percent=change_pct,
        volume=hq['volume'],
        amount=hq['amount']
    )

    ss = Session()
    ss.merge(hq_today)
    ss.commit()


if __name__ == '__main__':
    s = Session()
    for index in s.query(HSIndex).filter(HSIndex.code.in_(index_code_to_sync)).all():
        pull_index_last_hq(index)
