import pandas as pd
from decoder_moduals import *


def main():
    df=pd.read_csv(r"data\NUM.csv",sep=",",encoding="utf-8")
    df["新准考證"]=None
    for num_index,num in enumerate(df["准考證"]):
        picname=write_pic(num_index=num_index,dcode=num.split("base64,")[1])
        text=img_to_str(picname)
        df["新准考證"][num_index]=str(text)
    df.to_csv("new_num3.csv",index=False)


if __name__ == "__main__":
    main()

