import streamlit as st
import pandas as pd
import datetime as dt
import random
import pytz
import time


def set_seed():
    madrid_tz = pytz.timezone('Europe/Madrid')
    tt = dt.datetime.now(madrid_tz).date().timetuple()
    seed = tt.tm_mday * 1000000 + tt.tm_mon*10000 + tt.tm_year
    random.seed(seed)


@st.cache_data
def llegeix_dataset():
    """Aquesta funció llegeix el dataset."""
    df = pd.read_csv("refranys.csv", quotechar='"', quoting=1)
    return df

NOMBRE_DE_FRASES = 10 # len(llegeix_dataset())


def llegeix_parts(index_primera: int, index_segona: int):
    df = llegeix_dataset()
    return df.iloc[index_primera]["part1"], df.iloc[index_segona]["part2"], \
        df.iloc[index_primera]["refrany"], df.iloc[index_segona]["refrany"]


def llegeix_frase(index: int):
    """Retorna la fila del dataset en una tupla:
    (refrany, primera part, segona part, definició)
    """
    df = llegeix_dataset()
    return  df.iloc[index]



def mostra_frase_definicions(idx1: int, idx2: int):
    refrany1, r1_part1, _, r1_def = llegeix_frase(idx1)
    refrany2, _, r2_part2, r2_def = llegeix_frase(idx2)
    st.markdown(f"<h2 style='text-align: center'>{r1_part1} {r2_part2}</h2>", unsafe_allow_html=True)
    st.text("")
    st.markdown("Les frases originals són:")
    st.markdown("**"+refrany1+"**: "+r1_def)
    st.markdown("**"+refrany2+"**: "+r2_def)


def frase_del_dia():
    st.title("La frase del dia és:")
    set_seed()
    primer = random.randint(0, NOMBRE_DE_FRASES-1)
    segon = random.randint(0, NOMBRE_DE_FRASES-1)
    mostra_frase_definicions(primer, segon)


def generador_aleatori():
    st.title("Generador aleatori")
    random.seed(time.time())
    if st.button("Genera una frase"):
        primer = random.randint(0, NOMBRE_DE_FRASES-1)
        segon = random.randint(0, NOMBRE_DE_FRASES-1)
        mostra_frase_definicions(primer, segon)


def main():
    st.sidebar.title("Navega")
    app_mode = st.sidebar.radio("Ves a:", ["La frase del dia", "Generador aleatori"])

    if app_mode == "La frase del dia":
        frase_del_dia()
    elif app_mode == "Generador aleatori":
        generador_aleatori()

    # [ ] Revisar amb l'Anaiis a nivell de disseny de la pagina
    st.divider()
    st.markdown("Si no vols pols és una aplicació per aprendre frases fetes en Català de manera divertida. De manera aleatòria, es poden generar frases fetes barrejant la primera part d'una, amb la segona part d'una altra. Cada dia sortirà una combinació única, i també pots anar a la pàgina de generació aleatòria per provar noves combinacions. Els refranys els hem extret del llibre [Els 100 refranys més populars](https://lafinestralectora.cat/els-100-refranys-mes-populars/) de Víctor Pàmies i Jordi Palou. Les definicions les hem extret de [Roda Mots](https://rodamots.cat/)")
    st.markdown("Esperem que us ho passeu bé!")


if __name__ == "__main__":
    main()
