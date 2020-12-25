# Google Dataset Creator
Creating datasets for personal deep learning projects using Google Images. Duplicate images found within the created dataset or any other dataset can also be automatically deleted.

### Usage

Open a command prompt and execute the following to download the repository:
```
git clone https://github.com/saifjamsheer/google-dataset-creator.git
```
Access the cloned repository by executing the following in the command prompt:
```
cd google-dataset-creator
```
Download the necessary libraries using the command prompt:
```
pip install -r requirements.txt
```
After generating the 'urls.txt' file by following the instructions in [urls.js](urls.js), run the following script to download the desired images:
```
create.py --urls url_textfile_path
```
To delete any duplicate images, ensure that all images are in [dataset](dataset) and run the following script:
```
delete.py
```

