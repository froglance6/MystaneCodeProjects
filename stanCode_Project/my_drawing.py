"""
File: my_drawing
Name: 謝昱騰
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon
from campy.graphics.gwindow import GWindow


window = GWindow(800, 600)


def main():
    """
    Snorlax is the cutest pokemon. It has big body and always yawning.
    I believe everyone love it.
    """
    body()
    foot()
    head()
    lfinger()
    rfinger()
    toe()


def body():
    hand1 = GOval(350, 100)
    hand1.filled = True
    hand1.fill_color = 'darkcyan'
    hand1.color = 'darkcyan'
    window.add(hand1, 70, 180)
    hand2 = GOval(350, 100)
    hand2.filled = True
    hand2.fill_color = 'darkcyan'
    hand2.color = 'darkcyan'
    window.add(hand2, 360, 180)
    foot1 = GOval(200, 200)
    foot1.filled = True
    foot1.fill_color = 'darkcyan'
    foot1.color = 'darkcyan'
    window.add(foot1, 170, 310)
    foot2 = GOval(200, 200)
    foot2.filled = True
    foot2.fill_color = 'darkcyan'
    foot2.color = 'darkcyan'
    window.add(foot2, 400, 310)
    body2 = GOval(420, 360)
    body2.filled = True
    body2.fill_color = 'darkcyan'
    body2.color = 'darkcyan'
    window.add(body2, 180, 150)
    body3 = GOval(350, 310)
    body3.filled = True
    body3.fill_color = 'antiquewhite'
    body3.color = 'antiquewhite'
    window.add(body3, 210, 210)


def foot():
    foot3 = GOval(110, 150)
    foot3.filled = True
    foot3.fill_color = 'antiquewhite'
    window.add(foot3, 140, 390)
    foot4 = GOval(110, 150)
    foot4.filled = True
    foot4.fill_color = 'antiquewhite'
    window.add(foot4, 510, 390)
    foot5 = GOval(60, 90)
    foot5.filled = True
    foot5.fill_color = 'tan'
    foot5.color = 'tan'
    window.add(foot5, 170, 430)
    foot6 = GOval(60, 90)
    foot6.filled = True
    foot6.fill_color = 'tan'
    foot6.color = 'tan'
    window.add(foot6, 530, 430)


def head():
    ear1 = GPolygon()
    ear1.add_vertex((470, 30))
    ear1.add_vertex((500, 110))
    ear1.add_vertex((420, 65))
    ear1.filled = True
    ear1.fill_color = 'darkcyan'
    ear1.color = 'darkcyan'
    window.add(ear1)
    ear2 = GPolygon()
    ear2.add_vertex((310, 30))
    ear2.add_vertex((280, 110))
    ear2.add_vertex((360, 65))
    ear2.filled = True
    ear2.fill_color = 'darkcyan'
    ear2.color = 'darkcyan'
    window.add(ear2)
    head1 = GOval(260, 200)
    head1.filled = True
    head1.fill_color = 'darkcyan'
    head1.color = 'darkcyan'
    window.add(head1, 260, 60)
    head2 = GOval(220, 160)
    head2.filled = True
    head2.fill_color = 'antiquewhite'
    window.add(head2, 280, 105)
    head3 = GPolygon()
    head3.add_vertex((390, 140))
    head3.add_vertex((340, 100))
    head3.add_vertex((440, 100))
    head3.filled = True
    head3.fill_color = 'darkcyan'
    head3.color = 'darkcyan'
    window.add(head3)
    eye1 = GArc(120, 180, 210, 90)
    window.add(eye1, 300, 140)
    eye2 = GArc(120, 180, 240, 90)
    window.add(eye2, 400, 140)
    mouse1 = GArc(120, 180, 210, 120)
    window.add(mouse1, 340, 200)
    teeth1 = GPolygon()
    teeth1.add_vertex((355, 225))
    teeth1.add_vertex((345, 235))
    teeth1.add_vertex((360, 240))
    teeth1.filled = True
    teeth1.fill_color = 'white'
    window.add(teeth1)
    teeth2 = GPolygon()
    teeth2.add_vertex((428, 225))
    teeth2.add_vertex((438, 235))
    teeth2.add_vertex((423, 240))
    teeth2.filled = True
    teeth2.fill_color = 'white'
    window.add(teeth2)


def lfinger():
    lfinger1 = GPolygon()
    lfinger1.add_vertex((73, 204))
    lfinger1.add_vertex((84, 210))
    lfinger1.add_vertex((77, 218))
    lfinger1.filled = True
    lfinger1.fill_color = 'white'
    window.add(lfinger1)
    lfinger2 = GPolygon()
    lfinger2.add_vertex((65, 215))
    lfinger2.add_vertex((77, 218))
    lfinger2.add_vertex((70, 225))
    lfinger2.filled = True
    lfinger2.fill_color = 'white'
    window.add(lfinger2)
    lfinger3 = GPolygon()
    lfinger3.add_vertex((70, 225))
    lfinger3.add_vertex((60, 230))
    lfinger3.add_vertex((70, 235))
    lfinger3.filled = True
    lfinger3.fill_color = 'white'
    window.add(lfinger3)
    lfinger4 = GPolygon()
    lfinger4.add_vertex((73, 256))
    lfinger4.add_vertex((84, 250))
    lfinger4.add_vertex((77, 242))
    lfinger4.filled = True
    lfinger4.fill_color = 'white'
    window.add(lfinger4)
    lfinger5 = GPolygon()
    lfinger5.add_vertex((65, 245))
    lfinger5.add_vertex((77, 242))
    lfinger5.add_vertex((70, 235))
    lfinger5.filled = True
    lfinger5.fill_color = 'white'
    window.add(lfinger5)


def rfinger():
    rfinger1 = GPolygon()
    rfinger1.add_vertex((707, 204))
    rfinger1.add_vertex((696, 210))
    rfinger1.add_vertex((703, 218))
    rfinger1.filled = True
    rfinger1.fill_color = 'white'
    window.add(rfinger1)
    rfinger2 = GPolygon()
    rfinger2.add_vertex((715, 215))
    rfinger2.add_vertex((703, 218))
    rfinger2.add_vertex((710, 225))
    rfinger2.filled = True
    rfinger2.fill_color = 'white'
    window.add(rfinger2)
    rfinger3 = GPolygon()
    rfinger3.add_vertex((710, 225))
    rfinger3.add_vertex((720, 230))
    rfinger3.add_vertex((710, 235))
    rfinger3.filled = True
    rfinger3.fill_color = 'white'
    window.add(rfinger3)
    rfinger4 = GPolygon()
    rfinger4.add_vertex((707, 256))
    rfinger4.add_vertex((696, 250))
    rfinger4.add_vertex((703, 242))
    rfinger4.filled = True
    rfinger4.fill_color = 'white'
    window.add(rfinger4)
    rfinger5 = GPolygon()
    rfinger5.add_vertex((715, 245))
    rfinger5.add_vertex((703, 242))
    rfinger5.add_vertex((710, 235))
    rfinger5.filled = True
    rfinger5.fill_color = 'white'
    window.add(rfinger5)


def toe():
    toe1 = GPolygon()
    toe1.add_vertex((195, 375))
    toe1.add_vertex((185, 400))
    toe1.add_vertex((205, 400))
    toe1.filled = True
    toe1.fill_color = 'white'
    window.add(toe1)
    toe2 = GPolygon()
    toe2.add_vertex((160, 390))
    toe2.add_vertex((160, 415))
    toe2.add_vertex((175, 405))
    toe2.filled = True
    toe2.fill_color = 'white'
    window.add(toe2)
    toe3 = GPolygon()
    toe3.add_vertex((230, 390))
    toe3.add_vertex((230, 415))
    toe3.add_vertex((215, 405))
    toe3.filled = True
    toe3.fill_color = 'white'
    window.add(toe3)
    toe4 = GPolygon()
    toe4.add_vertex((565, 375))
    toe4.add_vertex((575, 400))
    toe4.add_vertex((555, 400))
    toe4.filled = True
    toe4.fill_color = 'white'
    window.add(toe4)
    toe5 = GPolygon()
    toe5.add_vertex((600, 390))
    toe5.add_vertex((600, 415))
    toe5.add_vertex((585, 405))
    toe5.filled = True
    toe5.fill_color = 'white'
    window.add(toe5)
    toe6 = GPolygon()
    toe6.add_vertex((530, 390))
    toe6.add_vertex((530, 415))
    toe6.add_vertex((545, 405))
    toe6.filled = True
    toe6.fill_color = 'white'
    window.add(toe6)


if __name__ == '__main__':
    main()
