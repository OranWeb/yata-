"""
Copyright 2019 kivou.2000607@gmail.com

This file is part of yata.

    yata is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    yata is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with yata. If not, see <https://www.gnu.org/licenses/>.
"""
from django.utils import timezone

# from player.models import News
from player.models import Player
from faction.models import Member
from player.models import Message
from player.models import SECTION_CHOICES
from loot.models import NPC

from yata.handy import tsnow

# def news(request):
#     if request.session.get('player'):
#         tId = request.session["player"].get("tId")
#         player = Player.objects.filter(tId=tId).first()
#         news = News.objects.all().order_by("-date").first()
#         news = False if news in player.news_set.all() or news.date > (timezone.datetime.now(timezone.utc) + timezone.timedelta(weeks=2)) else news
#         return {"lastNews": news}
#     else:
#         return {}

def sectionMessage(request):
    section = request.get_full_path().split("/")[1]
    sectionMessages = Message.objects.filter(section__in=[section, "all"]).order_by("-date")
    return {"sectionMessages": sectionMessages}


def nextLoot(request):
    try:
        # get smaller due time
        to_late = tsnow() - (15 + 210) * 60
        next = NPC.objects.filter(show=True).filter(hospitalTS__gt=to_late).order_by('hospitalTS').first()
        if next is None:
            return {"nextLoot": ["All level V", 0, 0]}
        ts = max(next.lootTimings(lvl=4)["ts"], 0)
        return {"nextLoot": [next.name, next.tId, ts]}
    except BaseException:
        return {"nextLoot": ["Error", 0, 0]}
