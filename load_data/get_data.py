import tensorflow as tf
from sklearn.datasets import load_wine

_data = load_wine()

COLUMN_NAMES = [*_data["feature_names"], "target"]
FIELD_DEFAULTS = [*[[0.0] for _ in _data["feature_names"]], [0.0]]


def _encode_target(target):
    encoded_targets = [0, 0, 0]
    print(target)
    encoded_targets[int(target[0])] = 1
    return encoded_targets


def _csv_to_record(line: str):
    fields = tf.io.decode_csv(line, FIELD_DEFAULTS)
    records = dict(zip(COLUMN_NAMES, fields))
    target = records.pop("target")
    return tf.transpose(list(records.values())), tf.one_hot(tf.cast(target, tf.int32), 3)


def get_data(pth: str, batch_size: int = 100) -> tf.data.Dataset:
    dataset = tf.data.TextLineDataset(pth) \
        .skip(1) \
        .prefetch(buffer_size=tf.data.AUTOTUNE) \
        .batch(batch_size=batch_size) \
        .map(_csv_to_record, num_parallel_calls=tf.data.AUTOTUNE)

    return dataset


if __name__ == "__main__":
    import os

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\RLAURENZ\Documents\Projects\TF\configs.json"
    dataset = get_data("gs://data-bucket-performance-test/single_file.csv", batch_size=2)
    features, target = next(dataset.as_numpy_iterator())
    print(features)
    print(target)
