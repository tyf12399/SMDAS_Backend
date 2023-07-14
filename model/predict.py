from datetime import datetime

import akshare as ak
from keras.layers import Dense, LSTM
from keras.models import Sequential
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

end = datetime.now()
formatted_end = end.strftime("%Y%m%d")


def stock_pred(
    code: str,
    path: str = "./model/lstm.hdf5",
):
    df = ak.stock_zh_a_hist(
        symbol=code,
        period="daily",
        start_date="20000101",
        end_date=formatted_end,
        adjust="qfq",
    )
    data = df["收盘"]
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data.to_numpy().reshape(-1, 1))
    model = Sequential()
    model.add(LSTM(128, return_sequences=True, input_shape=(60, 1)))
    model.add(LSTM(64, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(5))
    model = load_model(filepath=path)
    X_pred = scaled_data[-60:].reshape(1, 60, 1)
    predictions = model.predict(X_pred)
    predictions = scaler.inverse_transform(predictions)

    return predictions[0]
