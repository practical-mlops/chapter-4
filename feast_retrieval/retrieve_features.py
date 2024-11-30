from datetime import datetime
import pandas as pd
from feast import FeatureStore

entity_df = pd.DataFrame.from_dict(
    {
        "user_id": ["9f2ac416-06e1-44a0-87bd-d4787c85bf66"],
        "event_timestamp": [
            datetime(2023, 1, 30, 10, 59, 42),
        ],
    }
)

store = FeatureStore(repo_path=".")

training_df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "demographic:Sex",
    ],
).to_df()

print("----- Feature schema -----\n")
print(training_df.info())

print("----- Example features -----\n")
print(training_df.head())
