from datetime import date

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - (
        (today.month, today.day) < (birthDate.month, birthDate.day)
    )

    return str(age)

def calculateHeight(inches):
    return str(round(float(int(inches) / 12), 1)).replace('.', "'")


def walkpercentage(walks, atbats):
    if walks and atbats:
        walks = float(walks)
        atbats = float(atbats)
        if walks != 0 and atbats != 0:
            return str(round(walks / atbats * 100, 2)) + "%"
        return "0.0%"

    return "N/A"

def sopercentage(so, atbats):
    if so and atbats:
        so = float(so)
        atbats= float(atbats)
        if so != 0 and atbats != 0:
            return str(round(so / atbats * 100, 2)) + "%"
        return "0.0%"

    return "N/A"

def avg(hits, atbats):
    if hits and atbats:
        hits = float(hits)
        atbats = float(atbats)
        if hits != 0:
            return '{:.3f}'.format(round(hits / atbats, 3))[-4:]

    return ".000"

def calculateIP(ippouts):
    if ippouts:
        ippouts = float(ippouts)
        if ippouts != 0:
            return str(round(ippouts/3.0, 1))
        return "0"
    return "N/A"

def calculateWHIP(walks, hits, ip):
    if walks and hits and ip != "N/A":
        walks = float(walks)
        hits = float(hits)
        ip = float(ip)
        if (walks != 0 or hits != 0) and ip != 0:
            return str(round((walks + hits) / ip , 2))
        return "0"
    return "N/A" 
    
def calculateXPER(stat, ip):
    if stat and ip != "N/A":
        stat = float(stat)
        ip = float(ip)
        if stat != 0 and ip != 0:
            return str(round((stat * 9)/ ip, 2))
        return "0.00"
    return "N/A"

def calculateWinLoss(wins, losses):
    total = wins + losses

    return '{:.3f}'.format(round(wins / total, 3)) + " W-L%"