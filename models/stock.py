# coding: utf-8

from sqlalchemy import BigInteger, Column, Date, DateTime, Numeric, String
from . import Base


class Stock(Base):
    """ Model for stock basic infomations. """
    __tablename__ = 'stock'

    market = Column(String(16), primary_key=True)
    code = Column(String(10), primary_key=True)
    name = Column(String(16), nullable=False)

    pe = Column(Numeric(precision=8, scale=2))
    market_value = Column(BigInteger)
    circulating_value = Column(BigInteger)
    outstanding_shares = Column(BigInteger)
    tradable_shares = Column(BigInteger)

    asset_value_per_share = Column(Numeric(precision=8, scale=3))
    gross_profit_margin = Column(Numeric(precision=8, scale=2))
    pb = Column(Numeric(precision=8, scale=2))
    eps = Column(Numeric(precision=8, scale=3))
    roe = Column(Numeric(precision=8, scale=2))
    debt_ratio = Column(Numeric(precision=8, scale=2))

    revenue = Column(BigInteger)
    revenue_growth = Column(Numeric(precision=8, scale=2))
    net_profit = Column(BigInteger)
    net_profit_growth = Column(Numeric(precision=8, scale=2))
    retained_earnings_per_share = Column(Numeric(precision=8, scale=3))

    pinyin = Column(String(16))
    full_name = Column(String(32))
    status = Column(String(16))
    listing_date = Column(Date)

    update_time = Column(DateTime)
