import os
import random
import shutil


dataset_path = r'D:/deep_space/MV/Dataset_3'


train_ratio = 0.85
test_ratio = 0.15


output_path = r'D:/deep_space/MV/Dataset_split_3'


train_path = os.path.join(output_path, 'train')
test_path = os.path.join(output_path, 'test')

os.makedirs(train_path, exist_ok=True)
os.makedirs(test_path, exist_ok=True)


for class_folder in os.listdir(dataset_path):
    class_path = os.path.join(dataset_path, class_folder)
    
   
    train_class_path = os.path.join(train_path, class_folder)
    test_class_path = os.path.join(test_path, class_folder)
    
    os.makedirs(train_class_path, exist_ok=True)
    os.makedirs(test_class_path, exist_ok=True)
    
    
    files = os.listdir(class_path)
    
   
    num_train = int(len(files) * train_ratio)

    print(num_train)
    
    
    random.shuffle(files)
    
    
    for i, file in enumerate(files):
        img_path = os.path.join(class_path, file)
        img = Image.open(img_path)
        
        
        img = img.convert("RGB")
        
        if i < num_train:
            
            img.save(os.path.join(train_class_path, os.path.splitext(file)[0] + '.png'))
        else:
            
            img.save(os.path.join(test_class_path, os.path.splitext(file)[0] + '.png'))

print("save success:", output_path)
