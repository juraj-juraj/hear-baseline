![HEAR2021](https://neuralaudio.ai/assets/img/hear-header-sponsor.jpg)
# HEAR 2021 Baseline
Several baseline audio embeddings that implement the [common API](https://neuralaudio.ai/hear2021-rules.html#common-api)
required by the HEAR 2021 NeurIPS competition.

Includes a simple DSP-based audio embedding consisting of a Mel-frequency spectrogram 
followed by a random projection, implemented in PyTorch, TensorFlow, and Keras. 

Additionally, we wrap several benchmark audio embedding models.
However, many of them are ineffecient because of limiting assumptions
in the original implementation (e.g. only one audio file can be
processed at a time using their high-level API).

For the HEAR 2021 evaluation, `hearbaseline.wav2vec2` and `hearbaseline.torchcrepe` baseline
embeddings were used.

For full details on the HEAR 2021 NeurIPS competition please visit the
[competition website.](https://neuralaudio.ai)

### Installation

Tested with Python 3.7 and 3.8. Python 3.9 is not officially supported
because pip3 installs are very finicky, but it might work.

**Method 1: pypi**
```python
pip install hearbaseline
```

**Method 2: pip local source tree**

This is the same method that will be used to by competition organizers when installing
submissions to HEAR 2021.
```python
git clone https://github.com/neuralaudio/hear-baseline.git
python3 -m pip install -e ./hear-baseline
```

### Naive Baseline Model
The naive baseline model provides an example for implementing the HEAR 2021 common API
using DSP-based techniques. It produces log-scaled Mel-frequency spectrograms using a
256-band Mel filter. Each frame of the spectrogram is then projected to 4096
dimensions using a random projection matrix. Weights for the projection matrix were
generated by sampling a normal distribution and are stored in this repository in the
file `saved_models/naive_baseline.pt`.

Using a random projection is less efficient
than a CNN but is one of the simplest models to implement from a coding perspective.

### Usage

Audio embeddings can be computed using one of two methods: 1)
`get_scene_embeddings`, or 2) `get_timestamp_embeddings`.

`get_scene_embeddings` accepts a batch of audio clips and produces a single embedding
for each audio clip. This can be computed like so:
```python
import torch
import hearbaseline

# Load model with weights - located in the root directory of this repo
model = hearbaseline.load_model("saved_models/naive_baseline.pt")

# Create a batch of 2 white noise clips that are 2-seconds long
# and compute scene embeddings for each clip
audio = torch.rand((2, model.sample_rate * 2))
embeddings = hearbaseline.get_scene_embeddings(audio, model)
```

The `get_timestamp_embeddings` method works exactly the same but returns an array
of embeddings computed every 25ms over the duration of the input audio. An array
of timestamps corresponding to each embedding is also returned.

See the [common API](https://neuralaudio.ai/hear2021-rules.html#common-api)
for more details.

### Other Baselines

- `hearbaseline.torchcrepe`
- `hearbaseline.vggish`
- `hearbaseline.vqt`
- `hearbaseline.wav2vec2`
- `hearbaseline.keras.naive`
- `hearbaseline.tf.naive`
