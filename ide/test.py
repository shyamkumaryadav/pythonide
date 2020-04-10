from PyQt5.Qsci import QsciScintilla
from PyQt5.Qt import *

def get_arrow(down, size, cmin, cmax):
    from PIL import Image
    from PIL.ImageQt import ImageQt
    from math import atan2, cos, pi
    pict = Image.new("RGBA", (size, size), tuple(cmin + [255]))
    pixl = pict.load()
    step = 3.25**2
    for y in range(pict.size[1]):
        for x in range(pict.size[0]):
            xpos = x - pict.size[0] // 2 + 1
            ypos = y - pict.size[1] // 2 + 1
            retn = 1.5 * atan2(ypos, xpos) + (pi / 4, 0)[not down]
            retn = ((abs(cos(retn))**2.5 + 3) * 2)**2 - xpos**2 - ypos**2
            if (retn < 0):
                retn = cmin
            elif (retn >= step):
                retn = cmax
            else:
                retn = [int((cmax[i] - cmin[i]) * retn / step + cmin[i])
                        for i in range(0, 3)]
            pixl[x, y] = tuple(retn + [255])
    return ImageQt(pict)

def color_to_sc(c):
    return (c[0] & 0xFF) | ((c[1] & 0xFF) << 8) | ((c[2] & 0xFF) << 16)

def set_fold(prev, line, fold, full):
    if (prev[0] >= 0):
        fmax = max(fold, prev[1])
        for iter in range(prev[0], line + 1):
            view.SendScintilla(view.SCI_SETFOLDLEVEL, iter,
                fmax | (0, view.SC_FOLDLEVELHEADERFLAG)[iter + 1 < full])

def line_empty(line):
    return view.SendScintilla(view.SCI_GETLINEENDPOSITION, line) \
        <= view.SendScintilla(view.SCI_GETLINEINDENTPOSITION, line)

def modify(position, modificationType, text, length, linesAdded,
           line, foldLevelNow, foldLevelPrev, token, annotationLinesAdded):
    full = view.SC_MOD_INSERTTEXT | view.SC_MOD_DELETETEXT
    if (~modificationType & full == full):
        return
    prev = [-1, 0]
    full = view.SendScintilla(view.SCI_GETLINECOUNT)
    lbgn = view.SendScintilla(view.SCI_LINEFROMPOSITION, position)
    lend = view.SendScintilla(view.SCI_LINEFROMPOSITION, position + length)
    for iter in range(max(lbgn - 1, 0), -1, -1):
        if ((iter == 0) or not line_empty(iter)):
            lbgn = iter
            break
    for iter in range(min(lend + 1, full), full + 1):
        if ((iter == full) or not line_empty(iter)):
            lend = min(iter + 1, full)
            break
    for iter in range(lbgn, lend):
        if (line_empty(iter)):
            if (prev[0] == -1):
                prev[0] = iter
        else:
            fold = view.SendScintilla(view.SCI_GETLINEINDENTATION, iter)
            fold //= view.SendScintilla(view.SCI_GETTABWIDTH)
            set_fold(prev, iter - 1, fold, full)
            set_fold([iter, fold], iter, fold, full)
            prev = [-1, fold]
    set_fold(prev, lend - 1, 0, full)

def hover(position, xpos, ypos):
    mask = view.SendScintilla(view.SCI_GETMARGINMASKN, 2)
    mask = (mask | view.SC_MASK_FOLDERS, mask & ~view.SC_MASK_FOLDERS) \
           [xpos > StandardMarginWidth]
    view.SendScintilla(view.SCI_SETMARGINMASKN, 2, mask)

if __name__ == '__main__':
    import sys
    import textwrap

    app = QApplication(sys.argv)
    view = QsciScintilla()
    # view.SendScintilla(view.SCI_SETMULTIPLESELECTION, True)
    # view.SendScintilla(view.SCI_SETMULTIPASTE, 1)
    # view.SendScintilla(view.SCI_SETADDITIONALSELECTIONTYPING, True)
    # view.SendScintilla(view.SCI_SETINDENTATIONGUIDES, view.SC_IV_REAL);
    view.SendScintilla(view.SCI_SETTABWIDTH, 4)

    view.setFolding(view.BoxedFoldStyle)

    StandardIconSize = 12
    StandardMarginWidth = 12
    StandardBackground = [64, 64, 64]
    StandardForeground = [192, 192, 192] # [R, G, B]

    view.SendScintilla(view.SCI_SETMARGINWIDTHN, 1, 0)
    view.SendScintilla(view.SCI_SETMARGINWIDTHN, 2, StandardMarginWidth)

    view.SendScintilla(view.SCI_STYLESETBACK, view.STYLE_LINENUMBER, color_to_sc(StandardBackground))
    view.SendScintilla(view.SCI_SETFOLDMARGINHICOLOUR, True, color_to_sc(StandardBackground))
    view.SendScintilla(view.SCI_SETFOLDMARGINCOLOUR, True, color_to_sc(StandardBackground))

    view.SendScintilla(view.SCI_RGBAIMAGESETHEIGHT, StandardIconSize)
    view.SendScintilla(view.SCI_RGBAIMAGESETWIDTH, StandardIconSize)
    fldr = get_arrow(0, StandardIconSize, StandardBackground, StandardForeground)
    open = get_arrow(1, StandardIconSize, StandardBackground, StandardForeground)
    view.SendScintilla(view.SCI_MARKERDEFINERGBAIMAGE, view.SC_MARKNUM_FOLDER, fldr)
    view.SendScintilla(view.SCI_MARKERDEFINERGBAIMAGE, view.SC_MARKNUM_FOLDEROPEN, open)

    view.SendScintilla(view.SCI_SETMOUSEDWELLTIME, 50)
    view.SCN_DWELLSTART.connect(hover)
    view.SCN_DWELLEND.connect(hover)

    view.SCN_MODIFIED.connect(modify)

    # NUM_CHUNKS = 1
    # chunk = textwrap.dedent("""\
    #     def foo():
    #         x = 10
    #         y = 20
    #         return x+y

    #     def bar(x):
    #         if x > 0:
    #             print('this is')
    #             print('branch1')
    #         else:
    #             print('and this')
    #             print('is branch2')

    #     print('end')
    # """)
    # view.setText("\n".join([chunk for i in range(NUM_CHUNKS)]))
    view.show()
    app.exec_()