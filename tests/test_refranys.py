import streamlit_app as sta


def test_read_data():
    df = sta.llegeix_dataset()


def test_data_completeness():
    df = sta.llegeix_dataset()

    assert df["refrany"].isnull().sum() == 0
    assert df["part1"].isnull().sum() == 0
    assert df["part2"].isnull().sum() == 0


def test_data_consistency():
    df = sta.llegeix_dataset()
    df_len = len(df)
    df_consistency = (df["refrany"] == df["part1"] + " " + df["part2"]).sum()

    assert df_len == df_consistency
