from trdg.generators import (
    GeneratorFromDict,
    GeneratorFromRandom,
    GeneratorFromStrings,
    GeneratorFromWikipedia,
)

# The generators use the same arguments as the CLI, only as parameters
generator = GeneratorFromStrings(
    ['Test1'],#, 'Test2', 'Test3'],
    blur=2,
    random_blur=True,
    count=3, # otherwise -1, infinite
)

for img, lbl in generator:
    # Do something with the pillow images here.
    print(lbl)
    img.show()

# USE trainer.ipynb with config directing to en_sample