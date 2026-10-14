def geld_gespendeerd(stuks, prijs):
    return stuks * prijs


def verdiende_mijlen(stuks, barcodes, mijlen_per_coupon):
    return stuks // barcodes * mijlen_per_coupon


stuks = int(input())
prijs = float(input())
barcodes = int(input())
mijlen = int(input())

print(f"Phillips spendeerde ${geld_gespendeerd(stuks, prijs)} "
      f"voor {verdiende_mijlen(stuks, barcodes, mijlen)} frequent flyer mijlen.")