# -*- coding: utf-8 -*-
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def thumb(url: str) -> str:
    rot = ""
    match = re.search(r"rotate=(-?\d+)", url)
    if match:
        rot = f":rotate={match.group(1)}"
    tail = re.sub(r"^https://image\.jimcdn\.com/app/cms/image/transf/[^/]+/", "", url)
    return f"https://image.jimcdn.com/app/cms/image/transf/dimension=320x320:mode=crop:format=jpg{rot}/{tail}"

def figures(urls, alt, start):
    items = []
    for offset, url in enumerate(urls):
        index = start + offset
        items.append(
            f'<figure class="shot"><button type="button" data-full="{url}" aria-label="Agrandir la photo {index} : {alt}">'
            f'<img src="{thumb(url)}" alt="{alt}" loading="lazy"></button></figure>'
        )
    return "".join(items)

def gallery(urls, alt, preview=12):
    shown = f'<div class="gallery">{figures(urls[:preview], alt, 1)}</div>'
    if len(urls) <= preview:
        return shown
    rest = len(urls) - preview
    label = "Voir l'autre photo" if rest == 1 else f"Voir les {rest} autres photos"
    close = "Masquer la photo" if rest == 1 else "Masquer les photos"
    hidden = figures(urls[preview:], alt, preview + 1)
    return (
        f'<div class="gallery-set">{shown}'
        f'<div class="gallery gallery-extra" hidden>{hidden}</div>'
        f'<button type="button" class="more" aria-expanded="false" data-open="{label}" data-close="{close}">{label}</button>'
        f'</div>'
    )

CADEAUX = [
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=180/path/se04fa5da6b2ade7f/image/i810c43b7da6f55d4/version/1729518557/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=180/path/se04fa5da6b2ade7f/image/i6bf6b3073df4d625/version/1729518557/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=180/path/se04fa5da6b2ade7f/image/i779b824ed7b94929/version/1729518557/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i373c2aeb2dda697d/version/1729518557/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i22feea91f504d570/version/1729518557/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/ib572a2559181c3f8/version/1729518558/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/ieea5a4368c850272/version/1729519122/image.jpg",
]
COMMUNIONS = [
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/iec805fff7f56ec0d/version/1709738927/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/idf51c08107576818/version/1709738927/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i17026be9fcc886a2/version/1709738927/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i27932f8c418207fc/version/1709738927/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i14e9b7a1af134ef4/version/1709738927/image.jpg",
]
MARIAGES = [
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/ia132e069bb438e72/version/1697898410/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i3b1574a95a028d4b/version/1697898410/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=180/path/se04fa5da6b2ade7f/image/i75e8b9eb8b8c6ad2/version/1697898410/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i2a3a92ba8028969f/version/1697898410/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i2f06752e6330434e/version/1697898410/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/ifa966fd9eba1d2c7/version/1697898410/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/ia9f318ce6c1409d1/version/1697898410/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i1b0a57582c2aa0c9/version/1697898410/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i75009d60c10fdce5/version/1697898410/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/id154805bee31f845/version/1697898410/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg/path/se04fa5da6b2ade7f/image/ifacc2123d7267cd2/version/1697898410/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i4325ba331558b79a/version/1697898410/image.jpg",
]
BAPTEMES = [
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i57e5bc8d2c0bcbaa/version/1709740238/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i0d279a80d8b7fa4f/version/1709740238/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/ib3bec7d741ee7742/version/1709740238/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i8ee67ec3fe7856dc/version/1709740238/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/iea256eb15b18fcfb/version/1709740238/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/id57874230e9d34fe/version/1709740238/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=180/path/se04fa5da6b2ade7f/image/ic5bdc35334fd049c/version/1709740238/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=180/path/se04fa5da6b2ade7f/image/ib46e1b37e53ea2e5/version/1709740238/image.jpg",
]
URNES = [
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i12d99711410e6ff2/version/1729518756/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i6af426e0510738f3/version/1729518756/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/id807a9c28a369a67/version/1729518756/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i914398e32428e9f0/version/1729518756/image.jpg",
]
AMANDES = [
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/ib0f503886a1bf301/version/1514644474/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/ia5ae97bf5f3923fe/version/1514644406/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i4b81a633d1870435/version/1514644529/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i0dfc0c65af6250db/version/1514644612/image.jpg",
]
CHOCOLAT = [
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i8960e4330ec3cdeb/version/1643561064/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/if96206b802160d19/version/1643560886/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i365d7422db7b6e1c/version/1514646690/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i32500692f65b39ef/version/1514646743/image.jpg",
]
ARGENT = [
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/ia26a704bb0303d1f/version/1643561587/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i7e8181facdc1ce98/version/1643561459/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i041b4b21e0ada506/version/1514651493/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i5c5d707953ef01eb/version/1514651553/image.jpg",
]
GOURMANDISES = [
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i37479b25d661af65/version/1643563581/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/ibd18794cf609ce28/version/1643563370/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/id17d0465017d9e82/version/1643563160/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/ic72f73fbc2a71df5/version/1643562779/image.jpg",
]
COEURS = [
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i0f3a50fa6f414856/version/1514713253/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i336bf7769c14e9a2/version/1514713373/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i1cc057a8d3fb1c46/version/1514713435/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/ib0ec542919c63fc6/version/1514713494/image.jpg",
]
BISCUITS = [
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/ieacbb82715f73842/version/1551477586/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i952a46c2d2836e38/version/1551477454/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/ib64930f6d189b750/version/1551477076/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i8b67767525878096/version/1551477275/image.jpg",
]
GATEAUX = [
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1280x1820:format=jpg:rotate=270/path/se04fa5da6b2ade7f/image/idcb7c0a7982a70e5/version/1551216821/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i56e8c6df68898d0e/version/1515358516/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i439c83c62f430650/version/1515358393/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i05b423d32c7134ca/version/1515358251/image.jpg",
]
SALLE = [
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg/path/se04fa5da6b2ade7f/image/i24ca1312d22c9273/version/1580766580/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg/path/se04fa5da6b2ade7f/image/i5b9376788d6d9c3b/version/1580766580/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg/path/se04fa5da6b2ade7f/image/i7ea600c41c965fa6/version/1580766580/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg/path/se04fa5da6b2ade7f/image/idd40fbfb4b8d4fa0/version/1580766580/image.jpg",
]
PERSO = [
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i204d822cd2be2e48/version/1697899484/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/if9f9944016ea1d5a/version/1697899484/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i7bd5d30301d96150/version/1697899484/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg:rotate=90/path/se04fa5da6b2ade7f/image/i3a5aaa08e3eac631/version/1697899484/image.jpg",
]
NOEL = [
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg/path/se04fa5da6b2ade7f/image/i9581cd4e7f597252/version/1511127393/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg/path/se04fa5da6b2ade7f/image/ifb6abfc318bcd918/version/1511127406/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg/path/se04fa5da6b2ade7f/image/i161aa6c573b591b6/version/1511127417/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=2048x2048:format=jpg/path/se04fa5da6b2ade7f/image/i95276011b736f260/version/1511127582/image.jpg",
]
PARRAINS = [
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i5cf857a1ec279163/version/1514843463/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i509ccb0386132d55/version/1514843228/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/i524a60b3ab5aecfc/version/1514842986/image.jpg",
    "https://image.jimcdn.com/app/cms/image/transf/dimension=1820x1280:format=jpg/path/se04fa5da6b2ade7f/image/ieeb23d5cb6b1e520/version/1514842629/image.jpg",
]

HERO = "https://image.jimcdn.com/app/cms/image/transf/dimension=1600x2000:format=jpg:rotate=180/path/se04fa5da6b2ade7f/image/i810c43b7da6f55d4/version/1729518557/image.jpg"

def current(page, name):
    return ' aria-current="page"' if page == name else ""

LOGO = "https://image.jimcdn.com/app/cms/image/transf/dimension=250x250:format=jpg/path/se04fa5da6b2ade7f/image/i3ea5c53453b13d08/version/1567195658/image.jpg"
SHOP = "https://image.jimcdn.com/app/cms/image/transf/dimension=640x480:format=jpg/path/se04fa5da6b2ade7f/image/i703736ef29e19249/version/1542059934/image.jpg"
TEL = "tel:+33671400323"
TEL2 = "tel:+33982499068"
WA = "https://wa.me/33671400323"
MAPS = "https://www.google.com/maps/search/?api=1&query=18+rue+Vallon+74200+Thonon-les-Bains"

def nav(page):
    return f'''<a class="skip" href="#contenu">Aller au contenu</a>
<header class="site-header">
  <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
  <a class="logo" href="index.html"><img src="{LOGO}" alt="D &amp; B Dragées &amp; Biscuits" width="220" height="220"></a>
  <nav class="nav" id="menu">
    <a href="index.html"{current(page, "accueil")}>Accueil</a>
    <a class="nav-feature" href="nouveautes.html"{current(page, "nouveautes")}>Nouveautés 2025-2026</a>
    <a href="noel.html"{current(page, "noel")}>Noël</a>
    <div class="drop">
      <button type="button" aria-expanded="false"{current(page, "evenements")}>Événements</button>
      <div class="drop-panel">
        <a href="mariages.html">Mariages</a>
        <a href="baptemes.html">Baptêmes</a>
        <a href="communions.html">Communions</a>
        <a href="parrains.html">Cadeaux parrains &amp; marraines</a>
      </div>
    </div>
    <div class="drop">
      <button type="button" aria-expanded="false"{current(page, "dragees")}>Dragées</button>
      <div class="drop-panel">
        <a href="dragees.html#amandes">Amandes Avolas</a>
        <a href="dragees.html#chocolat">Chocolat</a>
        <a href="dragees.html#argent">Argent</a>
        <a href="dragees.html#gourmandises">Gourmandises</a>
        <a href="dragees.html#coeurs">Petits cœurs chocolat</a>
      </div>
    </div>
    <div class="drop">
      <button type="button" aria-expanded="false"{current(page, "creations")}>Créations</button>
      <div class="drop-panel">
        <a href="creations.html#biscuits">Biscuits personnalisés</a>
        <a href="creations.html#gateaux">Décor de gâteaux</a>
        <a href="creations.html#salle">Décor de salle</a>
        <a href="creations.html#personnalise">Décor personnalisé</a>
        <a href="creations.html#urnes">Urnes et livres d'or</a>
        <a href="noel.html">Idées cadeaux de Noël</a>
      </div>
    </div>
    <a href="presse.html"{current(page, "presse")}>Presse</a>
    <a href="partenaires.html"{current(page, "partenaires")}>Partenaires</a>
    <a href="contact.html"{current(page, "contact")}>Contact</a>
  </nav>
</header>'''

def foot():
    return f'''<footer class="site-footer">
  <div class="footer-grid">
    <div>
      <strong>D &amp; B Dragées &amp; Biscuits</strong>
      <p>18 rue Vallon<br>74200 Thonon-les-Bains</p>
      <p><a href="{MAPS}" target="_blank" rel="noopener">Voir l'itinéraire</a></p>
    </div>
    <div>
      <strong>Horaires</strong>
      <p>Mardi au samedi<br>10 h 00 – 12 h 00<br>14 h 00 – 17 h 00</p>
    </div>
    <div>
      <strong>Téléphone</strong>
      <p><a href="{TEL}">06 71 40 03 23</a><br><a href="{TEL2}">09 82 49 90 68</a><br><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></p>
    </div>
  </div>
  <p class="footer-legal"><a href="mentions.html">Mentions légales</a></p>
</footer>
<div class="lightbox" role="dialog" aria-modal="true" aria-label="Photo agrandie">
  <button class="lightbox-close" type="button">Fermer</button>
  <img alt="">
</div>
<script src="js/site.js?v=8"></script>'''

def page(name, title, body, nav_key, description):
    html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} · Dragées &amp; Biscuits</title>
  <meta name="description" content="{description}">
  <link rel="icon" href="favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Noto+Sans:wght@400;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css?v=25">
</head>
<body>
{nav(nav_key)}
<main id="contenu">
{body}
</main>
{foot()}
</body>
</html>
'''
    (ROOT / name).write_text(html, encoding="utf-8")

SRC = ROOT.parent / "site"
ORDER = f'''<section class="block order">
  <h2>Comment commander</h2>
  <ol class="steps">
    <li><strong>En boutique</strong> Les couleurs, la date ou le prénom se choisissent au 18 rue Vallon, à Thonon-les-Bains. Mardi au samedi, 10 h 00 – 12 h 00 et 14 h 00 – 17 h 00.</li>
    <li><strong>Un devis par téléphone</strong> Pour un mariage, un baptême, une communion ou un décor de salle, appelez le 06 71 40 03 23. Le délai est convenu au moment du devis, selon la pièce.</li>
    <li><strong>WhatsApp</strong> Écrire au 06 71 40 03 23 pour une question ou pour envoyer une photo.</li>
  </ol>
  <p class="center actions"><a class="devis" href="{TEL}">Appeler pour un devis</a> <a class="devis" href="{WA}" target="_blank" rel="noopener">Écrire sur WhatsApp</a></p>
</section>'''

def unique(urls):
    found = set()
    kept = []
    for url in urls:
        image = re.search(r"/image/(i[0-9a-f]+)/version/", url)
        key = image.group(1) if image else url
        if key not in found:
            found.add(key)
            kept.append(url)
    return kept

def all_images(folder):
    html = (SRC / folder / "index.html").read_text(encoding="utf-8")
    return unique(re.findall(r'data-href="([^"]+)"', html))

def home_gallery(title):
    html = (SRC / "index.html").read_text(encoding="utf-8")
    marker = f">{title}</h1>"
    start = html.find(marker)
    if start < 0:
        return []
    nxt = html.find('class="j-module n j-header "', start + len(marker))
    chunk = html[start:nxt if nxt > 0 else None]
    return unique(re.findall(r'data-href="([^"]+)"', chunk))

PHOTOS = {
    "mariages": unique(home_gallery("Mariages 2024") + home_gallery("Mariages 2023") + all_images("mariages")),
    "baptemes": unique(home_gallery("Baptêmes 2024") + home_gallery("Baptêmes&nbsp; 2023") + all_images("baptêmes")),
    "communions": unique(home_gallery("Communions 2024") + home_gallery("Communions&nbsp; 2023") + all_images("communions")),
    "parrains": all_images("cadeaux-parrains-marraines"),
    "amandes": all_images("dragées-amandes-avolas"),
    "chocolat": all_images("dragées-chocolat"),
    "argent": all_images("dragées-argent"),
    "gourmandises": all_images("dragées-gourmandises"),
    "coeurs": all_images("petits-cœurs-chocolat"),
    "biscuits": all_images("biscuits-petit-beurres-personnalisés"),
    "gateaux": all_images("décor-de-gâteaux"),
    "salle": all_images("décor-de-salle"),
    "perso": all_images("décor-personnalisés"),
    "urnes": all_images("urnes-coussins-d-alliances-livres-d-or-personnalisés"),
    "noel": all_images("idées-cadeaux-noël"),
    "presse": all_images("presse"),
    "partenaires": all_images("partenaires"),
}

def card(href, label, title, image):
    return f'<a class="card" href="{href}"><img src="{thumb(image)}" alt="{title}"><span>{title}</span></a>'

page("index.html", "Accueil", f'''
<div class="banner">
  <p class="magenta title">D &amp; B</p>
  <p class="magenta title">Dragées &amp; Biscuits</p>
  <h1>18 rue Vallon<br>74200 Thonon-les-Bains</h1>
  <p class="lead">Dragées, biscuits et décors personnalisés pour les mariages, les baptêmes et les communions.<br>Les commandes se prennent à la boutique, par téléphone ou par WhatsApp.</p>
</div>
<div class="shop-row">
  <img src="{SHOP}" alt="Boutique Dragées et Biscuits, 18 rue Vallon à Thonon-les-Bains">
  <div class="magenta">
    <p><strong>Horaires d'ouverture</strong></p>
    <p>Du mardi au samedi</p>
    <p>10 h 00 – 12 h 00 · 14 h 00 – 17 h 00</p>
    <p><a href="{TEL}">06 71 40 03 23</a><br><a href="{TEL2}">09 82 49 90 68</a><br><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></p>
  </div>
</div>
<p class="magenta trust">Recommandé par Gault &amp; Millau<br>Fournisseur officiel du Hilton à Evian-les-Bains</p>
<section class="block note">
  <h2>La boutique</h2>
  <p>Tout un choix de couleurs pour personnaliser vos cadeaux invités.</p>
  <p>Les dragées sont des amandes Avolas à 44 %, donc très peu de sucre, avec la saveur de l'amande qui fond dans la bouche. Les dragées chocolat se déclinent en spéculoos, noisette, amande, calisson et chocolat à 70 %.</p>
  <p>Les biscuits petit-beurre sont faits maison et personnalisables avec une date ou un prénom, pour un mariage, un baptême, une communion, un anniversaire ou la Saint-Valentin.</p>
  <p>Pour changer des dragées : boissons sèches, sirop ou miel, alcool, sels de bain, savon, maracas, sucette avec de vrais pétales de fleurs, et kit de survie.</p>
  <p>Macarons maracas au gianduja (praliné), enrobés de glace royale : letchi, orange, fleur de sel, chocolat, praliné, café, citron, framboise, violette, crème brûlée, amande.</p>
</section>
{ORDER}
<h2>Nouveautés 2025-2026</h2>
<p class="magenta">Idées cadeaux gourmands de la saison.</p>
{gallery(CADEAUX[:4], "Nouveauté gourmande")}
<p class="center"><a href="nouveautes.html">Voir toutes les nouveautés</a></p>
<h2>Choisir une création</h2>
<div class="cards">
  {card("mariages.html", "Événements", "Mariages", MARIAGES[0])}
  {card("baptemes.html", "Événements", "Baptêmes", BAPTEMES[0])}
  {card("communions.html", "Événements", "Communions", COMMUNIONS[0])}
  {card("dragees.html", "Dragées", "Dragées", CHOCOLAT[0])}
  {card("creations.html#salle", "Créations", "Décors de salle", SALLE[0])}
  {card("creations.html#urnes", "Créations", "Urnes et livres d'or", URNES[0])}
  {card("noel.html", "Noël", "Idées cadeaux de Noël", NOEL[0])}
</div>
''', "accueil", "Dragées, biscuits et décors personnalisés à la boutique du 18 rue Vallon, à Thonon-les-Bains. Mariages, baptêmes et communions.")

page("nouveautes.html", "Nouveautés 2025-2026", f'''
<div class="page-intro">
  <p class="eyebrow">Saison 2025-2026</p>
  <h1>Nouveautés</h1>
  <p>Idées cadeaux gourmands, urnes, coussins d'alliances et livres d'or personnalisés.</p>
</div>
<section class="block">
  <h2>Idées cadeaux gourmands</h2>
  <p>Boîtes, compositions et douceurs à offrir.</p>
  {gallery(CADEAUX, "Idée cadeau gourmande")}
</section>
<section class="block" id="urnes">
  <h2>Urnes, coussins et livres d'or</h2>
  <p>Pièces personnalisées pour le jour de la cérémonie.</p>
  {gallery(URNES, "Urne, coussin ou livre d'or")}
</section>
<section class="block">
  <h2>Collections à commander cette saison</h2>
  <div class="cards">
    {card("mariages.html", "Événements", "Mariages", MARIAGES[1])}
    {card("baptemes.html", "Événements", "Baptêmes", BAPTEMES[1])}
    {card("communions.html", "Événements", "Communions", COMMUNIONS[1])}
  </div>
</section>
''', "nouveautes", "Idées cadeaux gourmands, urnes, coussins d'alliances et livres d'or personnalisés, à Thonon-les-Bains.")

page("mariages.html", "Mariages", f'''
<div class="page-intro">
  <p class="eyebrow">Événements</p>
  <h1>Mariages</h1>
  <p>Dragées, contenants et décors composés pour le jour du mariage.</p>
</div>
{ORDER}
<section class="block">{gallery(PHOTOS["mariages"], "Création de mariage")}</section>
''', "evenements", "Dragées, contenants et décors de mariage à Thonon-les-Bains. Devis au 06 71 40 03 23.")

page("baptemes.html", "Baptêmes", f'''
<div class="page-intro">
  <p class="eyebrow">Événements</p>
  <h1>Baptêmes</h1>
  <p>Des compositions douces pour le baptême : dragées, petits présents et mises en scène prêtes à déposer sur la table.</p>
</div>
{ORDER}
<section class="block">{gallery(PHOTOS["baptemes"], "Création de baptême")}</section>
''', "evenements", "Compositions de baptême : dragées, petits présents et mises en scène, à la boutique de Thonon-les-Bains.")

page("communions.html", "Communions", f'''
<div class="page-intro">
  <p class="eyebrow">Événements</p>
  <h1>Communions</h1>
  <p>Dragées et cadeaux d'invités pour la communion.</p>
</div>
{ORDER}
<section class="block">{gallery(PHOTOS["communions"], "Création de communion")}</section>
''', "evenements", "Dragées et cadeaux d'invités pour une communion, préparés à Thonon-les-Bains.")

page("parrains.html", "Cadeaux parrains et marraines", f'''
<div class="page-intro">
  <p class="eyebrow">Événements</p>
  <h1>Cadeaux parrains &amp; marraines</h1>
  <p>Des attentions à offrir aux parrains et marraines, en dragées, biscuits ou petites compositions personnalisées.</p>
</div>
{ORDER}
<section class="block">{gallery(PHOTOS["parrains"], "Cadeau parrain ou marraine")}</section>
''', "evenements", "Cadeaux pour les parrains et marraines : dragées, biscuits et petites compositions personnalisées.")

page("dragees.html", "Dragées", f'''
<div class="page-intro">
  <p class="eyebrow">La boutique</p>
  <h1>Dragées</h1>
  <p>Depuis la Grèce antique et l'époque romaine, la dragée française est créée en 1220 par un apothicaire. Elle devient une friandise recherchée, présente sur les tables à chaque événement familial. L'amande Avola, cultivée à Avola dans la province de Syracuse en Sicile, est présentée comme la meilleure amande du monde.</p>
  <p>Les dragées sont des amandes Avolas à 44 %, donc très peu de sucre, avec la saveur de l'amande qui fond dans la bouche.</p>
  <p>Les dragées chocolat : spéculoos, noisette, amande, calisson et chocolat à 70 %.</p>
</div>
{ORDER}
<section class="block" id="amandes"><h2>Amandes Avolas</h2>{gallery(PHOTOS["amandes"], "Dragée amande Avolas")}</section>
<section class="block" id="chocolat"><h2>Dragées chocolat</h2>{gallery(PHOTOS["chocolat"], "Dragée chocolat")}</section>
<section class="block" id="argent"><h2>Dragées argent</h2>{gallery(PHOTOS["argent"], "Dragée argent")}</section>
<section class="block" id="gourmandises"><h2>Gourmandises</h2>{gallery(PHOTOS["gourmandises"], "Gourmandise")}</section>
<section class="block" id="coeurs"><h2>Petits cœurs chocolat</h2>{gallery(PHOTOS["coeurs"], "Petit cœur chocolat")}</section>
''', "dragees", "Amandes Avolas à 44 %, dragées chocolat, dragées argent et gourmandises, à Thonon-les-Bains.")

page("creations.html", "Créations", f'''
<div class="page-intro">
  <p class="eyebrow">Atelier</p>
  <h1>Créations</h1>
  <p>Biscuits provençaux, décors de gâteaux, décors de salle et pièces personnalisées pour le jour J.</p>
</div>
{ORDER}
<section class="block" id="biscuits">
  <h2>Biscuits personnalisés</h2>
  <p>Biscuits petit-beurre faits maison, personnalisables avec une date ou un prénom. Pour un mariage, un baptême, une communion, un anniversaire, la Saint-Valentin ou un autre événement.</p>
  <p>Les biscuits provençaux, canistrelli et navettes, sont fabriqués en Corse par un artisan. Œufs du Lubéron, amandes entières de Provence, farine et sucre sans OGM.</p>
  {gallery(PHOTOS["biscuits"], "Biscuit personnalisé")}
</section>
<section class="block" id="gateaux"><h2>Décor de gâteaux</h2>{gallery(PHOTOS["gateaux"], "Décor de gâteau")}</section>
<section class="block" id="salle">
  <h2>Décor de salle</h2>
  <p>N'hésitez pas à me demander un devis pour vos décors de salle, à la maison ou en extérieur, pour tous vos événements. Je ferai en sorte que vos rêves deviennent réalité.</p>
  {gallery(PHOTOS["salle"], "Décor de salle")}
</section>
<section class="block" id="personnalise"><h2>Décor personnalisé</h2>{gallery(PHOTOS["perso"], "Décor personnalisé")}</section>
<section class="block" id="urnes"><h2>Urnes, coussins et livres d'or</h2>{gallery(PHOTOS["urnes"], "Urne ou livre d'or")}</section>
''', "creations", "Biscuits personnalisés, décors de gâteaux, décors de salle, urnes et livres d'or à Thonon-les-Bains.")

page("contact.html", "Contact", f'''
<div class="page-intro">
  <p class="eyebrow">Boutique</p>
  <h1>Contact</h1>
  <p>Les commandes et les conseils se font à la boutique, au 18 rue Vallon à Thonon-les-Bains.</p>
</div>
<section class="block">
  <div class="info-grid">
    <div class="panel">
      <h2>Adresse</h2>
      <p>D &amp; B Dragées &amp; Biscuits<br>18 rue Vallon<br>74200 Thonon-les-Bains</p>
      <p><a href="{MAPS}" target="_blank" rel="noopener">Voir l'itinéraire</a></p>
      <p><a href="{TEL}">06 71 40 03 23</a><br><a href="{TEL2}">09 82 49 90 68</a><br><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></p>
    </div>
    <div class="panel">
      <h2>Horaires</h2>
      <ul class="hours">
        <li><span>Mardi – samedi</span><span>10 h 00 – 12 h 00<br>14 h 00 – 17 h 00</span></li>
      </ul>
    </div>
  </div>
  <iframe class="map" title="Carte : 18 rue Vallon, 74200 Thonon-les-Bains" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=18%20rue%20Vallon%2074200%20Thonon-les-Bains&amp;z=16&amp;output=embed"></iframe>
</section>
{ORDER}
''', "contact", "Boutique au 18 rue Vallon à Thonon-les-Bains. Mardi au samedi, 10 h 00 – 12 h 00 et 14 h 00 – 17 h 00.")

page("presse.html", "Presse", f'''
<div class="page-intro">
  <p class="eyebrow">La maison</p>
  <h1>Presse</h1>
  <p>Dragées &amp; Biscuits, recommandé par Gault &amp; Millau et fournisseur officiel du Hilton à Evian-les-Bains.</p>
</div>
<section class="block">{gallery(PHOTOS["presse"], "Presse")}</section>
''', "presse", "Dragées et Biscuits, recommandé par Gault et Millau, fournisseur officiel du Hilton à Evian-les-Bains.")

page("partenaires.html", "Partenaires", f'''
<div class="page-intro">
  <p class="eyebrow">La maison</p>
  <h1>Partenaires</h1>
  <p>Pour garder des moments de vie inoubliables. N'hésitez pas à les contacter, ce sont de vrais passionnés.</p>
</div>
<section class="block">
  <h2>Dans l'air du temps</h2>
  <p>Des sourires, des rires ou des larmes de bonheur.</p>
  <p class="wide"><img src="https://image.jimcdn.com/app/cms/image/transf/dimension=1040x624:format=jpg/path/se04fa5da6b2ade7f/image/i6374e5f96aad9e47/version/1518184825/image.jpg" alt="Partenaire Dans l'air du temps"></p>
</section>
<section class="block">
  <h2>Cristal Source</h2>
  <p>Pour une décoration zen ou un bijou, la caverne d'Ali Baba.</p>
  {gallery(PHOTOS["partenaires"][:2], "Cristal Source")}
</section>
<section class="block">
  <h2>Charter sur le lac Léman</h2>
  <p>Pour un mariage, un baptême, un anniversaire ou un moment de plaisir. Monter à bord avec un skipper diplômé, visiter des lieux insolites ou passer une soirée en amoureux.</p>
  {gallery(PHOTOS["partenaires"][2:4], "Charter sur le lac Léman")}
</section>
<section class="block">
  <h2>Calligraphie</h2>
  <p>Pour les faire-part de mariage, les menus ou tout autre événement : une calligraphie faite main, sans ordinateur.</p>
  {gallery(PHOTOS["partenaires"][4:], "Calligraphie")}
</section>
''', "partenaires", "Partenaires de la boutique : Dans l'air du temps, Cristal Source, charter sur le lac Léman et calligraphie.")

page("noel.html", "Idées cadeaux de Noël", f'''
<div class="page-intro">
  <p class="eyebrow">Fêtes</p>
  <h1>Idées cadeaux de Noël</h1>
  <p class="magenta"><strong>Vous pouvez choisir la couleur de nos pliages et Origami, pour être en osmose avec vos tables de Fêtes.</strong></p>
  <p>Remplissez toutes les présentations à vos goûts.</p>
</div>
{ORDER}
<section class="block">{gallery(PHOTOS["noel"], "Cadeau de Noël")}</section>
''', "noel", "Idées cadeaux de Noël : pliages et origami à la couleur de la table, présentations à remplir selon vos goûts.")

page("mentions.html", "Mentions légales", f'''
<div class="page-intro">
  <p class="eyebrow">Informations</p>
  <h1>Mentions légales</h1>
</div>
<section class="block legal">
  <h2>Éditeur</h2>
  <p>D &amp; B Dragées &amp; Biscuits<br>18 rue Vallon<br>74200 Thonon-les-Bains</p>
  <p>Téléphone : <a href="{TEL}">06 71 40 03 23</a> et <a href="{TEL2}">09 82 49 90 68</a><br>
  <a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></p>
  <p>Directeur de la publication : D &amp; B Dragées &amp; Biscuits, 18 rue Vallon, 74200 Thonon-les-Bains.</p>
  <p>Ce site présente la boutique. Les commandes se prennent au 18 rue Vallon, par téléphone ou par WhatsApp. Aucun paiement n'est encaissé sur ces pages.</p>
  <h2>Hébergement</h2>
  <p>www.dbdrageesbiscuits.fr est hébergé par Jimdo GmbH, Stresemannstrasse 375, 22761 Hambourg, Allemagne.</p>
  <h2>Boutique en ligne</h2>
  <p>Les conditions de la boutique déjà en ligne :</p>
  <ul>
    <li><a href="https://www.dbdrageesbiscuits.fr/j/shop/terms" target="_blank" rel="noopener">Conditions d'utilisation</a></li>
    <li><a href="https://www.dbdrageesbiscuits.fr/j/shop/withdrawal" target="_blank" rel="noopener">Conditions de retour et formulaire de rétractation</a></li>
    <li><a href="https://www.dbdrageesbiscuits.fr/j/shop/deliveryinfo" target="_blank" rel="noopener">Conditions de livraison et de paiement</a></li>
    <li><a href="https://www.dbdrageesbiscuits.fr/j/privacy" target="_blank" rel="noopener">Politique de confidentialité</a></li>
    <li><a href="https://www.dbdrageesbiscuits.fr/j/legal-guarantee" target="_blank" rel="noopener">Garantie légale</a></li>
  </ul>
  <h2>Propriété intellectuelle</h2>
  <p>Les textes, les photos et le logo floral sont la propriété de D &amp; B Dragées &amp; Biscuits, sauf mention contraire. Toute reproduction demande une autorisation.</p>
  <h2>Données</h2>
  <p>Ces pages ne contiennent pas de formulaire. Le téléphone et WhatsApp ouvrent l'application du visiteur. La carte est affichée par Google Maps, qui peut recevoir l'adresse IP du visiteur. Aucun cookie de mesure d'audience n'est déposé ici.</p>
</section>
''', "mentions", "Mentions légales de D &amp; B Dragées et Biscuits, 18 rue Vallon, 74200 Thonon-les-Bains.")

def ensure_favicon():
    dest = ROOT / "favicon.png"
    try:
        import ssl
        from io import BytesIO
        from urllib.request import Request, urlopen
        from PIL import Image
        context = ssl._create_unverified_context()
        request = Request(LOGO, headers={"User-Agent": "Mozilla/5.0"})
        data = urlopen(request, timeout=30, context=context).read()
        image = Image.open(BytesIO(data)).convert("RGBA")
        image.resize((64, 64), Image.Resampling.LANCZOS).save(dest, "PNG")
        print("favicon écrit")
    except Exception as exc:
        print("favicon non généré :", exc)

ensure_favicon()
print("pages écrites")
