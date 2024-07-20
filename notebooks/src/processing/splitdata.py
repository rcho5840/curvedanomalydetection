
import splitfolders

def splitdata(input_folder, output_folder):
    splitfolders.ratio(input_folder, output = output_folder,
                       seed = 42, ratio = (0.8,0.2),
                       move =   True)
    

    
