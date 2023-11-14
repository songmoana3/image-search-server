import logging


def get_header() -> dict:
    import random

    from img_search_project.settings import USER_AGENT

    random_idx = random.randint(0, len(USER_AGENT) - 1)
    user_agent = {'user-agent': USER_AGENT[random_idx]}
    return user_agent

def get_path(file: object, depth: int) -> str:
    from os.path import abspath, dirname

    path = dirname(abspath(file))
    for _ in range(depth):
        path = dirname(path)
    return path

def get_hash(thumbnail_url):

    import sys
    sys.path.append('/songmoana/app')
    from image_utils.image_downloader import download_image_from_url
    from image_utils.feature_extractor import FeatureExtractor
    from image_utils.hashing import LSHHash
    
    try:
        thumbnail_img = download_image_from_url(thumbnail_url)

        feature_extractor = FeatureExtractor(thumbnail_img)
        feature = feature_extractor.extract_feature()

        lsh_hash = LSHHash(256)
        hashed_feature = lsh_hash.hash_tensor(feature)
        return hashed_feature
    
    except Exception as e:
        logging.error(e)
        return None