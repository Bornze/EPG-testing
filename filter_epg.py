import gzip
import xml.etree.ElementTree as ET
from datetime import datetime

SOURCE_GZ = "source_epg.xml.gz"
OUTPUT_GZ = "filtered_epg.xml.gz"

# ==============================
# CHANNEL LIST (Indian + International)
# ==============================
CHANNELS_TEXT = """
# ===== Telugu Entertainment =====
zee.telugu.in
etv.hd.in
star.maa.hd.in
gemini.tv.hd.in
etv.plus.in
gemini.comedy.in
zee.cinemalu.hd.in
star.maa.movies.hd.in
gemini.movies.hd.in
star.maa.gold.in

# ===== Telugu News =====
etv.andhra.pradesh.in
sakshi.tv.in
tv9.telugu.in
NTV.Telugu.in
abn.andhra.jyothi.in
tv.5.news.in
v6.news.in
10.tv.in

# ===== Entertainment =====
colors.hd.in
set.hd.in
sony.sab.hd.in
sony.sab.in
colors.infinity.hd.in
PTC.Punjabi.in
AXN.id

# ===== Movies =====
sony.pix.hd.in
sony.max.hd.in
movies.now.hd.in
movies.now.in
mnx.hd.in
star.movies.hd.in
star.movies.select.hd.in

# ===== Sports =====
sony.sports.ten.1.hd.in
sony.sports.ten.2.hd.in
sony.sports.ten.5.hd.in
star.sports.1.hd.in
star.sports.2.hd.in
star.sports.select.1.hd.in
star.sports.select.2.hd.in
Star.Sports.2.Telugu.in
Star.Sports.1.Telugu.in
Zee.Cafe.HD.in
AndFlix.HD.in
And.Flix.in

# ===== Kids =====
cartoon.network.in
Cartoon.Network.HD+.in
nick.in
pogo.in
disney.channel.in
disney.junior.in
sony.yay.in
Animax.in

# ===== Infotainment / Lifestyle =====
discovery.hd.world.in
history.tv18.hd.in
tlc.hd.in
travelxp.hd.in

# ===== Music =====
gemini.music.hd.in
star.maa.music.in
E.24.in
zoom.in
music.india.in
Raj.Music.Telugu.in
PTC.Chak.De.in
PTC.Music.in
PTC.Punjabi.Gold.in
Sangeet.Bangla.in
MTV.in
MTV.HD.in

# ===== News International =====
al.jazeera.in
dw.in
wion.in
france.24.in
nhk.world.japan.in
Euro.News.in
Channel.News.Asia.International.in
"""

# ==============================
# Cleaning function
# ==============================
SUFFIXES = [".in", ".uk", ".us", ".au", ".hk", ".ca", ".sa"]

def clean_id(cid):
    cid = cid.strip().lower()
    for s in SUFFIXES:
        if cid.endswith(s):
            cid = cid[:-len(s)]
            break
    return cid + ".in"

# Parse channels
CHANNELS = {}
for line in CHANNELS_TEXT.strip().splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    parts = line.split(maxsplit=1)
    original_id = parts[0].strip().lower()
    logo = parts[1].strip() if len(parts) == 2 else None
    cleaned = clean_id(original_id)
    CHANNELS[cleaned] = {
        "original": original_id,
        "logo": logo
    }

def main():
    kept = set()
    programmes = 0

    with open("filtered_epg.xml", "wb") as out:
        out.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        out.write(f'<tv generator-info-name="Bornze Filtered EPG" date="{datetime.utcnow().strftime("%Y%m%d%H%M%S +0000")}">\n'.encode())

        with gzip.open(SOURCE_GZ, "rb") as f:
            for _, elem in ET.iterparse(f, events=("end",)):
                if elem.tag == "channel":
                    raw_id = elem.attrib.get("id", "")
                    cid = clean_id(raw_id)

                    if cid in CHANNELS:
                        elem.attrib["id"] = CHANNELS[cid]["original"]
                        kept.add(cid)

                        logo = CHANNELS[cid]["logo"]
                        if logo:
                            for i in elem.findall("icon"):
                                elem.remove(i)
                            icon = ET.Element("icon")
                            icon.set("src", logo)
                            elem.append(icon)

                        out.write(ET.tostring(elem) + b"\n")
                    elem.clear()

                elif elem.tag == "programme":
                    raw_id = elem.attrib.get("channel", "")
                    cid = clean_id(raw_id)

                    if cid in kept:
                        elem.attrib["channel"] = CHANNELS[cid]["original"]
                        out.write(ET.tostring(elem) + b"\n")
                        programmes += 1
                    elem.clear()

        out.write(b"</tv>")

    # Compress the file
    with open("filtered_epg.xml", "rb") as fi, gzip.open(OUTPUT_GZ, "wb") as fo:
        fo.writelines(fi)

    print("✅ Filtering complete")
    print(f"Channels kept : {len(kept)}")
    print(f"Programmes    : {programmes}")

if __name__ == "__main__":
    main()
