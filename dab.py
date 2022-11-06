#!/usr/bin/env python3

from sqlalchemy import Table, Column, Integer, String, DateTime, Sequence, ForeignKey, create_engine, and_, MetaData
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class mydb():
    def __init__(self):
        self.engine = create_engine("sqlite:///:memory:", echo = True)
        self.meta = MetaData()

        self.users = Table("users", self.meta,
            Column('id', Integer, Sequence("user_id_seq"), primary_key = True),
            Column('name', String(50)),
        )

        self.travels = Table("travel", self.meta,
            Column('id', Integer, Sequence("travel_id_seq"), primary_key = True),
            Column('starttime', DateTime),
            Column('stops', String(50)),
        )

        self.bookings = Table("bookings", self.meta,
            Column('id', Integer, Sequence("booking_id_seq"), primary_key = True),
            Column('userid', Integer, ForeignKey(self.users.c.id)),
            Column('travelid', Integer, ForeignKey(self.travels.c.id)),
        )
        
        self.meta.create_all(self.engine)
        # creat session
        self.Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.session = self.Session()
        
    def __exit__(self, exc_type, exc_value, traceback):
        # delete session
        self.session.close()

    def createDB(self):
        self.session.execute(self.users.insert(), [
            {'name' : 'Abby'},
            {'name' : 'Body'},
            {'name' : 'Casy'},
            {'name' : 'Dewy'},
            {'name' : 'Eric'},
            {'name' : 'Fred'},
        ])

        self.session.execute(self.bookings.insert(), [
            {'userid' : 1, 'travelid' : 1},
            {'userid' : 2, 'travelid' : 2},
            {'userid' : 3, 'travelid' : 3},
            {'userid' : 4, 'travelid' : 4},
            {'userid' : 5, 'travelid' : 5},
            {'userid' : 6, 'travelid' : 6},
        ])

        self.session.execute(self.travels.insert(), [
            {'starttime' : datetime.fromisoformat('2020-03-11T06:04:00'), 'stops' : 'LLL AAA'},
            {'starttime' : datetime.fromisoformat('2020-04-12T11:05:00'), 'stops' : 'GGG AAA LLL'},
            {'starttime' : datetime.fromisoformat('2020-05-13T10:06:00'), 'stops' : 'BBB AAA LLL JJJ SSS'},
            {'starttime' : datetime.fromisoformat('2020-06-14T08:07:00'), 'stops' : 'AAA LLL'},
            {'starttime' : datetime.fromisoformat('2020-07-15T20:08:00'), 'stops' : 'ATL AAA BBB'},
            {'starttime' : datetime.fromisoformat('2020-08-16T09:09:00'), 'stops' : 'AAA CCC LLL'},        
        ])

    def queryBeforeStart(self, btime):
        _statement = select(self.users.c.name, self.travels.c.starttime, self.travels.c.stops).\
                        where(and_(self.bookings.c.userid == self.users.c.id, self.bookings.c.travelid == self.travels.c.id)).\
                        where(self.travels.c.starttime < datetime.fromisoformat(btime))

        return self.session.execute(_statement).fetchall()

    def queryWithStops(self, wstop):
        _search = "%{}%".format(wstop)
        _statement = select(self.users.c.name, self.travels.c.starttime, self.travels.c.stops).\
                        where(and_(self.bookings.c.userid == self.users.c.id, self.bookings.c.travelid == self.travels.c.id)).\
                        filter(self.travels.c.stops.like(_search))

        return self.session.execute(_statement).fetchall()
