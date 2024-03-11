## Converter 

Module to generate data for the dataset

## Run 
Run with generate function in generator main.py folder. 

```python
from generator.main import generate


generate(amount=5,
         samples_path='SAMPLES',
         dataset_name='DATASET_NAME')
```

### Parameters:

* amount - how many photos to generate
* samples_path - path to samples folder with data to fill generated photo
* dataset_path [Optional] - where to create dataset
    * if unset - generated in the same place where the generator is
    * if uploading - must be set and valid
* dataset_name [Optional] - name for a dataset
    * if unset - default name *'dataset'*
    * parameter is not used when generating to already existing dataset
* upload [Optional] - default False, set ***True*** to generate data to already present dataset 
    * If set True - *dataset_path* must be passed

### Samples

Samples is a folder with such structure:

```
samples         
    ├── sample_background_images    
    │       ├── image1.jpg        
    │       └── ...        
    ├── sample_fonts    
    │       ├── font1.ttf        
    │       └── ...     
    ├── sample_insert_images            
    │       ├── image1.jpg          
    │       └── ...        
    ├── sample_table_fonts        
    │       ├── font1.ttf           
    │       └── ...        
    ├── sample_text    
    │       ├── text1.txt         
    │       └── ...        
    ├── content_sentences.txt        
    └── content_words.txt    
  ```

**sample_background_images** - images used for background    
**sample_fonts** - fonts used for text blocks     
**sample_insert_images** - images to insert     
**sample_table_fonts** - fonts used for text in tables     
**sample_text** - texts used for text blocks    
**table_content_sentences.txt** - text file with sentences to fill tables. Each sentence must be from new line
**table_content_words.txt** - text file with words to fill tables and graphs. Each word must be from new line 






   