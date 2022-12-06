import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

#####


class Doc:
    def drawing(self, vat, date, title, chargewithvat, chargewithoutvat, desc1, netvalue1, invoiceno, desc2, desc3, desc4, netvalue2, netvalue3, netvalue4, quantity1, quantity2, quantity3, quantity4):
        pfi = Image.open('template/PFI_Template.jpg')
        invoice = Image.open('template/Invoice_Template.jpg')
        draw = ImageDraw.Draw(pfi)
        draw2 = ImageDraw.Draw(invoice)
        fonttype = ImageFont.truetype('times.ttf', 40)

        def pfi_description(content):
            words = textwrap.fill(content, width=40)
            return words.upper()

        if invoiceno == "":
            def drawtext(x, y, content):
                draw.text((x, y), content, font=fonttype, fill=(0, 0, 0))
        else:
            def drawtext(x, y, content):
                draw2.text((x, y), content, font=fonttype, fill=(0, 0, 0))

        def code():
            drawtext(1750, 1100, date)
            drawtext(2210, 1125, invoiceno)
            drawtext(1600, 2960, vat)
            drawtext(1600, 2892, chargewithoutvat)
            drawtext(1600, 3105, chargewithvat)
            drawtext(170, 1350, title)

            # pfi description
            drawtext(140, 1560, pfi_description(desc1))
            drawtext(140, 1820, pfi_description(desc2))
            drawtext(140, 2100, pfi_description(desc3))
            drawtext(140, 2370, pfi_description(desc4))
            # pfi quantity
            drawtext(1690, 1600, quantity1)
            drawtext(1690, 1820, quantity2)
            drawtext(1690, 2100, quantity3)
            drawtext(1690, 2370, quantity4)
            # net value for each item
            drawtext(2150, 1600, netvalue1)
            drawtext(2150, 1820, netvalue2)
            drawtext(2150, 2100, netvalue3)
            drawtext(2150, 2370, netvalue4)

        code()
        if invoiceno == "":
            i = 0
            while os.path.exists(f"PFI/PFI_{i}.jpg"):
                i += 1

            pfi.save("PFI/PFI_%s.jpg" % i)
            print("PFI generated successfully!")
        else:
            i = 0
            while os.path.exists(f"INVOICE/Newinvoice_{i}.jpg"):
                i += 1

            invoice.save("INVOICE/Newinvoice_%s.jpg" % i)
            print("Invoice generated successfully!")


def runProcess(vat, date, title, chargewithvat, chargewithoutvat, desc1, netvalue1, invoiceno, desc2, desc3, desc4, netvalue2, netvalue3, netvalue4, quantity1, quantity2, quantity3, quantity4):
    newPFI = Doc()
    newPFI.drawing(vat, date, title, chargewithvat,
                   chargewithoutvat,  desc1, netvalue1, invoiceno,  desc2, desc3, desc4, netvalue2, netvalue3, netvalue4, quantity1, quantity2, quantity3, quantity4)
