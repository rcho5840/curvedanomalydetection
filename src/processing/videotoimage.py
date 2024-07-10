import cv2
import os


def videoToImage(videopath, outputpath):
    if __name__ == "__main__":
        
        output_dir = os.path.abspath(outputpath)
        os.makedirs(output_dir, exist_ok=True)
            
        vid = cv2.VideoCapture(videopath)
        if not vid.isOpened():
            raise Exception("Video could not be opened")
        
        
        print(int(vid.get(cv2.CAP_PROP_FRAME_COUNT)))
        
        
        count = 1
        while True:
            success, frame = vid.read()
            
            if not success:
                break
            save_path = os.path.join(output_dir, f'frame{count}.png')
            cv2.imwrite(save_path, frame)
            count+=1
            
            vid.release()
            cv2.destroyAllWindows()
            