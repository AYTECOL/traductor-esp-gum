# OCR Development for Namtrik using EasyOCR
Using:
* Main EasyOCR cutom model docs: https://github.com/JaidedAI/EasyOCR/blob/master/custom_model.md
* TextRecognitionDataGenerator: https://github.com/Belval/TextRecognitionDataGenerator
* Custom Datasets and pretrained models: https://jaided.ai/easyocr/modelhub/
* Benchmarking and training example: https://github.com/clovaai/deep-text-recognition-benchmark

## Run

* Make sure to be on \ocr and use an environment (e.g. virtualenv)
* Install requirements `pip install -r requirements.txt`
* Generate a dataset of word images: `python DataGenerator/data_generator.py`
* Use a model:
    1. Run `python EasyOCR/namtrik.py`. It will display the recognized textbox and text from an example image (in \EasyOCR\examples). It also will create a baseline user model folder.
    2. Copy \CustomModel folder content into Users\<your user>\.EasyOCR. *.pth files need to be in \model, and *.py and *.yaml on user_network. All three files must be named the same (e.g. custom_example, custom_model, modelSomething, etc.). Python files contain the architecture, YAML files containt the architecture configuration, and PTH files contain the binary model weights.
    3. Uncomment EasyOCR\namtrik.py line with the custom model from (2) using `reader = easyocr.Reader(['en'], recog_network='custom_example')`, and run. It will use the custom model.
* Train a model:
    1. Go to \EasyOCR\trainer
    2. Training and validation datasets should be on \all_data. Currently only training dataset (en_sample) is uploaded. Each contains images and a labels.csv file (with filename and text label).
    3. Config training files should be in \config_files
    4. Run trainer.ipynb notebook, it will call the config file and train.py over the configured dataset
    5. Output will be on \saved_models

## Acknowledgment

This is under development for Ayté only, it would be wise to split the OCR part on another repo with cleaner procedures once it is stable and replicable.