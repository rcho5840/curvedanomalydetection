import fiftyone as fo
import fiftyone.brain as fob
import glob
import os

def uniquesets(imagefilepath):
    
    #Traverse directory path, finding respective labeled folders and finding the unique images
    for directory_path in glob.glob(imagefilepath):
        dataset = fo.Dataset.from_images_dir(directory_path)

        res = fob.compute_similarity(dataset, brain_key="frame_sim")
            
        
        res.find_unique(500)
        uniq_view = dataset.select(res.unique_ids)
        dataset= dataset.select(uniq_view)
            
            #Export your unique images to the directory path
        dataset.export(
            export_dir= directory_path + r"\new", dataset_type=fo.types.ImageDirectory
        )
            #Delete the pre-existing data in the directory as you do not need it anymore
        for filename in os.listdir(directory_path):
            if filename.endswith('.jpg'):
                os.remove(os.path.join(directory_path, filename))
                print(f"Deleted: {filename}")
            
            
            
            

            
            
                

    
# import fiftyone as fo
# import fiftyone.brain as fob
# import glob
# import os

# def uniquesets(imagefilepath):
    
#     #Traverse directory path, finding respective labeled folders and finding the unique images
#     for directory_path in glob.glob(imagefilepath):
#         for second_directory_path in glob.glob(directory_path + "\*"):
#             dataset = fo.Dataset.from_images_dir(second_directory_path)

#             res = fob.compute_similarity(dataset, brain_key="frame_sim")
            
#             if second_directory_path == "ra":
                
#                 res.find_unique(50)
#             else:
#                 res.find_unique(150)
#             uniq_view = dataset.select(res.unique_ids)
#             dataset= dataset.select(uniq_view)
            
#             #Export your unique images to the directory path
#             dataset.export(
#                 export_dir= second_directory_path + r"\new", dataset_type=fo.types.ImageDirectory
#             )
#             #Delete the pre-existing data in the directory as you do not need it anymore
#             for filename in os.listdir(second_directory_path):
#                 if filename.endswith('.jpg'):
#                     os.remove(os.path.join(second_directory_path, filename))
#                     print(f"Deleted: {filename}")
            
            
            
            

            
            
                

    