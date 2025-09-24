import requests as req
from time import time
import json
import random

invidious_urls = [
    "https://clover-pitch-position.glitch.me/",
    "https://inv.zzls.xyz/",
    "https://invidious.einfachzocken.eu/",
    "https://cal1.iv.ggtyler.dev/",
    "https://invidious.nerdvpn.de/",
    "https://iv.melmac.space/",
    "https://invidious.0011.lt/",
    "https://invidious.nietzospannend.nl/",
    "http://144.126.251.186/",
    "https://185.233.104.172:8443/",
    "https://aids.coronachan.tk/",
    "https://britneyspears.b9iqf.opdns.net/",
    "https://cal1.iv.ggtyler.dev/",
    "https://clips.im.allmendenetz.de/",
    "https://discordjp.cc/",
    "https://i.oyster.men/",
    "https://incogtube.com/",
    "https://inv.bp.projectsegfau.lt/",
    "https://inv.nadeko.net/",
    "https://inv.odyssey346.dev/",
    "https://inv.privacy.com.de/",
    "https://inv.riverside.rocks/",
    "https://inv.skrep.eu/",
    "https://inv.tux.pizza/",
    "https://inv.us.projectsegfau.lt/",
    "https://inv.vern.cc/",
    "https://inv.zzls.xyz/",
    "https://invi.susurrando.com/",
    "https://invidio.xamh.de/",
    "https://invidious-jp.kavin.rocks/",
    "https://invidious.0011.lt/",
    "https://invidious.2br02b.live/",
    "https://invidious.13ad.de/",
    "https://invidious.adminforge.de/",
    "https://invidious.baczek.me/",
    "https://invidious.chunboan.zone/",
    "https://invidious.dhusch.de/",
    "https://invidious.domain.glass/",
    "https://invidious.drgns.space/",
    "https://invidious.drivet.xyz/",
    "https://invidious.einfachzocken.eu/",
    "https://invidious.epicsite.xyz/",
    "https://invidious.esmailelbob.xyz/",
    "https://invidious.ethibox.fr/",
    "https://invidious.everythingcostsmoney.com/",
    "https://invidious.fdn.fr/",
    "https://invidious.flokinet.to/",
    "https://invidious.frbin.com/",
    "https://invidious.garudalinux.org/",
    "https://invidious.grimneko.de/",
    "https://invidious.jing.rocks/",
    "https://invidious.kavin.rocks/",
    "https://invidious.lidarshield.cloud/",
    "https://invidious.longtime.duckdns.org/",
    "https://invidious.lunar.icu/",
    "https://invidious.materialio.us/",
    "https://invidious.myachin.xyz/",
    "https://invidious.namazso.eu/",
    "https://invidious.nerdvpn.de/",
    "https://invidious.nietzospannend.nl/",
    "https://invidious.not.futbol/",
    "https://invidious.osi.kr/",
    "https://invidious.pcgamingfreaks.at/",
    "https://invidious.perennialte.ch/",
    "https://invidious.poast.org/",
    "https://invidious.privacydev.net/",
    "https://invidious.privacyredirect.com/",
    "https://invidious.private.coffee/",
    "https://invidious.projectsegfau.lt/",
    "https://invidious.protokolla.fi/",
    "https://invidious.pufe.org/",
    "https://invidious.qwik.space/",
    "https://invidious.reallyaweso.me/",
    "https://invidious.rhyshl.live/",
    "https://invidious.rndsh.it:8443/",
    "https://invidious.services.nachtalb.io/",
    "https://invidious.sethforprivacy.com/",
    "https://invidious.silur.me/",
    "https://invidious.slipfox.xyz/",
    "https://invidious.snopyta.org/",
    "https://invidious.technicalvoid.dev/",
    "https://invidious.tiekoetter.com/",
    "https://invidious.tinfoil-hat.net/",
    "https://invidious.varishangout.net/",
    "https://invidious.vern.cc/",
    "https://invidious.weblibre.org/",
    "https://invidious.yourdevice.ch/",
    "https://invidious.zapashcanon.fr/",
    "https://iteroni.com/",
    "https://iv.catgirl.cloud/",
    "https://iv.datura.network/",
    "https://iv.ggtyler.dev/",
    "https://iv.melmac.space/",
    "https://iv.nboeck.de/",
    "https://iv.nowhere.moe/",
    "https://iv.ok0.org/",
    "https://monocles.live/",
    "https://poketube.fun/",
    "https://rust.oskamp.nl/",
    "https://subscriptions.gir.st/",
    "https://tube.cthd.icu/",
    "https://tube.cumulus2bill.fr/",
    "https://tube.netflux.io/",
    "https://tv.metaversum.wtf/",
    "https://vid.priv.au/",
    "https://vid.puffyan.us/",
    "https://video.weiler.rocks/",
    "https://vro.omcat.info/",
    "https://watch.thekitty.zone/",
    "https://y.com.sb/",
    "https://yewtu.be/",
    "https://youtube.076.ne.jp/",
    "https://youtube.it-service-schopfheim.de/",
    "https://youtube.longtime.duckdns.org/",
    "https://youtube.mosesmang.com/",
    "https://youtube.noogle.gay/",
    "https://youtube.notrack.ch/",
    "https://youtube.privacyplz.org/",
    "https://youtube.skkato.repl.co/",
    "https://youtube.stowwe.pw/",
    "https://yt-no.discard.no/",
    "https://yt-us.discard.no/",
    "https://yt.512mb.org/",
    "https://yt.artemislena.eu/",
    "https://yt.cdaut.de/",
    "https://yt.control-console.link/",
    "https://yt.drgnz.club/",
    "https://yt.funami.tech/",
    "https://yt.leverenz.email/",
    "https://yt.oelrichsgarcia.de/",
    "https://yt.thechangebook.org/",
    "https://yt.vern.cc/",
    "https://yt.wkwkwk.fun/",
    "https://yt.yoc.ovh/",
    "https://ytb.alexio.tf/",
    "https://ytb.trom.tf/",
    "https://ytclient.antaresx.ch/",
    "https://rust.oskamp.nl/",
    "https://youtube.lurkmore.com/",
    "https://yt.yoc.ovh/"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

successful_instances = []
best = {
    "name": "",
    "time": 99999
}

print("[*] Starting Invidious instance check...")

for url in invidious_urls:
    if not url.startswith("http"):
        print(f"[-] Skipping {url}: Invalid protocol")
        continue

    print(f"[*] Checking {url}: ", end="")
    try:
        s = time()
        res = req.get(f"{url}api/v1/videos/e-qWitCw9dU", headers=headers, timeout=10)
        
        if res.status_code == 200:
            secs = time() - s
            secs_str = f"{secs:.4f}"
            successful_instances.append({
                "url": url,
                "time": secs_str
            })
            print(f"Took {secs_str}s")

            if best["time"] > secs:
                best["name"] = url
                best["time"] = secs
        else:
            print(f"Bad response ({res.status_code})")

    except req.exceptions.Timeout:
        print("Timeout")
    except req.exceptions.RequestException as e:
        print(f"Failed ({e})")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

print("\n---")
if not successful_instances:
    print("[-] All instances failed to respond.")
else:
    print("[+] Check completed. The following instances were successful:")
    # 応答時間でソートして表示
    sorted_instances = sorted(successful_instances, key=lambda x: float(x['time']))
    for inst in sorted_instances:
        print(f"  - {inst['url']}: {inst['time']}s")

    print("\n[+] The fastest instance found is:")
    print(f"  - {best['name']} ({best['time']:.4f}s)")
