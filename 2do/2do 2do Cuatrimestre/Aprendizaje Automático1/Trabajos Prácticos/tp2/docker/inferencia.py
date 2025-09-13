import pandas as pd
import joblib
import json
import sys
import warnings

warnings.filterwarnings("ignore")

def limpiar(df):
    code_lluvia = json.load(open("code_lluvia.json"))
    WindDirToXDir = json.load(open("WindDirToXDir.json"))
    WindDirToYDir = json.load(open("WindDirToYDir.json"))

    # Codificación de la lluvia
    df["RainToday"] = df["RainToday"].map(code_lluvia)

    df['Date'] = pd.to_datetime(df['Date'])
    df["Month"] = df["Date"].dt.month
    # Creamos rows dummys para que funciona el get_dummies
    months_dict = {}
    for column in df.columns:
        months_dict[column] = None
    for i in range(1, 13):
        months_dict["Month"] =i
        df.loc[len(df)+i-1] = months_dict
    
    # One-Hot Encoding de los meses
    df = pd.get_dummies(df, columns=['Month'], drop_first=True, dtype='int8')
    df = df[:-12] # dropeamos los rows dummys
    
    # Codificación de la direccion del viento
    df['WindDir3pmX'] = df['WindDir3pm'].map(WindDirToXDir)
    df['WindDir3pmY'] = df['WindDir3pm'].map(WindDirToYDir)

    df['WindDir9amX'] = df['WindDir9am'].map(WindDirToXDir)
    df['WindDir9amY'] = df['WindDir9am'].map(WindDirToYDir)

    df['WindGustDirX'] = df['WindGustDir'].map(WindDirToXDir)
    df['WindGustDirY'] = df['WindGustDir'].map(WindDirToYDir)

    df = df.drop(columns=['WindDir3pm'])
    df = df.drop(columns=['WindDir9am'])
    df = df.drop(columns=['WindGustDir'])

    # Dropeamos date
    df = df.drop(columns=['Date', 'Location', 'RainTomorrow'])
    return df

input_file = sys.argv[1]
output_file = sys.argv[2]

pipeline = joblib.load("pipeline.joblib")

df = limpiar(pd.read_csv(input_file))

df_imputed = pipeline.named_steps["imputer"].transform(df)

df = pd.DataFrame(df_imputed, columns=df.columns)

df_numeric = df.drop(columns=['WindDir3pmX', 'WindDir3pmY', 'WindDir9amX',
                              'WindDir9amY', 'WindGustDirX', 'WindGustDirY',
                              "RainToday",
                              "Month_2", "Month_3", "Month_4", "Month_5", "Month_6",
                              "Month_7", "Month_8", "Month_9", "Month_10", "Month_11", "Month_12"
                              ])

df_numeric = pd.DataFrame(pipeline.named_steps["scaler"].transform(df_numeric), columns=df_numeric.columns)

df = pd.concat([df_numeric,
                df[["WindDir3pmX", "WindDir3pmY", "WindDir9amX", "WindDir9amY",
                    "WindGustDirX", "WindGustDirY", "RainToday",
                    "Month_2", "Month_3", "Month_4", "Month_5", "Month_6",
                    "Month_7", "Month_8", "Month_9", "Month_10", "Month_11", "Month_12"]]], axis=1)

df["Predicción"] = pipeline.named_steps["model"].predict(df)

df.to_csv(output_file, index=False)
