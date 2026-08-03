# generate_playlist.py

EPG_URL = "https://raw.githubusercontent.com/Bornze/EPG-testing/main/filtered_epg.xml.gz"

# ==============================
# Full Channel List
# Format: (tvg-id, Channel Name, Logo, Group, Stream URL)
# ==============================

CHANNELS = [

    # ========== Telugu Entertainment ==========
    ("zee.telugu.hd.in", "Zee Telugu HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Zee_Telugu_HD.png", "Entertainment - Telugu", "http://iptvcasomsapi.jprdigital.in/x-media/C0537/master.m3u8"),
    ("etv.hd.in", "ETV HD", "https://jiotvimages.cdn.jio.com/dare_images/images/ETV_HD.png", "Entertainment - Telugu", "https://d27zlkxhgwrfgo.cloudfront.net/v1/master/9d43eacaed199f8d5883927e7aef514a8a08e108/ETV_HD_H264_cloud_in/index.m3u8"),
    ("star.maa.hd.in", "Star Maa HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Maa_HD.png", "Entertainment - Telugu", "http://iptvcasomsapi.jprdigital.in/x-media/C0478/master.m3u8"),
    ("gemini.tv.hd.in", "Gemini TV HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Gemini_TV_HD.png", "Entertainment - Telugu", "http://iptvcasomsapi.jprdigital.in/x-media/C0568/master.m3u8"),
    ("etv.plus.hd.in", "ETV Plus HD", "https://jiotvimages.cdn.jio.com/dare_images/images/ETV_Plus_HD.png", "Entertainment - Telugu", "https://d27zlkxhgwrfgo.cloudfront.net/v1/master/9d43eacaed199f8d5883927e7aef514a8a08e108/ETV_PLUS_H264_cloud_in/index.m3u8"),
    ("gemini.comedy.in", "Gemini Comedy", "https://jiotvimages.cdn.jio.com/dare_images/images/Gemini_Comedy.png", "Entertainment - Telugu", "http://iptvcasomsapi.jprdigital.in/x-media/C0573/master.m3u8"),
    ("zee.cinemalu.hd.in", "Zee Cinemalu HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Zee_Cinemalu_HD.png", "Entertainment - Telugu", "http://iptvcasomsapi.jprdigital.in/x-media/C0544/master.m3u8"),
    ("star.maa.movies.hd.in", "Star Maa Movies HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Maa_Movies_HD.png", "Entertainment - Telugu", "http://iptvcasomsapi.jprdigital.in/x-media/C0479/master.m3u8"),
    ("gemini.movies.hd.in", "Gemini Movies HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Gemini_Movies_HD.png", "Entertainment - Telugu", "https://mumbai-edge.smartplaytv.in/GeminiMoviesHD/index.m3u8"),
    ("star.maa.gold.in", "Star Maa Gold", "https://d229kpbsb5jevy.cloudfront.net/tv/150/150/bnw/maa-gold-white.png", "Entertainment - Telugu", "http://iptvcasomsapi.jprdigital.in/x-media/C0480/master.m3u8"),

    # ========== Telugu News ==========
    ("etv.andhra.pradesh.in", "ETV Andhra Pradesh", "https://jiotvimages.cdn.jio.com/dare_images/images/ETV_Andhra_pradesh.png", "News - Telugu", "https://d1g35elx8qnif3.cloudfront.net/v1/master/9d43eacaed199f8d5883927e7aef514a8a08e108/ETV_AP_H264_cloud_in/index.m3u8"),
    ("sakshi.tv.in", "Sakshi TV", "https://jiotvimages.cdn.jio.com/dare_images/images/Sakshi_tv.png", "News - Telugu", "https://yuppmedtaorire.akamaized.net/v1/master/a0d007312bfd99c47f76b77ae26b1ccdaae76cb1/sakshi_nim_https/240122/sakshi/playlist.m3u8"),
    ("tv9.telugu.in", "TV9 Telugu", "https://jiotvimages.cdn.jio.com/dare_images/images/TV9_Telugu_News.png", "News - Telugu", "https://dyjmyiv3bp2ez.cloudfront.net/pub-iotv9telcmjhcs/liveabr/playlist.m3u8"),
    ("ntv.telugu.in", "NTV", "https://jiotvimages.cdn.jio.com/dare_images/images/NTV.png", "News - Telugu", "https://yuppmedtaorire.akamaized.net/v1/master/a0d007312bfd99c47f76b77ae26b1ccdaae76cb1/ntv_nim_https/110322/ntv/playlist.m3u8"),
    ("abn.andhra.jyothi.in", "ABN Andhra Jyothi", "https://static.andhrajyothy.com/assets/images/logo.png", "News - Telugu", "https://cdn-1.pishow.tv/live/407/master.m3u8"),
    ("tv5.news.in", "TV5 News", "https://jiotvimages.cdn.jio.com/dare_images/images/TV_5_News.png", "News - Telugu", "https://yuppmedtaorire.akamaized.net/v1/master/a0d007312bfd99c47f76b77ae26b1ccdaae76cb1/tv5_nim_https/110322/tv5/playlist.m3u8"),
    ("v6.news.in", "V6 News", "https://jiotvimages.cdn.jio.com/dare_images/images/V6_News.png", "News - Telugu", "https://yuppmedtaorire.akamaized.net/v1/master/a0d007312bfd99c47f76b77ae26b1ccdaae76cb1/v6news_nim_https/140622/v6news/playlist.m3u8"),
    ("10.tv.in", "10TV", "https://jiotvimages.cdn.jio.com/dare_images/images/10_TV.png", "News - Telugu", "https://cdn-1.pishow.tv/live/391/master.m3u8"),

    # ========== Entertainment ==========
    ("colors.hd.in", "Colors HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Colors_HD.png", "Entertainment", "http://iptvcasomsapi.jprdigital.in/x-media/C0431/master.m3u8"),
    ("set.hd.in", "SET HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Sony_HD.png", "Entertainment", "http://iptvcasomsapi.jprdigital.in/x-media/C0379/master.m3u8"),
    ("sony.sab.hd.in", "Sony SAB HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Sony_SAB.png", "Entertainment", "http://iptvcasomsapi.jprdigital.in/x-media/C0375/master.m3u8"),
    ("colors.infinity.hd.in", "Colors Infinity HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Colors_Infinity_HD.png", "Entertainment", "http://iptvcasomsapi.jprdigital.in/x-media/C0437/master.m3u8"),

    # ========== Movies ==========
    ("sony.pix.hd.in", "Sony PIX HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Sony_Pix_HD.png", "Movies", "https://sl.vodep39240327.workers.dev/channel/SONY%20PIX%20HD.m3u8"),
    ("sony.max.hd.in", "Sony MAX HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Sony_Max_HD.png", "Movies", "https://sl.vodep39240327.workers.dev/channel/SONY%20MAX%20HD.m3u8"),
    ("movies.now.hd.in", "Movies Now HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Movies_Now_HD.png", "Movies", "http://iptvcasomsapi.jprdigital.in/x-media/C0090/master.m3u8"),
    ("mnx.hd.in", "MNX HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Movies_Now2_HD.png", "Movies", "http://iptvcasomsapi.jprdigital.in/x-media/C0114/master.m3u8"),
    ("star.movies.hd.in", "Star Movies HD", "https://images.weserv.nl/?url=https://tv-site.b-cdn.net/images/channel-logo/star-movies-hd.png", "Movies", "http://iptvcasomsapi.jprdigital.in/x-media/C0439/master.m3u8"),
    ("star.movies.select.hd.in", "Star Movies Select HD", "https://images.weserv.nl/?url=https://tv-site.b-cdn.net/images/channel-logo/star-movies-select-hd.png", "Movies", "http://iptvcasomsapi.jprdigital.in/x-media/C0440/master.m3u8"),

    # ========== Sports ==========
    ("sony.sports.ten.1.hd.in", "Sony TEN 1 HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Ten_HD.png", "Sports", "http://iptvcasomsapi.jprdigital.in/x-media/C0378/master.m3u8"),
    ("sony.sports.ten.2.hd.in", "Sony TEN 2 HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Ten2_HD.png", "Sports", "http://iptvcasomsapi.jprdigital.in/x-media/C0372/master.m3u8"),
    ("sony.sports.ten.5.hd.in", "Sony TEN 5 HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Six_HD.png", "Sports", "http://iptvcasomsapi.jprdigital.in/x-media/C0377/master.m3u8"),
    ("star.sports.1.hd.in", "Star Sports 1 HD", "https://jiotvimages.cdn.jio.com/dare_images/images/200/-/Star_Sports_HD_1.png", "Sports", "http://iptvcasomsapi.jprdigital.in/x-media/C0441/master.m3u8"),
    ("star.sports.2.hd.in", "Star Sports 2 HD", "https://jiotvimages.cdn.jio.com/dare_images/images/200/-/Star_Sports_HD_2.png", "Sports", "http://iptvcasomsapi.jprdigital.in/x-media/C0442/master.m3u8"),
    ("star.sports.select.1.hd.in", "Star Sports Select 1 HD", "https://jiotvimages.cdn.jio.com/dare_images/images/200/-/Star_Sports_Select_HD_1.png", "Sports", "https://tvsen7.aynascope.net/sspts1/index.m3u8"),
    ("star.sports.select.2.hd.in", "Star Sports Select 2 HD", "https://jiotvimages.cdn.jio.com/dare_images/images/200/-/Star_Sports_Select_HD_2.png", "Sports", "http://103.157.248.140:8000/play/a00p/index.m3u8"),

    # ========== Kids ==========
    ("cartoon.network.in", "Cartoon Network", "https://jiotvimages.cdn.jio.com/dare_images/images/Cartoon_Network.png", "Kids", "http://103.182.170.32:8888/play/a04o"),
    ("nick.hd+.in", "Nick HD+", "https://jiotvimages.cdn.jio.com/dare_images/images/Nick_HD.png", "Kids", "http://iptvcasomsapi.jprdigital.in/x-media/C0405/master.m3u8"),
    ("pogo.in", "Pogo", "https://jiotvimages.cdn.jio.com/dare_images/images/Pogo_Telugu.png", "Kids", "http://103.182.170.32:8888/play/a02p"),
    ("disney.channel.in", "Disney Channel", "https://jiotvimages.cdn.jio.com/dare_images/images/Disney_Channel.png", "Kids", "http://iptvcasomsapi.jprdigital.in/x-media/C0451/master.m3u8"),
    ("disney.junior.in", "Disney Junior", "https://jiotvimages.cdn.jio.com/dare_images/images/Disney_Junior.png", "Kids", "http://103.182.170.32:8888/play/a03q"),
    ("sony.yay.in", "Sony YAY", "https://jiotvimages.cdn.jio.com/dare_images/images/SonyYAYTel.png", "Kids", "https://sl.vodep39240327.workers.dev/channel/SONY%20YAY.m3u8"),

    # ========== Infotainment ==========
    ("discovery.hd.world.in", "Discovery HD World", "https://jiotvimages.cdn.jio.com/dare_images/images/Discovery_HD_World.png", "Infotainment", "http://103.157.248.140:8000/play/a017/index.m3u8"),
    ("history.tv18.hd.in", "History TV18 HD", "https://jiotvimages.cdn.jio.com/dare_images/images/History_18_Telugu.png", "Infotainment", "http://iptvcasomsapi.jprdigital.in/x-media/C0427/master.m3u8"),
    ("tlc.hd.in", "TLC HD", "https://yt3.googleusercontent.com/7uTWS1ZIhWMlKkvEKCCdfhAG9gf9PmkZ8RTz-6Zxmxlzfr0dN6uM6iaoZWNHz3_AQ0AggW3z5w=s160-c-k-c0x00ffffff-no-rj", "Lifestyle", "http://103.157.248.140:8000/play/a00z/index.m3u8"),
    ("travelxp.hd.in", "Travelxp HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Travel_XP.png", "Lifestyle", "https://deltatesttatasky.akamaized.net/out/i/968284.m3u8"),

    # ========== Music ==========
    ("gemini.music.hd.in", "Gemini Music HD", "https://jiotvimages.cdn.jio.com/dare_images/images/Gemini_Music_HD.png", "Music", "https://mumbai-edge.smartplaytv.in/GeminiMusicHD/index.m3u8"),
    ("star.maa.music.in", "Star Maa Music", "https://d229kpbsb5jevy.cloudfront.net/tv/150/150/bnw/maa-music-white.png", "Music", "http://iptvcasomsapi.jprdigital.in/x-media/C0481/master.m3u8"),
    ("zoom.in", "ZOOM", "https://jiotvimages.cdn.jio.com/dare_images/images/Zoom.png", "Music", "https://d2esfk1pb9cdob.cloudfront.net/master.m3u8"),
    ("music.india.in", "Music India", "https://jiotvimages.cdn.jio.com/dare_images/images/Music_India.png", "Music", "https://cdn-2.pishow.tv/live/226/master.m3u8"),

    # ========== News International ==========
    ("al.jazeera.in", "Al Jazeera", "https://jiotvimages.cdn.jio.com/dare_images/images/AL_Jazeera.png", "News International", "https://live-hls-apps-aje-fa.getaj.net/AJE/index.m3u8"),
    ("dw.in", "DW", "https://jiotvimages.cdn.jio.com/dare_images/images/dw.png", "News International", "https://dwamdstream102.akamaized.net/hls/live/2015525/dwstream102/index.m3u8"),
    ("wion.in", "WION", "https://pbs.twimg.com/profile_images/875597226747207681/0jkhMbbB_400x400.jpg", "News International", "https://raw.githubusercontent.com/Alstruit/adaptive-streams/alstruit-10_23_in/streams/in/WION.in.m3u8"),
    ("france.24.in", "France 24", "https://jiotvimages.cdn.jio.com/dare_images/images/France_24.png", "News International", "https://live.france24.com/hls/live/2037218-b/F24_EN_HI_HLS/master_2300.m3u8"),
    ("nhk.world.japan.in", "NHK World Japan", "https://jiotvimages.cdn.jio.com/dare_images/images/NHK_World_Japan.png", "News International", "https://media-tyo.hls.nhkworld.jp/hls/w/live/master.m3u8"),
]

def generate_playlist():
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(f'#EXTM3U url-tvg="{EPG_URL}" x-tvg-url="{EPG_URL}"\n\n')

        for tvg_id, name, logo, group, url in CHANNELS:
            f.write(f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-name="{name}" tvg-logo="{logo}" group-title="{group}",{name}\n')
            f.write(f'{url}\n\n')

    print(f"✅ playlist.m3u generated successfully with {len(CHANNELS)} channels")

if __name__ == "__main__":
    generate_playlist()
