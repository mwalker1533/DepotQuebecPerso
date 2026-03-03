# Dépôt Québec Perso

Dépôt Kodi personnel avec les versions **améliorées et corrigées** de trois addons pour les chaînes de télévision francophones du Québec.

Tous compatibles avec **Kodi 20+ (Nexus/Omega)** et **Python 3**.

---

## 📺 Addons inclus

| Addon | Version | Chaîne | Statut |
|---|---|---|---|
| plugin.infologique.TVAgo | 2.1.0 | TVA+ | ✅ Fonctionnel |
| plugin.infologique.tou.tv | 3.1.0 | ICI Tou.TV | ✅ Fonctionnel |
| plugin.video.vtele | 5.1.0 | Noovo | ✅ Fonctionnel |

---

## 🔧 Comment installer le dépôt

### Étape 1 — Télécharger le fichier ZIP du dépôt

[👉 Cliquez ici pour télécharger](https://github.com/mwalker1533/DepotQuebecPerso/raw/master/repository.depot.quebec.perso/repository.depot.quebec.perso-1.0.0.zip)

### Étape 2 — Installer dans Kodi

1. Dans Kodi, allez dans **Système → Paramètres → Addons**
2. Cliquez sur **Installer depuis un fichier ZIP**
3. Sélectionnez le fichier téléchargé à l'étape 1
4. Attendez la confirmation d'installation

### Étape 3 — Installer les addons

1. Allez dans **Système → Paramètres → Addons → Installer à partir du dépôt**
2. Sélectionnez **Dépôt Québec Perso**
3. Allez dans **Addons de vidéos**
4. Installez les addons souhaités un à la fois

---

## 🐛 Corrections apportées

### TVA+ (v2.1.0)
- Python 3 / Kodi 20+ complet
- Correction des erreurs HTTP 403 sur Raspberry Pi (headers navigateur ajoutés)
- Suppression de la dépendance simplejson
- Gestion d'erreurs améliorée

### ICI Tou.TV (v3.1.0)
- **Correction principale** : `deviceType` changé de `iphone4` (cassé) à `ioscenc` — corrige l'erreur *"Aucun DRM n'est supporté"* présente depuis 2017
- Python 3 / Kodi 20+ complet
- Messages d'erreur en français

### Noovo (v5.1.0)
- **Correction principale** : crash `NoneType` sur la lecture vidéo corrigé — l'ancien code faisait du scraping HTML instable, remplacé par les APIs JSON Noovo + Brightcove
- Correction de `xbmcvfs.translatePath` (avertissement de dépréciation)
- Python 3 / Kodi 20+ complet

---

## ℹ️ Notes

- Le contenu **Extra** de Tou.TV (abonnement payant) n'est pas supporté
- Certains contenus Noovo peuvent nécessiter un abonnement Bell
- Ces addons fonctionnent uniquement pour le contenu accessible au Canada

---

*Basé sur le travail original de [anisite/DepotQuebec](https://github.com/anisite/DepotQuebec)*
