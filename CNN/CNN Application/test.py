from camera import CameraReal

if __name__ == "__main__":
    cap = CameraReal(0)
    cap.reset_savedNum()
    for i in range(50):
        cap.imsave("Figure/")
        
        
