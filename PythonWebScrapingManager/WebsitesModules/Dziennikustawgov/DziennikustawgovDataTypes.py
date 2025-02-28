import datetime

import attr

@attr.define
class DziennikustawgovDocument:
    title: str
    pdfUrl: str
    date: datetime
    position: int