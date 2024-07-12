import fiftyone as fo
import fiftyone.brain as fob


def findunique(videofilepath, savepath):

    # Load the dataset and use image embedding to determine the 30 most unique images
    dataset = fo.Dataset.from_images_dir(videofilepath)
    res = fob.compute_similarity(dataset, brain_key="frame_sim")
    res.find_unique(30)
    uniq_view = dataset.select(res.unique_ids)
    fo.launch_app(view=uniq_view)
    
    dataset= dataset.select(res.unique_ids)

    #export the dataset
    dataset.export(
        export_dir=savepath, dataset_type=fo.types.ImageDirectory
    )
    