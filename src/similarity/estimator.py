import os
import pandas as pd
import ntpath

from sklearn.metrics.pairwise import cosine_similarity
from src.feature.extractor import GFeatureExtractor
from utils.folder_file_manager import log_print
from settings import INPUT_EXCEL_PATH, OUTPUT_DIR


class FileSimilarity:
    def __init__(self):
        self.feature_extractor = GFeatureExtractor()

    def run(self):
        similarity_values = []

        file_name = ntpath.basename(INPUT_EXCEL_PATH).replace(".xlsx", "")
        output_file_path = os.path.join(OUTPUT_DIR, f"{file_name}_result.csv")

        input_df = pd.read_excel(INPUT_EXCEL_PATH)
        master_key = input_df.iloc[1, 1]
        master_feature = self.feature_extractor.get_feature_token_words(text=master_key)
        statements = input_df.iloc[2:, 3].values.tolist()
        for s_des in statements:
            try:
                s_des_feature = self.feature_extractor.get_feature_token_words(text=s_des)
                proximity = cosine_similarity([master_feature], [s_des_feature])
                similarity_values.append(proximity[0][0])
            except Exception as e:
                similarity_values.append("None")
                log_print(e)

        output_df = pd.DataFrame([[master_key], statements, similarity_values]).T
        output_df.to_csv(output_file_path, index=True, header=["Master Key", "Statements", "Proximity Score"], mode='w')

        print(f"[INFO] Successfully saved in {output_file_path}")

        return


if __name__ == '__main__':
    FileSimilarity().run()
