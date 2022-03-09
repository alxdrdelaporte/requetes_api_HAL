#!/usr/lib/python3.8
# -*-coding:utf-8 -*
"""
Alexander DELAPORTE - CRLAO
https://tekipaki.hypotheses.org/
https://github.com/alxdrdelaporte/
https://gitlab.com/alxdrdelaporte

Interroger l'API HAL avec Python 3
https://tekipaki.hypotheses.org/2102
"""

import requests
import json.decoder
from bs4 import BeautifulSoup as soup


def afficher_texte_reponse_api_hal(requete_api_hal: str):
    """Interroge l'API HAL et affiche le texte de la réponse
    Paramètre = requête API HAL"""
    reponse = requests.get(requete_api_hal, timeout=5)
    print(reponse.text)


def afficher_erreur_api(erreur):
    """Affiche les erreurs soulevées lors de l'interrogation de l'API HAL
    Paramètre = erreur"""
    print(f"Les résultats HAL n'ont pas pu être récupérés ({erreur}).")


def afficher_publications_hal(requete_api_hal: str):
    """Interroge l'API HAL et affiche les infos des documents de la réponse
    Paramètre = requête API HAL avec wt=json (str)"""
    try:
        reponse = requests.get(requete_api_hal, timeout=5)
        for doc in reponse.json()['response']['docs']:
            print(f"***\nId = {doc['docid']}\n{soup(doc['label_s'], 'html.parser').text}\n{doc['uri_s']}\n***\n")
    except requests.exceptions.HTTPError as errh:
        afficher_erreur_api(errh)
    except requests.exceptions.ConnectionError as errc:
        afficher_erreur_api(errc)
    except requests.exceptions.Timeout as errt:
        afficher_erreur_api(errt)
    except requests.exceptions.RequestException as err:
        afficher_erreur_api(err)
    except json.decoder.JSONDecodeError as errj:
        afficher_erreur_api(errj)


ma_requete = "http://api.archives-ouvertes.fr/search/CRLAO/?q=title_t:python&rows=100&sort=submittedDate_tdate desc"
ma_requete_csv = "http://api.archives-ouvertes.fr/search/CRLAO/?q=title_t:python&rows=100" \
                 "&sort=submittedDate_tdate desc&wt=csv"
ma_requete_xml = "http://api.archives-ouvertes.fr/search/CRLAO/?q=title_t:python&rows=100" \
                 "&sort=submittedDate_tdate desc&wt=xml"
ma_requete_xml_indente = "http://api.archives-ouvertes.fr/search/CRLAO/?q=title_t:python&rows=100" \
                         "&sort=submittedDate_tdate desc&wt=xml&indent=true"


# afficher_texte_reponse_api_hal(ma_requete)
# afficher_publications_hal(ma_requete)

# afficher_texte_reponse_api_hal(ma_requete_csv)
# afficher_texte_reponse_api_hal(ma_requete_xml)
# afficher_texte_reponse_api_hal(ma_requete_xml_indente)
